# TODO: write a function that takes a list of points and returns an IDW interpolation

import numpy as np
from scipy.interpolate import griddata
import geopandas as gpd
import matplotlib.pyplot as plt

def griddata_interpolation(xy, values, cell_size, method='linear', show_plot=False):
    x_min, x_max = np.min(xy[:, 0]), np.max(xy[:, 0])
    y_min, y_max = np.min(xy[:, 1]), np.max(xy[:, 1])
    grid_x, grid_y = np.mgrid[x_min:x_max:cell_size, y_min:y_max:cell_size]
    
    grid_z = griddata(xy, values, (grid_x, grid_y), method=method)
    
    if show_plot:
      plt.imshow(grid_z.T, extent=(grid_x.min(), grid_x.max(), grid_y.min(), grid_y.max()), origin='lower', cmap='viridis')
      plt.colorbar()
      plt.show()

    return grid_z


