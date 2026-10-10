import numpy as np

image = np.random.randint(0, 256, size=(100, 200, 3), dtype=np.uint8)

r = (image[:, :, 0] / 255.0).astype(np.float32)
g = (image[:, :, 1] / 255.0).astype(np.float32)
b = (image[:, :, 2] / 255.0).astype(np.float32)

g = np.sqrt(g)

new_image = np.stack([r, g, b], axis=-1)
print(f"shape={new_image.shape}")
print(f"type={new_image.dtype}")