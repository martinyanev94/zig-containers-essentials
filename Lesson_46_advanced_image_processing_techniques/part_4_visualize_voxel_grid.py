import numpy as np
import matplotlib.pyplot as plt

# Create a simple 3D numpy array to represent a voxel grid
voxel_grid = np.zeros((10, 10, 10))
voxel_grid[3:7, 3:7, 3:7] = 1  # Create a cube in the center

# Visualizing the voxel grid using matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Getting the coordinates of the voxels
x, y, z = np.indices(voxel_grid.shape)
ax.voxels(x, y, z, voxel_grid, edgecolor='k')

plt.show()
