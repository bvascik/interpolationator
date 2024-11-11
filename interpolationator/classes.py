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
  
  def get_grid_points(self, xy, cell_size=20):
    x_min, x_max = np.min(xy[:, 0]), np.max(xy[:, 0])
    y_min, y_max = np.min(xy[:, 1]), np.max(xy[:, 1])
    
    num_cells_x = int(np.ceil((x_max - x_min) / cell_size))
    num_cells_y = int(np.ceil((y_max - y_min) / cell_size))
    
    grid_x, grid_y = np.meshgrid(
        np.linspace(x_min, x_max, num_cells_x),
        np.linspace(y_min, y_max, num_cells_y)
    )
    grid_points = np.column_stack((grid_x.ravel(), grid_y.ravel()))
    return grid_x, grid_points

  def interpolate_griddata(self, method, cellsize, show_plot=False):
    if cellsize is None:
      cellsize = 20
    self.grid_x, self.grid_y = self.create_grid(self.points, cellsize)
    return griddata_interpolation(self.points, self.values, self.grid_x, self.grid_y, method=method, show_plot=show_plot)
  
  def interpolate_idw(self, power, cellsize, show_plot=False):
    if cellsize is None:
      cellsize = 20
    self.grid_x, self.grid_points = self.get_grid_points(self.points, cellsize)
    return idw_interpolation(self.points, self.values, self.grid_x, self.grid_points, idw_power=power, show_plot=show_plot)