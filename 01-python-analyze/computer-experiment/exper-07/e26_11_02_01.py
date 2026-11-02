"""
1.读取tip.csv文件中的数据，显示前5条记录
2.完成下列绘图任务，分别用Matplotlib和Seanborn实现，并添加坐标刻度，标签，标题等基本属性。
（1）.观察账单金额和小费之间的相关关系，绘制散点图
（2）.观察每周各天的平均消费，绘制条形图
（3）.按就餐人数size的平均小费变化趋势，绘制折线图
（4）.查看样本中餐、晚餐样本数量占比，绘制饼状图；（仅用Matplotlib实现即可）
（5）.查看不同日期、是否吸烟人群的平均账单，并绘制热力图（提示先做透视表，tips.pivot_table(index="smoker", columns="day", values="total_bill", aggfunc="mean")）
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

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


def step1_load_data():
    """读取 tips.csv / tip.csv 文件数据，显示前 5 条记录"""
    base_dir = Path(__file__).resolve().parent
    candidates = [
        base_dir / "tips.csv",
        base_dir / "tip.csv",
        Path("exper-07/tips.csv"),
        Path("exper-07/tip.csv"),
    ]
    file_path = None
    for p in candidates:
        if p.exists():
            file_path = p
            break

    if file_path is None:
        raise FileNotFoundError("未找到数据文件 tips.csv 或 tip.csv")

    tips = pd.read_csv(file_path)
    print("【步骤1】成功读取数据，前 5 条记录如下：")
    print(tips.head())
    return tips


def plot_task1_scatter(ax_mpl, ax_sns, tips):
    """(1) 账单金额与小费相关关系散点图"""
    # Matplotlib
    ax_mpl.scatter(
        tips["total_bill"],
        tips["tip"],
        color="#1f77b4",
        alpha=0.7,
        edgecolors="k",
        s=25,
        label="顾客样本",
    )
    ax_mpl.set_xticks(np.arange(0, 55, 10))
    ax_mpl.set_yticks(np.arange(0, 11, 2))
    ax_mpl.set_xlabel("账单金额 ($)", fontsize=9.5)
    ax_mpl.set_ylabel("小费金额 ($)", fontsize=9.5)
    ax_mpl.set_xlim(0, 55)
    ax_mpl.set_ylim(0, 11)
    ax_mpl.set_title(
        "Matplotlib: (1) 账单与小费散点图", fontsize=10.5, fontweight="bold", pad=6
    )
    ax_mpl.legend(loc="upper left", fontsize=8.5, frameon=True)
    ax_mpl.grid(True, linestyle="--", alpha=0.4)

    # Seaborn
    sns.scatterplot(
        data=tips,
        x="total_bill",
        y="tip",
        hue="time",
        style="time",
        palette={"Dinner": "#e41a1c", "Lunch": "#377eb8"},
        s=30,
        alpha=0.8,
        ax=ax_sns,
    )
    ax_sns.set_xticks(np.arange(0, 55, 10))
    ax_sns.set_yticks(np.arange(0, 11, 2))
    ax_sns.set_xlabel("账单金额 ($)", fontsize=9.5)
    ax_sns.set_ylabel("小费金额 ($)", fontsize=9.5)
    ax_sns.set_xlim(0, 55)
    ax_sns.set_ylim(0, 11)
    ax_sns.set_title(
        "Seaborn: (1) 账单与小费散点图", fontsize=10.5, fontweight="bold", pad=6
    )
    ax_sns.legend(loc="upper left", fontsize=8, frameon=True)
    ax_sns.grid(True, linestyle="--", alpha=0.4)


def plot_task2_bar(ax_mpl, ax_sns, tips):
    """(2) 每周各天平均消费条形图"""
    day_order = ["Thur", "Fri", "Sat", "Sun"]
    day_labels = ["周四", "周五", "周六", "周日"]
    day_avg = tips.groupby("day")["total_bill"].mean().reindex(day_order)

    # Matplotlib
    bars = ax_mpl.bar(
        range(len(day_order)),
        day_avg.values,
        color="#4C72B0",
        edgecolor="black",
        width=0.55,
    )
    ax_mpl.bar_label(bars, fmt="%.2f", padding=2, fontsize=8.5)
    ax_mpl.set_xticks(range(len(day_order)))
    ax_mpl.set_xticklabels(day_labels, fontsize=9)
    ax_mpl.set_yticks(np.arange(0, 31, 5))
    ax_mpl.set_ylim(0, 26)
    ax_mpl.set_xlabel("星期", fontsize=9.5)
    ax_mpl.set_ylabel("平均消费 ($)", fontsize=9.5)
    ax_mpl.set_title(
        "Matplotlib: (2) 各天平均消费条形图", fontsize=10.5, fontweight="bold", pad=6
    )
    ax_mpl.grid(axis="y", linestyle="--", alpha=0.4)

    # Seaborn
    sns.barplot(
        data=tips,
        x="day",
        y="total_bill",
        hue="day",
        legend=False,
        order=day_order,
        palette="Blues_d",
        errorbar=None,
        ax=ax_sns,
    )
    ax_sns.set_xticks(range(len(day_order)))
    ax_sns.set_xticklabels(day_labels, fontsize=9)
    ax_sns.set_yticks(np.arange(0, 31, 5))
    ax_sns.set_ylim(0, 26)
    ax_sns.set_xlabel("星期", fontsize=9.5)
    ax_sns.set_ylabel("平均消费 ($)", fontsize=9.5)
    for p in ax_sns.patches:
        height = p.get_height()
        ax_sns.annotate(
            f"{height:.2f}",
            (p.get_x() + p.get_width() / 2.0, height),
            ha="center",
            va="bottom",
            fontsize=8.5,
            xytext=(0, 2),
            textcoords="offset points",
        )
    ax_sns.set_title(
        "Seaborn: (2) 各天平均消费条形图", fontsize=10.5, fontweight="bold", pad=6
    )
    ax_sns.grid(axis="y", linestyle="--", alpha=0.4)


def plot_task3_line(ax_mpl, ax_sns, tips):
    """(3) 就餐人数与平均小费变化趋势折线图"""
    size_avg = tips.groupby("size")["tip"].mean().reset_index()

    # Matplotlib
    ax_mpl.plot(
        size_avg["size"],
        size_avg["tip"],
        marker="o",
        linewidth=2,
        color="#2ca02c",
    )
    for _, row in size_avg.iterrows():
        ax_mpl.annotate(
            f"{row['tip']:.2f}",
            (row["size"], row["tip"]),
            textcoords="offset points",
            xytext=(0, 5),
            ha="center",
            fontsize=8.5,
            fontweight="bold",
        )
    ax_mpl.set_xticks(size_avg["size"])
    ax_mpl.set_xticklabels([f"{int(s)}人" for s in size_avg["size"]], fontsize=9)
    ax_mpl.set_yticks(np.arange(1.0, 6.1, 1.0))
    ax_mpl.set_ylim(1.0, 5.8)
    ax_mpl.set_xlabel("就餐人数 (size)", fontsize=9.5)
    ax_mpl.set_ylabel("平均小费 ($)", fontsize=9.5)
    ax_mpl.set_title(
        "Matplotlib: (3) 就餐人数与小费折线图", fontsize=10.5, fontweight="bold", pad=6
    )
    ax_mpl.grid(True, linestyle="--", alpha=0.4)

    # Seaborn
    sns.lineplot(
        data=size_avg,
        x="size",
        y="tip",
        marker="s",
        color="#2ca02c",
        linewidth=2,
        ax=ax_sns,
    )
    for _, row in size_avg.iterrows():
        ax_sns.annotate(
            f"{row['tip']:.2f}",
            (row["size"], row["tip"]),
            textcoords="offset points",
            xytext=(0, 5),
            ha="center",
            fontsize=8.5,
            fontweight="bold",
        )
    ax_sns.set_xticks(size_avg["size"])
    ax_sns.set_xticklabels([f"{int(s)}人" for s in size_avg["size"]], fontsize=9)
    ax_sns.set_yticks(np.arange(1.0, 6.1, 1.0))
    ax_sns.set_ylim(1.0, 5.8)
    ax_sns.set_xlabel("就餐人数 (size)", fontsize=9.5)
    ax_sns.set_ylabel("平均小费 ($)", fontsize=9.5)
    ax_sns.set_title(
        "Seaborn: (3) 就餐人数与小费折线图", fontsize=10.5, fontweight="bold", pad=6
    )
    ax_sns.grid(True, linestyle="--", alpha=0.4)


def plot_task4_pie_and_count(ax_mpl, ax_sns, tips):
    """(4) 中餐/晚餐样本数量占比饼图（题目要求仅用Matplotlib），右侧配 Seaborn 频数图对照"""
    time_counts = tips["time"].value_counts()
    labels = ["晚餐", "中餐"]
    sizes = [time_counts.get("Dinner", 0), time_counts.get("Lunch", 0)]

    # Matplotlib 饼图
    wedges, _texts, autotexts = ax_mpl.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90,
        explode=(0.04, 0),
        colors=["#ff9999", "#66b3ff"],
        shadow=True,
        textprops={"fontsize": 9.5},
    )
    for at in autotexts:
        at.set_fontsize(9.5)
        at.set_weight("bold")
    ax_mpl.set_title(
        "Matplotlib: (4) 中餐/晚餐占比饼图", fontsize=10.5, fontweight="bold", pad=6
    )
    ax_mpl.legend(
        wedges,
        [f"{lbl}: {cnt}人" for lbl, cnt in zip(labels, sizes)],
        loc="lower center",
        bbox_to_anchor=(0.5, -0.22),
        ncol=2,
        fontsize=8,
    )

    # Seaborn 频数条形图对照
    sns.countplot(
        data=tips,
        x="time",
        hue="time",
        legend=False,
        order=["Dinner", "Lunch"],
        palette=["#ff9999", "#66b3ff"],
        ax=ax_sns,
    )
    ax_sns.set_xticks([0, 1])
    ax_sns.set_xticklabels(["晚餐", "中餐"], fontsize=9)
    ax_sns.set_xlabel("用餐时段", fontsize=9.5)
    ax_sns.set_ylabel("样本数", fontsize=9.5)
    ax_sns.set_yticks(np.arange(0, 201, 50))
    for p in ax_sns.patches:
        height = p.get_height()
        ax_sns.annotate(
            f"{int(height)}人",
            (p.get_x() + p.get_width() / 2.0, height),
            ha="center",
            va="bottom",
            fontsize=8.5,
            xytext=(0, 2),
            textcoords="offset points",
        )
    ax_sns.set_title(
        "Seaborn: (4) 用餐时段频数统计", fontsize=10.5, fontweight="bold", pad=6
    )
    ax_sns.grid(axis="y", linestyle="--", alpha=0.4)


def plot_task5_heatmap(ax_mpl, ax_sns, tips, fig):
    """(5) 不同日期、是否吸烟人群平均账单热力图"""
    day_order = ["Thur", "Fri", "Sat", "Sun"]
    pivot = tips.pivot_table(
        index="smoker", columns="day", values="total_bill", aggfunc="mean"
    ).reindex(columns=day_order)

    # Matplotlib
    matrix = pivot.values
    im = ax_mpl.imshow(matrix, cmap="YlGnBu", aspect="auto")
    for i in range(len(pivot.index)):
        for j in range(len(pivot.columns)):
            val = matrix[i, j]
            color = "white" if val > 21 else "black"
            ax_mpl.text(
                j,
                i,
                f"{val:.2f}",
                ha="center",
                va="center",
                color=color,
                fontsize=9.5,
                fontweight="bold",
            )
    ax_mpl.set_xticks(range(len(day_order)))
    ax_mpl.set_xticklabels(["周四", "周五", "周六", "周日"], fontsize=9)
    ax_mpl.set_yticks([0, 1])
    ax_mpl.set_yticklabels(["不吸烟", "吸烟"], fontsize=9)
    ax_mpl.set_xlabel("星期", fontsize=9.5)
    ax_mpl.set_ylabel("是否吸烟", fontsize=9.5)
    ax_mpl.set_title(
        "Matplotlib: (5) 平均账单热力图", fontsize=10.5, fontweight="bold", pad=6
    )
    cbar = fig.colorbar(im, ax=ax_mpl, fraction=0.046, pad=0.04)
    cbar.ax.tick_params(labelsize=8)
    cbar.set_label("($)", fontsize=8.5)

    # Seaborn
    sns.heatmap(
        pivot,
        annot=True,
        fmt=".2f",
        cmap="YlGnBu",
        cbar_kws={"label": "($)"},
        annot_kws={"size": 9.5, "weight": "bold"},
        ax=ax_sns,
    )
    ax_sns.set_xticklabels(["周四", "周五", "周六", "周日"], fontsize=9)
    ax_sns.set_yticklabels(["不吸烟", "吸烟"], fontsize=9, rotation=0)
    ax_sns.set_xlabel("星期", fontsize=9.5)
    ax_sns.set_ylabel("是否吸烟", fontsize=9.5)
    ax_sns.set_title(
        "Seaborn: (5) 平均账单热力图", fontsize=10.5, fontweight="bold", pad=6
    )


def main():
    tips = step1_load_data()
    output_dir = Path(__file__).resolve().parent

    # 仅创建唯一样式的一张横向 2行5列 对比大图（完全匹配宽屏，上层Matplotlib，下层Seaborn）
    # 彻底杜绝多窗口弹出以及 5 行垂直堆叠带来的文字重叠挤压
    fig, axes = plt.subplots(2, 5, figsize=(18, 8.5))
    fig.suptitle(
        "tips 数据集可视化分析：Matplotlib（上）与 Seaborn（下）全任务对比",
        fontsize=14,
        fontweight="bold",
        y=0.98,
    )

    # 列任务对应：Col 0 -> 任务1，Col 1 -> 任务2，Col 2 -> 任务3，Col 3 -> 任务4，Col 4 -> 任务5
    plot_task1_scatter(axes[0, 0], axes[1, 0], tips)
    plot_task2_bar(axes[0, 1], axes[1, 1], tips)
    plot_task3_line(axes[0, 2], axes[1, 2], tips)
    plot_task4_pie_and_count(axes[0, 3], axes[1, 3], tips)
    plot_task5_heatmap(axes[0, 4], axes[1, 4], tips, fig=fig)

    # 充裕的行列间距，左边留出 6% 边距保证 y 轴标签不挤压
    plt.subplots_adjust(
        top=0.91, bottom=0.09, left=0.06, right=0.98, hspace=0.38, wspace=0.32
    )

    save_path = output_dir / "tips_visualization_comparison.png"
    plt.savefig(save_path, dpi=300)
    print(f"已成功保存对比全览图至: {save_path.name}")

    plt.show()


if __name__ == "__main__":
    main()
