# This code is used to plot a NetCDF file @ a time slice based on a target variable defined.

import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# Open the NetCDF dataset
data = xr.open_dataset(r'C:\Users\yuwei\Desktop\Database\Dati Onde\wave2010.nc')

# Print information about the dataset
print(data)

# Access the target variable
target_variable = data['swh']

# Print information about the target variable
print(target_variable)

# Extract the data for a specific time slice
time_index = 85  # For example
time = target_variable['time'][time_index]
latitude = target_variable['latitude']
longitude = target_variable['longitude']
values = target_variable[time_index].values  # Data values @ the specific time slice

# Create a plot
fig = plt.figure(figsize=(10, 10), dpi=600)
ax = plt.axes(projection=ccrs.PlateCarree())

# Contour plot of the data
plt.contourf(longitude, latitude, values, transform=ccrs.PlateCarree())
ax.coastlines()

# Add colorbar
plt.colorbar()

# Set plot title and labels
plt.title('NetCDF Data Plot at {}'.format(time.values))
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Display the plot
plt.show()
