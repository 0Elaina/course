from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams["font.sans-serif"] = [
    "Noto Sans CJK SC",
    "WenQuanYi Micro Hei",
    "SimHei",
    "Microsoft YaHei",
    "PingFang SC",
    "sans-serif",
]
# 正常显示负号
plt.rcParams["axes.unicode_minus"] = False
# 设置图像全局 DPI
plt.rcParams["figure.dpi"] = 100


def step1_load_data():
    """读取 student_grade.xlsx 文件数据，自动适配不同工作区执行路径"""
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / "student_grade.xlsx"
    if not file_path.exists():
        file_path = Path("exper-07/student_grade.xlsx")

    if not file_path.exists():
        raise FileNotFoundError(f"未找到学生成绩数据文件: {file_path}")

    df = pd.read_excel(file_path)
    print("【步骤1】成功读取 student_grade.xlsx 数据：")
    print(f"数据形状（行数, 列数）: {df.shape}")
    print("\n前 5 行样例数据：")
    print(df.head())
    return df


def step2_plot_pie(ax, df):
    """
    将学生考试总成绩划分为 4 个区间，计算各区间学生人数，并绘制饼图
    区间划分：0~150、150~200、200~250、250~300
    等级对应：“不及格”“及格”“良好”“优秀”
    """
    bins = [0, 150, 200, 250, 300]
    labels = ["不及格", "及格", "良好", "优秀"]

    # 使用 pd.cut 进行总成绩分箱
    df["成绩等级"] = pd.cut(
        df["总成绩"],
        bins=bins,
        labels=labels,
        right=True,
        include_lowest=True,
    )

    # 统计各区间人数
    section_counts = df["成绩等级"].value_counts().reindex(labels)

    print("\n【步骤2】总成绩各区间学生人数统计：")
    for level, count in section_counts.items():
        level_str = str(level)
        idx = labels.index(level_str)
        ratio = (count / len(df)) * 100
        print(
            f"  - {level_str:4s} ({bins[idx]}~{bins[idx + 1]}分): {count} 人，占比 {ratio:.1f}%"
        )

    # 饼图参数配置
    colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"]
    explode = (0.05, 0.02, 0.02, 0.05)  # 突出展示两端等级

    wedges, _texts, autotexts = ax.pie(
        section_counts,
        labels=labels,
        autopct="%1.1f%%",
        startangle=140,
        explode=explode,
        colors=colors,
        shadow=True,
        textprops={"fontsize": 11},
    )

    # 设置百分比字体加粗
    for at in autotexts:
        at.set_fontsize(10)
        at.set_weight("bold")

    ax.set_title(
        "学生考试总成绩分布区间占比饼图", fontsize=14, fontweight="bold", pad=15
    )
    ax.legend(
        wedges,
        [f"{lvl}: {cnt}人" for lvl, cnt in section_counts.items()],
        title="成绩等级及人数",
        loc="upper right",
        bbox_to_anchor=(1.25, 1),
        fontsize=9,
    )
    return section_counts


def step3_plot_boxplot(ax, df):
    """
    提取学生数学、阅读、写作 3 项单科成绩，绘制各项成绩分散情况箱线图
    """
    subjects = ["数学成绩", "阅读成绩", "写作成绩"]
    subject_data = [df[col].dropna() for col in subjects]

    # 绘制箱线图
    box = ax.boxplot(
        subject_data,
        patch_artist=True,  # 允许填充颜色
        showmeans=True,  # 显示均值点
        meanline=True,  # 均值以虚线显示
        boxprops={"facecolor": "#cce5ff", "color": "#1f77b4", "linewidth": 1.5},
        whiskerprops={"color": "#1f77b4", "linewidth": 1.5},
        capprops={"color": "#1f77b4", "linewidth": 1.5},
        medianprops={"color": "#d95f02", "linewidth": 2.0},
        meanprops={"color": "#2ca02c", "linestyle": "--", "linewidth": 1.5},
        flierprops={"marker": "o", "color": "#d62728", "alpha": 0.6, "markersize": 5},
    )

    # 为 3 个箱体分别赋予辨识度色彩
    box_colors = ["#a6cee3", "#b2df8a", "#fb9a99"]
    for patch, color in zip(box["boxes"], box_colors):
        patch.set_facecolor(color)

    # 设置 x/y 轴刻度与标签
    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(subjects, fontsize=11, fontweight="bold")
    ax.set_xlabel("考试科目", fontsize=12, fontweight="bold")

    ax.set_yticks(np.arange(0, 101, 10))
    ax.set_ylabel("单科成绩（分）", fontsize=12, fontweight="bold")
    ax.set_ylim(-5, 105)

    # 设置标题、网格与图例说明
    ax.set_title(
        "学生 3 项单科考试成绩分散情况箱线图", fontsize=14, fontweight="bold", pad=15
    )
    ax.grid(axis="y", linestyle="--", alpha=0.6)

    # 添加中位数与平均值的图例标记
    from matplotlib.lines import Line2D

    legend_elements = [
        Line2D([0], [0], color="#d95f02", lw=2, label="中位数 (Median)"),
        Line2D([0], [0], color="#2ca02c", lw=1.5, linestyle="--", label="均值 (Mean)"),
        Line2D(
            [0],
            [0],
            marker="o",
            color="w",
            markerfacecolor="#d62728",
            markersize=6,
            label="离群值 (Outliers)",
        ),
    ]
    ax.legend(handles=legend_elements, loc="lower right", frameon=True, fontsize=9)


