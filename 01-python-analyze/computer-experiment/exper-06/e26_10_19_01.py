"""
一、有一个电商数据集，见“电商数据集.txt”,完成如下任务：
（1）把Q1和Q2两个季度的订单合并成一张全年订单表
（2）给订单补充客户姓名和城市，做客户为度分析
（3）将三表关联，订单+客户+商品，得到一张直接分析的宽表
（4）统计每位客户的下单总额，再按照客户索引join客户等级
（5）主客户表部分城市缺失，用历史存档表补全
"""

import pandas as pd
from ecommerce_data import (
    customers,
    customers_backup,
    orders_q1,
    orders_q2,
    products,
)

orders_all = pd.concat([orders_q1, orders_q2], axis=0, ignore_index=True)
print(orders_all)
print("=" * 70)

# 为订单补充客户姓名与城市
orders_customer = pd.merge(
    orders_all, customers[["customer_id", "name", "city"]], on="customer_id", how="left"
)
print(orders_customer)
print("=" * 70)

# 三表宽表
wide_table = orders_all.merge(
    customers[["customer_id", "name", "city", "level"]],
    on="customer_id",
    how="left",
).merge(
    products[["product_id", "product_name", "category", "unit_price"]],
    on="product_id",
    how="left",
)
print(wide_table)
print("=" * 70)

# 客户总额 + 按索引 join 等级
customer_total = (
    orders_all.groupby("customer_id")["amount"].sum().to_frame("total_amount")
)
customer_indexed = customers.set_index("customer_id")
customer_level_total = customer_total.join(customer_indexed[["level"]], how="left")
print(customer_level_total)
print("=" * 70)


# 补全城市
customers_filled = (
    customers.set_index("customer_id")
    .combine_first(customers_backup.set_index("customer_id"))
    .reset_index()
)
print(customers_filled)
