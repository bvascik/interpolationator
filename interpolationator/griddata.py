# TODO: write a function that takes a list of points and returns an IDW interpolation

import numpy as np
from scipy.interpolate import griddata
import geopandas as gpd
import matplotlib.pyplot as plt

def griddata_interpolation(points, values, grid_x, grid_y, method='linear', show_plot=False):
    grid_z = griddata(points, values, (grid_x, grid_y), method=method)
    if show_plot:
      plt.imshow(grid_z.T, extent=(grid_x.min(), grid_x.max(), grid_y.min(), grid_y.max()), origin='lower', cmap='viridis')
      plt.colorbar()
      plt.show()

    return grid_z


