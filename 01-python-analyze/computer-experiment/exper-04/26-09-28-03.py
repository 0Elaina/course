import numpy as np

a = [6, 2, 5, 0, 1, 3, 4, 7, 8, 9]
b = ["2", "3", "1", 5, 7]

shaped_a = np.array(a, dtype=int).reshape(2, 5)
shaped_b = np.array(b, dtype=int).reshape(1, 5)

print(f"[result]\n{shaped_a + shaped_b}")
