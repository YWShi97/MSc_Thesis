# This code is used to list all variable names in a Shapefile.

import geopandas as gpd

# Path to the Shapefile
file_path = r'C:\Users\yuwei\Desktop\Database\Basemap\Exclusive Economic Zone\eez.shp'

# Read the Shapefile
data = gpd.read_file(file_path)

# Get the variable names
variable_names = data.columns.tolist()

# Print all variable names
print(variable_names)
print(data.crs)
print(data.columns)