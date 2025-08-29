import logging
import math
from pathlib import Path
import tempfile
import numpy as np
import matplotlib.pyplot as plt

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

def square(lenx: float, lenz: float, scale_x: float, scale_z: float) -> np.ndarray:
    len_x = int(math.ceil(lenx / scale_x * 2))
    len_z = int(math.ceil(lenz / scale_z * 2))
    arr = np.zeros((len_z, len_x), dtype=np.int8)

    for iz in range(len_z):
        for ix in range(len_x):
            arr[iz, ix] = 1
    return arr
#grid=circle(3e-5, 10 * 1e-6, 10 * 1e-6)
#print(grid)
#grid=square(1e-6, 5e-6, 1 * 1e-6, 1 * 1e-6)
#print(grid)
#np.save("square_grid_1_5_1_1.npy",grid)
#0704-square(2e-4, 2e-3, 5 * 1e-6, 5 * 1e-6)

def hollowcircle(radius1: float, radius2: float, scale_x: float, scale_z: float) -> np.ndarray:
    len_x1=int(math.ceil(radius1 / scale_x * 2))
    len_z1=int(math.ceil(radius1 / scale_z * 2))
    arr = np.zeros((len_z1, len_x1), dtype=np.int8)
    for iz in range(len_z1):
        z = (iz - len_z1 / 2) * scale_z
        for ix in range(len_x1):
            x = (ix - len_x1 / 2) * scale_x

            if x * x + z * z <= radius1 * radius1 and x * x + z * z >= radius2 * radius2:
                arr[iz, ix] = 1
            elif  x * x + z * z <= radius2 * radius2:
                arr[iz, ix] = 0
    return arr
def double_ring(radius1: float, radius2: float, radius3: float, scale_x: float, scale_z: float) -> np.ndarray:
    len_x1=int(math.ceil(radius1 / scale_x * 2))
    len_z1=int(math.ceil(radius1 / scale_z * 2))
    arr = np.zeros((len_z1, len_x1), dtype=np.int8)
    for iz in range(len_z1):
        z = (iz - len_z1 / 2) * scale_z
        for ix in range(len_x1):
            x = (ix - len_x1 / 2) * scale_x

            if x * x + z * z <= radius1 * radius1 and x * x + z * z >= radius2 * radius2:
                arr[iz, ix] = 1
            elif  x * x + z * z <= radius2 * radius2 and x * x + z * z >= radius3 * radius3:
                arr[iz, ix] = 2
            else:
                arr[iz, ix] = 0
    return arr
def triple_ring(radius1: float, radius2: float, radius3: float, radius4: float, scale_x: float, scale_z: float) -> np.ndarray:
    len_x1=int(math.ceil(radius1 / scale_x * 2))
    len_z1=int(math.ceil(radius1 / scale_z * 2))
    arr = np.zeros((len_z1, len_x1), dtype=np.int8)
    for iz in range(len_z1):
        z = (iz - len_z1 / 2) * scale_z
        for ix in range(len_x1):
            x = (ix - len_x1 / 2) * scale_x

            if x * x + z * z <= radius1 * radius1 and x * x + z * z >= radius2 * radius2:
                arr[iz, ix] = 1
            elif  x * x + z * z <= radius2 * radius2 and x * x + z * z >= radius3 * radius3:
                arr[iz, ix] = 2
            elif  x * x + z * z <= radius3 * radius3 and x * x + z * z >= radius4 * radius4:
                arr[iz, ix] = 3
            else:
                arr[iz, ix] = 0
    return arr
grid=double_ring(150e-6, 100e-6, 35e-6, 1 * 1e-6, 1 * 1e-6)
plt.imshow(grid)
plt.show()
np.save("double_ring_150_100_35.npy",grid)
