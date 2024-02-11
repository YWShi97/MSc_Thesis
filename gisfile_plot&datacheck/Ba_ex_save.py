# This code is used to extract regions with elevation values below -160 meters or above 0 meters from a NetCDF bathymetry dataset
# and save them as separate NetCDF files.

import netCDF4 as nc
import numpy as np
import os

# Open the NetCDF file
nc_file = nc.Dataset(r'C:\Users\yuwei\Desktop\Database\Technical Sector\Bathymetry\gebco_bathymetry.nc', 'r')

# Get the elevation variable data
variable = nc_file.variables['elevation'][:]

# Get longitude and latitude coordinates
lon = nc_file.variables['lon'][:]
lat = nc_file.variables['lat'][:]

# Find the indices of regions where the elevation is lower than -160 or greater than 0
indices = np.where((variable < -160) | (variable > 0))

# Extract longitude, latitude, and variable values for the desired regions
lon_extracted = lon[indices[1]]
lat_extracted = lat[indices[0]]
variable_extracted = variable[indices]

# Create a directory to save the extracted region files
output_dir = r'C:\Users\yuwei\Desktop\Afterprocess\Technical Sector\bathymetry excluded\extracted_regions'
os.makedirs(output_dir, exist_ok=True)

# Save each chunk of extracted regions as separate NetCDF files
chunk_size = 1000  # Define the chunk size based on available memory
num_chunks = len(lon_extracted) // chunk_size + 1

for i in range(num_chunks):
    start_idx = i * chunk_size
    end_idx = (i + 1) * chunk_size

    # Create a new NetCDF file for the chunk
    chunk_file_path = os.path.join(output_dir, f'chunk_{i}.nc')
    chunk_nc_file = nc.Dataset(chunk_file_path, 'w', format='NETCDF4')

    # Create dimensions for latitude, longitude, and extracted regions
    chunk_nc_file.createDimension('lon', lon_extracted[start_idx:end_idx].shape[0])
    chunk_nc_file.createDimension('lat', lat_extracted[start_idx:end_idx].shape[0])

    # Create variables for latitude, longitude, and extracted regions
    new_lon = chunk_nc_file.createVariable('lon', lon.dtype, ('lon',))
    new_lat = chunk_nc_file.createVariable('lat', lat.dtype, ('lat',))
    new_var = chunk_nc_file.createVariable('extracted_region', variable_extracted.dtype, ('lat', 'lon'))

    # Assign values to variables
    new_lon[:] = lon_extracted[start_idx:end_idx]
    new_lat[:] = lat_extracted[start_idx:end_idx]
    new_var[:, :] = variable_extracted[start_idx:end_idx]

    # Close the chunk NetCDF file
    chunk_nc_file.close()

# Close the original NetCDF file
nc_file.close()
