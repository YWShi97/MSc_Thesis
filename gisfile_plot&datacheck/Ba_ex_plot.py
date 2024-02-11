# This code is used to visualize regions with elevation values below -160 meters or above 0 meters from a NetCDF bathymetry dataset.

import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# Open the NetCDF file
nc_file = nc.Dataset(r'C:\Users\yuwei\Desktop\Database\Technical Sector\Bathymetry\gebco_bathymetry.nc', 'r')

# Get the elevation variable data
variable = nc_file.variables['elevation'][:]

# Get longitude and latitude coordinates
lon = nc_file.variables['lon'][:]
lat = nc_file.variables['lat'][:]

# Find the indices of regions where the elevation is lower than -160 or greater than or equal to 0
indices = np.where((variable < -160) | (variable >= 0))

# Extract longitude, latitude, and variable values for the desired regions
lon_extracted = lon[indices[1]]
lat_extracted = lat[indices[0]]
variable_extracted = variable[indices]

# Close file
nc_file.close()

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

# Plot the extracted regions
sc = ax.scatter(lon_extracted, lat_extracted, c=variable_extracted, cmap='jet', s=10, transform=ccrs.PlateCarree())

# Add colorbar
cbar = plt.colorbar(sc, label='Elevation')

# Set axis labels
ax.set_title('Regions with Elevation < -160 or Elevation > 0')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# Set the plot extent
ax.set_extent([lon.min(), lon.max(), lat.min(), lat.max()], crs=ccrs.PlateCarree())

# Plot
plt.show()
