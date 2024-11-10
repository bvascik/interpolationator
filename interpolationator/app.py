import argparse
import geopandas as gpd

from classes import Points

def main():
  parser = argparse.ArgumentParser(description='Interpolate data from a GeoJSON file')
  parser.add_argument('--points', type=str, required=True, help='The file path to the GeoJSON file containing the points to interpolate')
  parser.add_argument('--griddata', type=str, required=False, help='The method to use for griddata interpolation: [nearest, linear, or cubic]')
  parser.add_argument('--plot', action='store_true', required=False, help='Show the plot of the interpolated data')

  args = parser.parse_args()

  print(args)

  try:
    gdf_points = gpd.read_file(args.points)
  except FileNotFoundError:
    print(f"Error: The file {args.points} does not exist.")
    return
  
  points = Points(gdf_points)
  if args.griddata:
    if args.plot:
      points.interpolate(method=args.griddata, show_plot=True)
    else:
      points.interpolate(method=args.griddata)

if __name__ == '__main__':
  main()
