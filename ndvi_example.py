import numpy as np

# Simple NDVI example
nir = np.array([0.75, 0.80, 0.65])
red = np.array([0.30, 0.35, 0.40])

ndvi = (nir - red) / (nir + red)
print("NDVI values:", ndvi)
