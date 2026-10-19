"""
1.统计每个部门的 平均工资、最高工资、人数
2.给每个人加一列 「部门平均工资」，保留所有行
3.新增一列 「工资等级」,工资 ≥ 12000 → ' 高';8000 ≤ 工资 < 12000 → ' 中';其他 → ' 低'
4.取出 每个部门工资最高的 1 个人
5.做透视表1,行：部门; 列：绩效; 值：工资; 计算：平均值
6.做透视表2，行：部门; 列：绩效; 值：工资、工龄；工资算：平均、最高；工龄算：平均、总和，
要求：列名全部中文，顺序固定，无警告

数据为：

import pandas as pd df =
pd.DataFrame({
'部门': ['销售', '销售', '技术', '技术', '技术', '人事', '人事'],
'姓名': ['张三', '李四', '王五', '赵六', '钱七', '孙八', '周九'],
'工资': [8000, 9000, 12000, 11000, 13000, 7000, 7500],
'工龄': [3, 4, 5, 2, 6, 1, 2],
'绩效': ['A', 'B', 'A', 'B', 'A', 'C', 'B'] })
"""

import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)

df = pd.DataFrame(
    {
        "部门": ["销售", "销售", "技术", "技术", "技术", "人事", "人事"],
        "姓名": ["张三", "李四", "王五", "赵六", "钱七", "孙八", "周九"],
        "工资": [8000, 9000, 12000, 11000, 13000, 7000, 7500],
        "工龄": [3, 4, 5, 2, 6, 1, 2],
        "绩效": ["A", "B", "A", "B", "A", "C", "B"],
    }
)

dept_stat = (
    df.groupby("部门")
    .agg(
        avg_wage=("工资", "mean"),
        max_wage=("工资", "max"),
        person_count=("姓名", "count"),
    )
    .reset_index()
)
print(dept_stat)
print("\n" + "=" * 70 + "\n")

df["部门平均工资"] = df.groupby("部门")["工资"].transform("mean")
print(df)
print("\n" + "=" * 70 + "\n")


def level(x):
    if x >= 12000:
        return "高"
    elif x >= 8000:
        return "中"
    else:
        return "低"


df["工资等级"] = df["工资"].apply(level)
print(df)
print("\n" + "=" * 70 + "\n")


pt1 = pd.pivot_table(df, index="部门", columns="绩效", values="工资", aggfunc="mean")
pt1 = pt1.reset_index()
pt1.columns.name = None
print(pt1)
print("\n" + "=" * 70 + "\n")

pt2 = pd.pivot_table(
    df,
    index="部门",
    columns="绩效",
    values=["工资", "工龄"],
    aggfunc={"工资": ["mean", "max"], "工龄": ["mean", "sum"]},
)
metric_map = {"工资": "工资", "工龄": "工龄"}
calc_map = {"mean": "平均", "max": "最高", "sum": "总和"}
pt2.columns = [f"{metric_map[v]}{calc_map[a]}_{p}" for v, a, p in pt2.columns]
order = []
for perf in ["A", "B", "C"]:
    for m in ["工资平均", "工资最高", "工龄平均", "工龄总和"]:
        col = f"{m}_{perf}"
        if col in pt2.columns:
            order.append(col)
pt2 = pt2[order]
pt2.columns.name = None
pt2 = pt2.reset_index()
print(pt2)