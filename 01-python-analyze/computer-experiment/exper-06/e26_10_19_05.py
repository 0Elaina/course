import numpy as np
import pandas as pd

df = pd.read_excel("exper-06/demo_100.xlsx", dtype=str)  # 先全部按字符串读入，便于清洗

# 姓名去首尾空格
df["姓名"] = df["姓名"].str.strip()


# 性别统一为 男/女
def norm_gender(x):
    if pd.isna(x):
        return np.nan
    x = str(x).strip().lower()
    if x in ["男", "male", "m"]:
        return "男"
    if x in ["女", "female", "f"]:
        return "女"
    return np.nan


df["性别"] = df["性别"].apply(norm_gender)

# 拆分省份/城市 + 提取产品编号数字
# 地区形如 "广东省,广州市"
split_region = df["地区"].str.split(",", n=1, expand=True)
df["省份"] = split_region[0].str.strip()
df["城市"] = split_region[1].str.strip()

# 产品编号数字
df["产品编号数字"] = df["产品编号"].str.extract(r"(\d+)").astype(int)

# 3. 特殊字符识别为缺失值
missing_tokens = ["?", "？", "#", "*", "", " ", "nan", "none", "null", "na"]


def to_missing(x):
    if pd.isna(x):
        return np.nan
    s = str(x).strip().lower()
    if s in missing_tokens:
        return np.nan
    return x


for col in [
    "姓名",
    "性别",
    "地区",
    "年龄",
    "销售额",
    "工资",
    "产品编号",
    "省份",
    "城市",
]:
    df[col] = df[col].apply(to_missing)

# 数值列强制转数值（残留符号如 "3000*"、"12000#" 会变 NaN）
for col in ["年龄", "销售额", "工资"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# 缺失值填充（按城市中位数 → 全局中位数）
for col in ["年龄", "销售额", "工资"]:
    # 按城市分组中位数填充
    city_median = df.groupby("城市")[col].transform("median")
    df[col] = df[col].fillna(city_median)
    # 剩余用全局中位数填充
    df[col] = df[col].fillna(df[col].median())

# 异常值处理
# (a) 销售额、工资 > 0，负值替换为中位数
for col in ["销售额", "工资"]:
    med = df[col].median()
    df.loc[df[col] <= 0, col] = med
    # 3σ 检查异常值并删除
    mu, sigma = df[col].mean(), df[col].std()
    df = df[(df[col] >= mu - 3 * sigma) & (df[col] <= mu + 3 * sigma)]

# (b) 年龄限定 [0,120]，越界用中位数填充
age_med = df["年龄"].median()
df.loc[(df["年龄"] < 0) | (df["年龄"] > 120), "年龄"] = age_med

# IQR 检查年龄异常值并删除
Q1, Q3 = df["年龄"].quantile(0.25), df["年龄"].quantile(0.75)
IQR = Q3 - Q1
low, high = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
df = df[(df["年龄"] >= low) & (df["年龄"] <= high)]

# 重置索引
df = df.reset_index(drop=True)

# 保存清洗后数据
out_cols = [
    "姓名",
    "性别",
    "地区",
    "年龄",
    "销售额",
    "工资",
    "产品编号",
    "省份",
    "城市",
    "产品编号数字",
]
df = df[out_cols]
df.to_csv("exper-06/demo_100_cleaned.csv", index=False, encoding="utf-8-sig")

print("清洗完成，共保留", len(df), "行")
print(df.head())
