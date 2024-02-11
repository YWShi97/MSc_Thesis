# This code is to build a Buffered region for Active licences Area for Oil & Gas Exploitation and Exploration.
# The Buffer Distance is set as 500 meters.

import geopandas as gpd
import matplotlib.pyplot as plt
import os

# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Set the input folder name
input_folder_name = "raw_OilandGasEE_shp"

# Create the input folder path
input_folder_path = os.path.join(script_directory, input_folder_name)

# Set the shapefile path within the input folder
shapefile_path = os.path.join(input_folder_path, "activelicensesPolygon.shp")
data = gpd.read_file(shapefile_path)

# Set the buffer distance @500 meters
buffer_distance = 500

# Re-project the .shp file to a projected CRS
data = data.to_crs("EPSG:32610")

# Create a buffer region by buffer function
buffered_data = data.buffer(buffer_distance)


# Set the output folder name
output_folder_name = "buffer_OilandGasEE_shp"

# Create the output folder path
output_folder_path = os.path.join(script_directory, output_folder_name)

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Set the output shapefile path within the output folder
output_shapefile_path = os.path.join(output_folder_path, "buffered_data.shp")

# Save the buffered data as a new shapefile
buffered_data.to_file(output_shapefile_path)


# Create a plot to show the buffered region
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the original region
# data.plot(ax=ax, color='blue')

# Plot the buffered region
buffered_data.plot(ax=ax, color='red')

# Set plot title and labels
ax.set_title("Buffered @500m")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Display the plot
plt.show()
