import pandas as pd

# exper-06/healthcare-dataset-age_abs (1).xls

# 读取中风患者的基础信息和体检数据表
stroke_df = pd.read_excel("exper-06/healthcare-dataset-stroke (1).xls")
# 读取年龄和平均血糖数据表
age_abs_df = pd.read_excel("exper-06/healthcare-dataset-age_abs (1).xls")


# 查看两表的数据量
print(f"中风基础数据表形状: {stroke_df.shape}")
print(f"年龄血糖数据表形状: {age_abs_df.shape}")

# 以编号作为主键进行外连接
merged_df = pd.merge(stroke_df, age_abs_df, on="编号", how="outer")

# 查看数据是否合并成功
print(f"合并后数据表形状: {merged_df.shape}")
print(merged_df.head())
