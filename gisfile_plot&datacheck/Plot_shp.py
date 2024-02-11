# This code is used to plot a REDUCED Shapefile and save it as a new Shapefile.

import geopandas as gpd
import matplotlib.pyplot as plt

# Path to the Shapefile
shapefile_path = r'C:\Users\yuwei\Desktop\Database\Coastlines\EMODnet_Bathymetry_2022_coastlines\Europe_2022_satellite_coastline_MSL\EMODnet_satellite_coastline_MSL.shp'

# Read the Shapefile
data = gpd.read_file(shapefile_path)

# Filter the data based on longitude and latitude
filtered_data = data.cx[-19.99791666666667:44.99791666666667, 30.00208333333333:46.99791666666667]

# Re-project the filtered data to a projected CRS
filtered_data = filtered_data.to_crs("EPSG:32633")

# Set the output shapefile path
output_shapefile_path = r'C:\Users\yuwei\Desktop\Filtered_Coastlines.shp'

# Save the filtered data as a new shapefile
filtered_data.to_file(output_shapefile_path)

# Create a plot
fig, ax = plt.subplots(figsize=(10, 10))
filtered_data.plot(ax=ax, color='black')
ax.set_aspect('equal')

# Display the plot
plt.show()
