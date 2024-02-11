# This code is used to plot a GeoTIFF file.

import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt

# Path to the GeoTIFF file
file_path = r"C:\Users\yuwei\Desktop\Database\Economic Sector\EMODnet_HA_Vessel_Density_all_2017-2022Avg\EMODnet_Vessel_Density_17-22\vesseldensity_all_2022.tif"

# Get the values
with rasterio.open(file_path) as src:

    # Read the raster data
    array = src.read(1)

    # Create a plot
    fig, ax = plt.subplots(figsize=(10, 10))

    # Plot the data @ original resolution
    show(array, ax=ax, transform=src.transform)

    # Display the plot
    plt.show()
