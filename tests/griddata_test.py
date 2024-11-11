import numpy as np
import pytest
from interpolationator.griddata import griddata_interpolation

def test_griddata_interpolation_linear():
  xy = np.array([[0, 0], [1, 1], [1, 0], [0, 1]])
  values = np.array([0, 1, 1, 0])
  grid_x, grid_y = np.mgrid[0:1:100j, 0:1:100j]
  result = griddata_interpolation(xy, values, grid_x, grid_y, method='linear')
  assert result.shape == (100, 100)
  assert np.isfinite(result).all()

def test_griddata_interpolation_nearest():
  xy = np.array([[0, 0], [1, 1], [1, 0], [0, 1]])
  values = np.array([0, 1, 1, 0])
  grid_x, grid_y = np.mgrid[0:1:100j, 0:1:100j]
  result = griddata_interpolation(xy, values, grid_x, grid_y, method='nearest')
  assert result.shape == (100, 100)
  assert np.isfinite(result).all()

def test_griddata_interpolation_cubic():
  xy = np.array([[0, 0], [1, 1], [1, 0], [0, 1]])
  values = np.array([0, 1, 1, 0])
  grid_x, grid_y = np.mgrid[0:1:100j, 0:1:100j]
  result = griddata_interpolation(xy, values, grid_x, grid_y, method='cubic')
  assert result.shape == (100, 100)
  assert np.isfinite(result).all()

if __name__ == "__main__":
  pytest.main()