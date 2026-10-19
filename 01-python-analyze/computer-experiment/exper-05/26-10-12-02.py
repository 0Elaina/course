import pandas as pd

"""
获取所有“篮球”运动员基本信息
统计男篮、女篮运动员的年龄、身高、体重的平均值以及极差值（最大-最小）
统计男篮运动员的体质指数，并增加一列为“体质指数”
体质指数（BMI）=体重（公斤）除以身高（米）的平方
"""

pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)

df = pd.read_excel("./exper-05/TYSJ.xlsx")

basketball = df[df["项目"] == "篮球"]
print(basketball)
print("\n" + "=" * 60 + "\n")

cols = ["年龄（岁）", "身高（cm)", "体重（kg）"]
mean_result = basketball.groupby("性别")[cols].mean()
print(mean_result)
print("\n" + "=" * 60 + "\n")

range_result = basketball.groupby("性别")[cols].agg(lambda x: x.max() - x.min())
print(range_result)
print("\n" + "=" * 60 + "\n")

male_bb = basketball[basketball["性别"] == "男"].copy()
male_bb["体质指数"] = male_bb["体重（kg）"] / (male_bb["身高（cm)"] / 100) ** 2
print(male_bb)