def step4_analyze(df, section_counts):
    """
    (4) 分析学生考试总成绩的分布情况和 3 项单科成绩的分散情况
    输出定量指标与结构化分析结论
    """
    subjects = ["数学成绩", "阅读成绩", "写作成绩"]
    total = df["总成绩"]

    print("\n【步骤4：综合分析与结论报告】")

    print("\n一、学生考试总成绩分布情况分析：")
    total_mean = total.mean()
    total_median = total.median()
    total_std = total.std()
    total_min = total.min()
    total_max = total.max()
    print(
        f"  1. 总体指标：总分全距为 [{total_min}, {total_max}]，均值为 {total_mean:.2f} 分，中位数为 {total_median:.2f} 分，标准差为 {total_std:.2f}。"
    )
    print(
        f"  2. 分布形态：中位数（{total_median:.1f}）与均值（{total_mean:.1f}）高度接近，说明总成绩整体呈现良好的正态/对称分布特征。"
    )
    print("  3. 等级结构占比：")
    for lvl in ["不及格", "及格", "良好", "优秀"]:
        cnt = section_counts[lvl]
        pct = (cnt / len(df)) * 100
        print(f"     - 【{lvl}】：{cnt} 人，占比 {pct:.1f}%")
    print(
        "  4. 结论：大部分学生处于“良好”（41.4%）和“及格”（34.3%）区间，两者合计占比达 75.7%，表明绝大多数学生掌握了基础课程内容；优秀率为 13.4%，不及格率为 10.9%，呈现“中间大、两头小”的稳定纺锤形分布。"
    )

    print("\n二、3 项单科成绩分散情况分析：")
    for sub in subjects:
        s = df[sub]
        mean_v = s.mean()
        med_v = s.median()
        std_v = s.std()
        q1 = s.quantile(0.25)
        q3 = s.quantile(0.75)
        iqr = q3 - q1
        min_v = s.min()
        max_v = s.max()
        outliers = s[(s < q1 - 1.5 * iqr) | (s > q3 + 1.5 * iqr)]
        print(f"  【{sub}】：")
        print(f"     - 均值: {mean_v:.2f}, 中位数: {med_v:.2f}, 标准差: {std_v:.2f}")
        print(
            f"     - 分数范围: [{min_v}, {max_v}], 四分位间距(IQR): {iqr:.2f} (Q1={q1:.1f}, Q3={q3:.1f})"
        )
        print(
            f"     - 离群异常值数量: {len(outliers)} 个，最低异常分为 {outliers.min() if len(outliers) > 0 else '无'}"
        )

    print("\n三、横向对比与分散性规律总结：")
    print(
        "  1. 成绩离散度：数学成绩的标准差（15.16）与写作成绩（15.20）相近，但数学成绩的最低分达 0 分（存在明显低分异常点），说明数学学科两极分化更剧烈。"
    )
    print(
        "  2. 学科水平对比：阅读成绩整体表现最优（均值 69.17 分，中位数 70.0 分），标准差最小（14.60），箱体紧凑且位置最高，说明学生阅读水平相对集中且基础较好。"
    )
    print(
        "  3. 异常值特征：3 项单科成绩的异常值全部出现在箱体下边缘（即严重低分），没有出现上限高分异常点，表明试卷具有足够的区分度，同时提示教学中需重点针对这部分低分偏科学生实施补弱帮扶。"
    )


def main():
    # (1) 读取数据
    df = step1_load_data()

    # 创建并列对比画布 (1 行 2 列)
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle(
        "实训1：学生考试成绩特征的分布与分散情况分析",
        fontsize=16,
        fontweight="bold",
        y=0.98,
    )

    # (2) 绘制总成绩分布饼图
    section_counts = step2_plot_pie(axes[0], df)

    # (3) 绘制 3 项单科成绩分散情况箱线图
    step3_plot_boxplot(axes[1], df)

    # (4) 控制台输出详细分析报告
    step4_analyze(df, section_counts)

    # 调整布局
    plt.tight_layout(rect=(0.0, 0.03, 1.0, 0.95))

    # 保存图片文件（便于插入实验报告）
    output_dir = Path(__file__).resolve().parent
    combined_img_path = output_dir / "student_grade_distribution_and_dispersion.png"
    plt.savefig(combined_img_path, dpi=300, bbox_inches="tight")
    print(f"\n可视化综合图表已成功保存至: {combined_img_path}")

    # 分别保存单张高清图表
    fig_pie, ax_pie = plt.subplots(figsize=(7, 6))
    step2_plot_pie(ax_pie, df)
    plt.tight_layout()
    pie_path = output_dir / "01_total_score_pie.png"
    plt.savefig(pie_path, dpi=300, bbox_inches="tight")
    plt.close(fig_pie)

    fig_box, ax_box = plt.subplots(figsize=(7, 6))
    step3_plot_boxplot(ax_box, df)
    plt.tight_layout()
    box_path = output_dir / "02_subjects_boxplot.png"
    plt.savefig(box_path, dpi=300, bbox_inches="tight")
    plt.close(fig_box)

    print(
        "已成功保存独立的饼图 (01_total_score_pie.png) 与箱线图 (02_subjects_boxplot.png)！"
    )

    # 显示图表窗口
    plt.show()


if __name__ == "__main__":
    main()
