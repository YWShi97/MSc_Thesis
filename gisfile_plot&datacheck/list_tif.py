# This code is used to list all variable values in a GeoTIFF file.

import rasterio

# Path to the GeoTIFF file
file_path = r"C:\Users\yuwei\Desktop\Database\Economic Sector\EMODnet_HA_Vessel_Density_all_2017-2022Avg\EMODnet_Vessel_Density_17-22\vesseldensity_all_2022.tif"

# Get the variable values
with rasterio.open(file_path) as src:

    # Iterate over each variable
    for i in range(src.count):
        # Read the data for the current variable
        data = src.read(i + 1)

        # Print the variable values
        print(f"Variable {i + 1}:\n{data}\n")
