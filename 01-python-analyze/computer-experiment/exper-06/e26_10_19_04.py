import pandas as pd
from e26_10_19_03 import clean_df


def discretize_age(age):
    if pd.isna(age):
        return "未知"
    elif age < 18:
        return "少年"
    elif age < 35:
        return "青年"
    elif age < 60:
        return "中年"
    else:
        return "老年"


clean_df["年龄段"] = clean_df["年龄"].apply(discretize_age)

print(clean_df[["年龄", "年龄段"]].head())
