## Interpolationator

Interpolationator is a tool for performing various types of interpolation on point datasets. It supports various interpolation methods

### Features

- Linear interpolationn
- Nearest-neighbor interpolation
- Cubic interpolation
- IDW interpolation
- Easy-to-use CLI interface
- Memory safe (will kill process is it exceeds 75% memory usage)

### Installation

To install Interpolationator, clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/interpolationator.git
cd interpolationator
pip install -r requirements.txt
```

### Usage

Here's a basic example of how to use Interpolationator:

```bash
python app.py path/to/points.geojson --griddata nearest --cellsize 5 --plot
```

This will produce a griddata 'nearest' plot with cellsize 5 and plot it.

### Upcoming changes

- cli option to save a georeferenced raster with the data
- Kriging interpolation

### License

This project is licensed under the MIT License.