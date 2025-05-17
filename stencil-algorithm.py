# 2D Dask array for the mean stencil
import dask.array as da
import numpy as np

np_arr = np.random.randint(0, 10, size=(10, 10))
dask_arr = da.from_array(np_arr, chunks=(5, 5))

def stencil_mean_3x3(block):
    """Apply a 3x3 averaging stencil to a numpy block."""
    kernel = np.ones((3, 3)) / 9.0
    from scipy.signal import convolve2d
    return convolve2d(block, kernel, mode='valid')

result = dask_arr.map_overlap(
    stencil_mean_3x3,
    depth=1,              # 1-cell halo on all sides
    boundary='reflect',   # how to extend edges
    trim=True,            # remove halo after operation
    dtype=float
)

# Compute the final result
final = result.compute()
print(final)