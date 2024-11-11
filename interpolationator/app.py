import argparse
import geopandas as gpd
import time

from classes import Points
import psutil
import os
import signal
import threading
# TODO: Add georeference image saving
# TODO: Add testing

def main():
  parser = argparse.ArgumentParser(description='Interpolate data from a GeoJSON file')
  parser.add_argument('--points', type=str, required=True, help='The file path to the GeoJSON file containing the points to interpolate')
  parser.add_argument('--griddata', type=str, required=False, help='The method to use for griddata interpolation: [nearest, linear, or cubic]')
  parser.add_argument('--idw', type=int, required=False, help='The power parameter for IDW interpolation')
  parser.add_argument('--cellsize', type=int, required=False, help='The size of the grid cells for IDW interpolation')
  parser.add_argument('--plot', action='store_true', required=False, help='Show the plot of the interpolated data')

  args = parser.parse_args()

  print(args)

  try:
    gdf_points = gpd.read_file(args.points)
  except FileNotFoundError:
    print(f"Error: The file {args.points} does not exist.")
    return
  
  points = Points(gdf_points)
  
  start_time = time.time()
  
  if args.griddata:
    if args.plot:
      points.interpolate_griddata(method=args.griddata, show_plot=True)
    else:
      points.interpolate_griddata(method=args.griddata)
  elif args.idw:
    if args.plot:
      points.interpolate_idw(power=args.idw, cellsize=args.cellsize, show_plot=True)
    else:
      points.interpolate_idw(power=args.idw, cellsize=args.cellsize)
  
  end_time = time.time()
  elapsed_time = end_time - start_time
  print(f"Interpolation completed in {elapsed_time:.2f} seconds")

def monitor_memory(threshold=75):
  while True:
    memory = psutil.virtual_memory()
    if memory.percent > threshold:
      print(f"Memory usage exceeded {threshold}%. Terminating process.")
      os.kill(os.getpid(), signal.SIGTERM)
    time.sleep(1)

if __name__ == '__main__':
  monitor_thread = threading.Thread(target=monitor_memory)
  monitor_thread.daemon = True
  monitor_thread.start()
  main()