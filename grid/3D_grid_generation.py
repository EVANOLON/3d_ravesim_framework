import logging
import math
from pathlib import Path
import tempfile
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def circle(radius: float, scale_x: float, scale_z: float) -> np.ndarray:
    """
    Generate a circle sample with materials 1 inside and 0 outside the circle
    """

    len_x = int(math.ceil(radius / scale_x * 2))
    print(len_x)
    len_z = int(math.ceil(radius / scale_z * 2))
    print(len_z)
    arr = np.zeros((len_z, len_x), dtype=np.int8)

    for iz in range(len_z):
        z = (iz - len_z / 2) * scale_z
        for ix in range(len_x):
            x = (ix - len_x / 2) * scale_x

            if x * x + z * z <= radius * radius:
                arr[iz, ix] = 1

    return arr

def square_3d(lenx: float, leny: float, lenz: float, scale_x: float, scale_y: float, scale_z: float) -> np.ndarray:
    len_x = int(math.ceil(lenx / scale_x))
    len_y = int(math.ceil(leny / scale_y))
    len_z = int(math.ceil(lenz / scale_z))
    arr = np.zeros((len_z, len_x, len_y), dtype=np.int8)

    for iz in range(len_z):
        for ix in range(len_x):
            for iy in range(len_y):
                arr[iz, ix, iy] = 1
    return arr

grid=square_3d(5e-6, 4e-6, 3e-6, 1 * 1e-6, 1 * 1e-6, 1 * 1e-6)
print(grid)
np.save("3d_square_5_4_3.npy",grid)
