import numpy as np

martix = np.arange(10, 59, 2, dtype=int).reshape(5, 5)
print(f"martix: {martix}")
core_view = martix[1:4, 1:4]
print(f"martix: {martix}")
print(f"core_view: {core_view}")
core_snapshot = martix[1:4, 1:4].copy()
print(f"martix: {martix}")
print(f"core_view: {core_snapshot}")

print(f"\n ---------------------- \n")

core_view[:] = -1
print(f"martix: {martix}")
print(f"core_view: {core_view}")
print(f"core_snapshot: {core_snapshot}")

print(f"\n ---------------------- \n")

last_row = martix[-1, :].ravel()
last_col = martix[:, -1].ravel()
print(f"last_row: {last_row}")
print(f"last_col: {last_col}")
