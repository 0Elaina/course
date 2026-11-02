"""
一、数据集说明：

    用户表 (users)
        字段：用户ID、姓名、年龄、城市、注册日期
        脏数据示例：年龄为150、-5或缺失；城市缺失；注册日期格式错误（如2021/13/01）。

    交易记录表 (transactions)
        字段：交易 ID、用户 ID、交易日期、金额、产品类别
        脏数据示例：交易日期无效（2023-02-29或NaN）；金额为负数或极高异常值（10000）

二、实验内容

1.数据清洗：
    用户表：将异常年龄（>100 或 <0）替换为缺失值，用中位数填充年龄缺失；用众数填充城市缺失；将注册日期转换为标准日期格式并删除无效日期行。
    交易表：转换交易日期并删除无效行；将负金额和大于 5000 的异常金额替换为缺失值，用中位数填充金额缺失。

2.数据转换：
    从交易日期提取年、月、年月组合列，在原表中增加新列。
    计算每个用户的累计消费、平均消费、交易次数。
    根据累计消费金额划分消费水平（低、中、高、超高），
    提示：
     pd.cut(merged['累计消费'], bins=[0, 500, 2000, 5000, 100000], labels=['低', '中', '高', '超高'])

3. 数据合并
    通过用户 ID 内连接用户表和交易表，形成包含用户信息和交易记录的分析宽表。

4. 数据可视化
    绘制各城市总消费金额条形图。
    绘制每月消费总额趋势折线图。
    绘制年龄与平均消费金额的散点图（按城市着色）。
    绘制不同产品类别消费金额分布的箱线图。
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 支持中文字体显示（兼容 Linux / Windows / macOS 常见字体）
plt.rcParams["font.sans-serif"] = [
    "Noto Sans CJK SC",
    "WenQuanYi Micro Hei",
    "SimHei",
    "Microsoft YaHei",
    "PingFang SC",
    "sans-serif",
]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.dpi"] = 100


def get_data_path(filename):
    """自动兼容不同工作目录下的数据文件路径定位"""
    base_dir = Path(__file__).resolve().parent
    candidates = [
        base_dir / filename,
        Path("exper-08") / filename,
    ]
    for p in candidates:
        if p.exists():
            return p
    raise FileNotFoundError(f"未找到数据文件: {filename}")


# 1. 数据读取与清洗
def clean_users_data(users_path):
    """用户表数据清洗"""
    raw_users = pd.read_excel(users_path)
    assert isinstance(raw_users, pd.DataFrame)
    unnamed_cols = [c for c in raw_users.columns if str(c).startswith("Unnamed")]
    users = raw_users.drop(columns=unnamed_cols) if unnamed_cols else raw_users
    assert isinstance(users, pd.DataFrame)

    print("【1. 用户表清洗前】形状:", users.shape)

    # 年龄清洗：异常年龄（>100 或 <0）替换为缺失值，用中位数填充
    age_series = pd.Series(pd.to_numeric(users["年龄"], errors="coerce"))
    age_series.loc[(age_series < 0) | (age_series > 100)] = np.nan
    age_median = float(age_series.median())
    users["年龄"] = age_series.fillna(age_median)

    # 城市清洗：替换空值及字符串 'nan'，用众数填充
    city_series = pd.Series(users["城市"]).replace(["nan", "NaN", "None", ""], np.nan)
    city_mode = str(city_series.dropna().mode().iloc[0])
    users["城市"] = city_series.fillna(city_mode)

    # 注册日期清洗：转换为标准日期格式，删除格式错误导致的无效日期行
    users["注册日期"] = pd.to_datetime(users["注册日期"], errors="coerce")
    users = users.dropna(subset=["注册日期"]).copy()

    print("【1. 用户表清洗后】形状:", users.shape)
    print("年龄中位数填充值:", age_median, "城市众数填充值:", city_mode)
    print(users.head(3))
    return users


def clean_transactions_data(transactions_path):
    """交易记录表数据清洗"""
    raw_tx = pd.read_excel(transactions_path)
    assert isinstance(raw_tx, pd.DataFrame)
    unnamed_cols = [c for c in raw_tx.columns if str(c).startswith("Unnamed")]
    transactions = raw_tx.drop(columns=unnamed_cols) if unnamed_cols else raw_tx
    assert isinstance(transactions, pd.DataFrame)

    print("\n【1. 交易表清洗前】形状:", transactions.shape)

    # 交易日期清洗：转换为标准日期格式，删除无效日期行（如 2023-02-29）
    transactions["交易日期"] = pd.to_datetime(transactions["交易日期"], errors="coerce")
    transactions = transactions.dropna(subset=["交易日期"]).copy()

    # 金额清洗：负金额和大于 5000 的异常金额替换为缺失值，用中位数填充
    amount_series = pd.Series(pd.to_numeric(transactions["金额"], errors="coerce"))
    amount_series.loc[(amount_series < 0) | (amount_series > 5000)] = np.nan
    amount_median = float(amount_series.median())
    transactions["金额"] = amount_series.fillna(amount_median)

    print("【1. 交易表清洗后】形状:", transactions.shape)
    print("交易金额中位数填充值:", round(amount_median, 2))
    print(transactions.head(3))
    return transactions


# 2. 数据转换
def transform_transactions(transactions):
    """从交易日期提取年、月、年月组合列"""
    transactions["年"] = transactions["交易日期"].dt.year
    transactions["月"] = transactions["交易日期"].dt.month
    transactions["年月"] = transactions["交易日期"].dt.strftime("%Y-%m")
    return transactions


def calculate_user_stats(transactions):
    """计算每个用户的累计消费、平均消费、交易次数"""
    user_stats = (
        transactions.groupby("用户ID")
        .agg(
            累计消费=("金额", "sum"),
            平均消费=("金额", "mean"),
            交易次数=("交易ID", "count"),
        )
        .reset_index()
    )
    user_stats["累计消费"] = user_stats["累计消费"].round(2)
    user_stats["平均消费"] = user_stats["平均消费"].round(2)
    return user_stats


# 3. 数据合并
def merge_data(users, transactions, user_stats):
    """内连接用户表和交易表，并关联每个用户的统计特征与消费水平"""
    # 基础内连接：交易记录表 + 用户表
    merged = pd.merge(transactions, users, on="用户ID", how="inner")

    # 关联用户统计指标：累计消费、平均消费、交易次数
    merged = pd.merge(merged, user_stats, on="用户ID", how="left")

    # 根据累计消费金额划分消费水平（低、中、高、超高）
    bins = [0, 500, 2000, 5000, 100000]
    labels = ["低", "中", "高", "超高"]
    merged["消费水平"] = pd.cut(
        merged["累计消费"], bins=bins, labels=labels, right=True
    )

    print("\n【3. 分析宽表合并完成】宽表形状:", merged.shape)
    print("分析宽表前 3 条记录:")
    print(
        merged[
            [
                "交易ID",
                "用户ID",
                "姓名",
                "城市",
                "年龄",
                "金额",
                "产品类别",
                "年月",
                "累计消费",
                "平均消费",
                "消费水平",
            ]
        ].head(3)
    )
    return merged


# 4. 数据可视化
def plot_visualizations(merged, output_dir):
    """绘制 4 种分析图表，以 2x2 画布呈现"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(
        "电商用户与交易特征数据分析综合看板", fontsize=15, fontweight="bold", y=0.98
    )

    # (1) 各城市总消费金额条形图
    city_spending = merged.groupby("城市")["金额"].sum().sort_values(ascending=False)
    bars = axes[0, 0].bar(
        city_spending.index,
        city_spending.values,
        color="#4C72B0",
        edgecolor="black",
        width=0.55,
    )
    axes[0, 0].bar_label(bars, fmt="%.1f", padding=3, fontsize=9)
    axes[0, 0].set_title(
        "各城市总消费金额条形图", fontsize=11.5, fontweight="bold", pad=8
    )
    axes[0, 0].set_xlabel("城市", fontsize=10, fontweight="bold")
    axes[0, 0].set_ylabel("总消费金额 (元)", fontsize=10, fontweight="bold")
    axes[0, 0].grid(axis="y", linestyle="--", alpha=0.4)

    # (2) 每月消费总额趋势折线图
    monthly_spending = merged.groupby("年月")["金额"].sum().sort_index()
    axes[0, 1].plot(
        range(len(monthly_spending)),
        monthly_spending.values,
        marker="o",
        linewidth=2,
        color="#2ca02c",
        label="月度消费总额",
    )
    axes[0, 1].set_xticks(range(len(monthly_spending)))
    axes[0, 1].set_xticklabels(
        [str(x) for x in monthly_spending.index], rotation=45, ha="right", fontsize=8
    )
    axes[0, 1].set_title(
        "每月消费总额趋势折线图", fontsize=11.5, fontweight="bold", pad=8
    )
    axes[0, 1].set_xlabel("年月", fontsize=10, fontweight="bold")
    axes[0, 1].set_ylabel("消费总额 (元)", fontsize=10, fontweight="bold")
    axes[0, 1].grid(True, linestyle="--", alpha=0.4)
    axes[0, 1].legend(loc="upper left", fontsize=9, frameon=True)

    # (3) 年龄与平均消费金额的散点图（按城市着色）
    # 提取独立用户层面的年龄、城市与平均消费
    user_unique = merged.drop_duplicates(subset=["用户ID"])[
        ["用户ID", "年龄", "城市", "平均消费"]
    ]
    sns.scatterplot(
        data=user_unique,
        x="年龄",
        y="平均消费",
        hue="城市",
        palette="Set2",
        s=55,
        alpha=0.85,
        edgecolor="k",
        ax=axes[1, 0],
    )
    axes[1, 0].set_title(
        "用户年龄与平均消费金额散点图 (按城市着色)",
        fontsize=11.5,
        fontweight="bold",
        pad=8,
    )
    axes[1, 0].set_xlabel("年龄 (岁)", fontsize=10, fontweight="bold")
    axes[1, 0].set_ylabel("平均消费金额 (元)", fontsize=10, fontweight="bold")
    axes[1, 0].legend(title="城市", loc="upper left", fontsize=8.5, frameon=True)
    axes[1, 0].grid(True, linestyle="--", alpha=0.4)

    # (4) 不同产品类别消费金额分布的箱线图
    category_order = ["食品", "服装", "图书", "家居", "电子产品"]
    sns.boxplot(
        data=merged,
        x="产品类别",
        y="金额",
        hue="产品类别",
        legend=False,
        order=category_order,
        palette="Pastel1",
        boxprops={"linewidth": 1.2},
        whiskerprops={"linewidth": 1.2},
        capprops={"linewidth": 1.2},
        medianprops={"color": "#d95f02", "linewidth": 1.8},
        ax=axes[1, 1],
    )
    axes[1, 1].set_title(
        "不同产品类别消费金额分布箱线图", fontsize=11.5, fontweight="bold", pad=8
    )
    axes[1, 1].set_xlabel("产品类别", fontsize=10, fontweight="bold")
    axes[1, 1].set_ylabel("单笔交易金额 (元)", fontsize=10, fontweight="bold")
    axes[1, 1].grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout(rect=(0.0, 0.03, 1.0, 0.95))

    save_path = output_dir / "user_transaction_analysis.png"
    plt.savefig(save_path, dpi=300)
    print(f"\n【4. 可视化完成】分析大图已保存至: {save_path.name}")
    plt.show()


def main():
    users_path = get_data_path("users.xlsx")
    transactions_path = get_data_path("transactions.xlsx")
    output_dir = Path(__file__).resolve().parent

    # 1. 数据清洗
    users = clean_users_data(users_path)
    transactions = clean_transactions_data(transactions_path)

    # 2. 数据转换
    transactions = transform_transactions(transactions)
    user_stats = calculate_user_stats(transactions)

    # 3. 数据合并
    merged = merge_data(users, transactions, user_stats)

    # 4. 数据可视化
    plot_visualizations(merged, output_dir)


if __name__ == "__main__":
    main()
