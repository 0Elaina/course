"""
Python 数据合并方法实战演示
场景：某电商平台「优选生活」的数据合并分析
覆盖：concat / merge / join / combine_first / merge_asof / merge_ordered
"""

import pandas as pd

print("=" * 60)
print("① 原始数据准备")
print("=" * 60)
# ---- 订单表（一季度 & 二季度，同一表结构，用于纵向拼接） ----
orders_q1 = pd.DataFrame(
    [
        ["O101", "C01", "P01", "2024-01-12", 2, 9998],
        ["O102", "C02", "P02", "2024-01-25", 1, 5499],
        ["O103", "C01", "P03", "2024-02-08", 3, 2037],
        ["O104", "C04", "P01", "2024-02-20", 1, 4999],
        ["O105", "C03", "P04", "2024-03-05", 2, 2598],
    ],
    columns=[
        "order_id",
        "customer_id",
        "product_id",
        "order_date",
        "quantity",
        "amount",
    ],
)
orders_q2 = pd.DataFrame(
    [
        ["O201", "C02", "P02", "2024-04-11", 1, 5499],
        ["O202", "C05", "P05", "2024-04-18", 1, 6999],  # 新客户 C05、新产品 P05
        ["O203", "C01", "P01", "2024-05-02", 1, 4999],
        ["O204", "C03", "P03", "2024-05-16", 4, 2716],
        ["O205", "C04", "P04", "2024-06-09", 2, 2598],
    ],
    columns=[
        "order_id",
        "customer_id",
        "product_id",
        "order_date",
        "quantity",
        "amount",
    ],
)
# ---- 客户表（主表，部分 city 缺失，用于 combine_first） ----
customers = pd.DataFrame(
    [
        ["C01", "张伟", "上海", "金卡"],
        ["C02", "李娜", None, "银卡"],
        ["C03", "王芳", "广州", "金卡"],
        ["C04", "刘强", "深圳", "普通"],
        ["C05", "陈静", None, "普通"],
        ["C06", "陈来", None, "银卡"],
    ],
    columns=["customer_id", "name", "city", "level"],
)
# ---- 历史存档客户表（用于补全缺失城市） ----
customers_backup = pd.DataFrame(
    [
        ["C02", "北京"],
        ["C05", "杭州"],
    ],
    columns=["customer_id", "city"],
)
# ---- 商品表 ----
products = pd.DataFrame(
    [
        ["P01", "智能手表", "数码", 4999],
        ["P02", "空气净化器", "家电", 5499],
        ["P03", "电动牙刷", "个护", 679],
        ["P04", "蓝牙耳机", "数码", 1299],
        ["P05", "智能音箱", "数码", 6999],
    ],
    columns=["product_id", "product_name", "category", "unit_price"],
)
# ---- 折扣生效时间表（用于 merge_asof：订单匹配下单时最新折扣率） ----
promo = pd.DataFrame(
    [
        ["2024-01-01", 0.95],
        ["2024-02-15", 0.88],
        ["2024-04-01", 0.90],
        ["2024-05-20", 0.85],
    ],
    columns=["effective_time", "discount_rate"],
)
# ---- 月度销售表（用于 merge_ordered 时间序列演示） ----
monthly_q1 = pd.DataFrame(
    [
        ["2024-01", 5],
        ["2024-02", 7],
        ["2024-03", 9],
    ],
    columns=["month", "sales_q1"],
)
monthly_q2 = pd.DataFrame(
    [
        ["2024-01", 11],
        ["2024-02", 15],
        ["2024-04", 8],
        ["2024-05", 10],
    ],
    columns=["month", "sales_q2"],
)
