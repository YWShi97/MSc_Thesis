# This code is used to check the latitude and longitude resolutions of a NetCDF file,
# along with their corresponding resolutions in km.

import netCDF4 as nc
from math import radians, cos, sin, sqrt, atan2

def calculate_distance(lat1, lon1, lat2, lon2):
    # Approximate radius of Earth in km
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    # Haversine formula to calculate distance between two points on a sphere
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return distance

def print_nc_resolution(file_path):
    try:
        # Open the NetCDF file
        dataset = nc.Dataset(file_path)

        # Check if the 'latitude' and 'longitude' variables exist
        if 'latitude' in dataset.variables and 'longitude' in dataset.variables:
            lat_res = abs(dataset.variables['latitude'][1] - dataset.variables['latitude'][0])
            lon_res = abs(dataset.variables['longitude'][1] - dataset.variables['longitude'][0])

            # Calculate the resolution in kilometers
            lat1, lon1 = dataset.variables['latitude'][0], dataset.variables['longitude'][0]
            lat2, lon2 = lat1 + lat_res, lon1 + lon_res
            resolution_km = calculate_distance(lat1, lon1, lat2, lon2)

            print(f"Latitude resolution: {lat_res} degrees")
            print(f"Longitude resolution: {lon_res} degrees")
            print(f"Resolution in kilometers: {resolution_km:.2f} km")
        else:
            print("Error: The 'latitude' and 'longitude' variables are not present in the NetCDF file.")

        dataset.close()

    except Exception as e:
        print(f"Error occurred: {str(e)}")


# Path to the NetCDF dataset
nc_file_path = r'C:\Users\yuwei\Desktop\Database\Dati Onde\wave2010.nc'

# Print the resolutions
print_nc_resolution(nc_file_path)
