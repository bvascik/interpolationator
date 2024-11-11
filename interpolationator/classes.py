import numpy as np
from griddata import griddata_interpolation
from idw import idw_interpolation

class Points:
  def __init__(self, gdf):
    self.gdf = gdf
    self.points = np.array(list(zip(gdf.geometry.x, gdf.geometry.y)))
    self.values = gdf['methane_co'].to_numpy()
    self.min_x, self.max_x = self.points[:, 0].min(), self.points[:, 0].max()
    self.min_y, self.max_y = self.points[:, 1].min(), self.points[:, 1].max()

  def create_grid(self, xy, cell_size=20):
    x_min, x_max = np.min(xy[:, 0]), np.max(xy[:, 0])
    y_min, y_max = np.min(xy[:, 1]), np.max(xy[:, 1])
    grid_x, grid_y = np.mgrid[x_min:x_max:cell_size, y_min:y_max:cell_size]

    return grid_x, grid_y

  def interpolate_griddata(self, method, cellsize, show_plot=False):
    self.grid_x, self.grid_y = self.create_grid(self.points, cellsize)
    return griddata_interpolation(self.points, self.values, self.grid_x, self.grid_y, method=method, show_plot=show_plot)
  
  def interpolate_idw(self, power, cellsize, show_plot=False):
    return idw_interpolation(self.points, self.values, idw_power=power, cell_size=cellsize, show_plot=show_plot)