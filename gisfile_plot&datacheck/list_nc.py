# This code is used to list all variable names in a NetCDF file.

import netCDF4 as nc

# Open the NetCDF file
nc_file = nc.Dataset(r'C:\Users\yuwei\Desktop\Database\Dati Onde\wave2010.nc', 'r')

# Print all variable names
print(nc_file.variables.keys())

# Close the NetCDF file
nc_file.close()
