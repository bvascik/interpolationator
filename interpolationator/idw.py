import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt

# TODO: add custom grid_point sizing


def get_interpolated_values(xy, values, xi, power=2):
    """
    Perform IDW interpolation.

    Parameters:
    xy : ndarray of shape (n, 2)
        Known data point coordinates.
    values : ndarray of shape (n,)
        Values at the known data points.
    xi : ndarray of shape (m, 2)
        Interpolation points.
    power : int
        Power parameter of the IDW formula.

    Returns:
    interpolated_values : ndarray of shape (m,)
        Interpolated values at points xi.
    """
    dist = distance.cdist(xi, xy, 'euclidean')
    
    with np.errstate(divide='ignore'):
        weights = 1 / dist**power
    
    weights[dist == 0] = np.inf  # Infinite weight for coinciding points
    weights_sum = np.sum(weights, axis=1)
    
    interpolated_values = np.sum(weights * values, axis=1) / weights_sum
    interpolated_values[weights_sum == 0] = np.nan  # Avoid NaNs for coinciding points

    return interpolated_values

def get_grid_points(xy, cell_size):
    x_min, x_max = np.min(xy[:, 0]), np.max(xy[:, 0])
    y_min, y_max = np.min(xy[:, 1]), np.max(xy[:, 1])
    
    # Calculate the number of cells based on the cell size
    num_cells_x = int(np.ceil((x_max - x_min) / cell_size))
    num_cells_y = int(np.ceil((y_max - y_min) / cell_size))
    
    grid_x, grid_y = np.meshgrid(
        np.linspace(x_min, x_max, num_cells_x),
        np.linspace(y_min, y_max, num_cells_y)
    )
    grid_points = np.column_stack((grid_x.ravel(), grid_y.ravel()))
    return grid_x, grid_points

def idw_interpolation(xy, values, idw_power=2, cell_size=20, show_plot=False):
  grid_x, grid_points = get_grid_points(xy, cell_size)
  grid_z = get_interpolated_values(xy, values, grid_points, power=idw_power)

  # Reshape interpolated values to match the grid
  grid_z = grid_z.reshape(grid_x.shape)

  if show_plot:
    # Determine the extent of the plot based on the input data
    x_min, x_max = np.min(xy[:, 0]), np.max(xy[:, 0])
    y_min, y_max = np.min(xy[:, 1]), np.max(xy[:, 1])
    
    # Plot the interpolated result as an image
    plt.imshow(grid_z, extent=(x_min, x_max, y_min, y_max), origin='lower', cmap='viridis')
    plt.colorbar(label='Interpolated value')
    plt.title("IDW Interpolation")
    plt.legend()
    plt.show()

  return grid_z
