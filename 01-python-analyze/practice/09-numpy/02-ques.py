import numpy as np

def printByName(name: str, value: any) -> None:
    print(f"{name}: {value}")
    print(f"--------------------")

def check(sales, core_view, core_backup) -> None:
    printByName("sales", sales)
    printByName("core_view", core_view)
    printByName("core_backup", core_backup)


np.random.seed(42)
sales = np.random.randint(10, 100, size=30).reshape(6, 5).astype(float)

core_view = sales[1:5, 1:4]
printByName("core_view", core_view)
core_backup = core_view.copy()

core_view[core_view % 2 == 0] = -99
check(sales, core_view, core_backup)

dirty_count = (sales == -99).sum()
print(f"dirty_count: {dirty_count}")

clean_sales = np.where(sales == -99, 20.0, sales)
printByName("clean_sales", clean_sales)

product_mean = clean_sales.mean(axis=0)
printByName("product_mean", product_mean)

relative_sales = np.round(clean_sales / product_mean, 2)
printByName("relative_sales", relative_sales)

store_totals = clean_sales.sum(axis=1)
printByName("store_totals", store_totals)

best_store = store_totals.argmax()
print(f"best_store: {best_store}")

desc_order = np.argsort(-store_totals)