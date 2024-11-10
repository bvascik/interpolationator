import numpy as np
from griddata import griddata_interpolation

class Points:
  def __init__(self, gdf):
    self.gdf = gdf
    self.points = np.array(list(zip(gdf.geometry.x, gdf.geometry.y)))
    self.values = gdf['methane_co'].to_numpy()
    self.min_x, self.max_x = self.points[:, 0].min(), self.points[:, 0].max()
    self.min_y, self.max_y = self.points[:, 1].min(), self.points[:, 1].max()

  def interpolate(self, method, show_plot=False):
    grid_x, grid_y = np.mgrid[self.min_x:self.max_x:100j, self.min_y:self.max_y:100j]
    return griddata_interpolation(self.points, self.values, grid_x, grid_y, method=method, show_plot=show_plot)