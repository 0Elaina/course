import pandas as pd
from e26_10_19_02 import merged_df

valid_indices = []

for index, age in merged_df["年龄"].items():
    if pd.isna(age):
        continue

    # 判断年龄是否包含小数
    if age % 1 != 0:
        pass
    else:
        valid_indices.append(index)

# 根据正常索引过滤数据
clean_df = merged_df.loc[valid_indices].copy()

print(f"删除异常值后的数据量: {clean_df.shape}")
