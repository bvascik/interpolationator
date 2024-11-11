import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt

def get_interpolated_values(xy, values, xi, power=2):
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
    
    num_cells_x = int(np.ceil((x_max - x_min) / cell_size))
    num_cells_y = int(np.ceil((y_max - y_min) / cell_size))
    
    grid_x, grid_y = np.meshgrid(
        np.linspace(x_min, x_max, num_cells_x),
        np.linspace(y_min, y_max, num_cells_y)
    )
    grid_points = np.column_stack((grid_x.ravel(), grid_y.ravel()))
    return grid_x, grid_points

def idw_interpolation(xy, values, idw_power=2, cell_size=20, chunk_size=1000, show_plot=False):
    grid_x, grid_points = get_grid_points(xy, cell_size)
    grid_z = np.empty(grid_points.shape[0])

    for i in range(0, grid_points.shape[0], chunk_size):
        chunk = grid_points[i:i + chunk_size]
        grid_z[i:i + chunk_size] = get_interpolated_values(xy, values, chunk, power=idw_power)

    grid_z = grid_z.reshape(grid_x.shape)

    if show_plot:
        x_min, x_max = np.min(xy[:, 0]), np.max(xy[:, 0])
        y_min, y_max = np.min(xy[:, 1]), np.max(xy[:, 1])
        
        plt.imshow(grid_z, extent=(x_min, x_max, y_min, y_max), origin='lower', cmap='viridis')
        plt.colorbar(label='Interpolated value')
        plt.title("IDW Interpolation")
        plt.legend()
        plt.show()

    return grid_z
