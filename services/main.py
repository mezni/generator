# main.py
from persistance import InmemLocationRepository
from services import LocationService

# Configuration for Tunisia including network-specific configurations
config = {
    "Country": "Tunisia",
    "Latitude": [30.24, 37.54],
    "Longitude": [7.52, 11.60],
    "network_configs": {
        "2G": {"rows": 3, "cols": 1, "region_names": ["North", "Mid", "South"]},
        "3G": {
            "rows": 4,
            "cols": 1,
            "region_names": ["North", "Central", "South", "West"],
        },
        "4G": {"rows": 3, "cols": 1, "region_names": ["Nord", "Mid", "Sud"]},
        "5G": {
            "rows": 4,
            "cols": 1,
            "region_names": ["North", "East", "West", "South"],
        },
    },
}

# Instantiate the in-memory repository
repo = InmemLocationRepository()

# Instantiate the LocationService with the repository
location_service = LocationService(repo)

# Generate and add locations for 2G network
locations_2g = location_service.generate_and_add_locations(config, "2G")

# Print out the generated locations for 2G network
print("Generated locations for 2G network:")
for location in locations_2g:
    print(location)

# Generate and add locations for 4G network
locations_4g = location_service.generate_and_add_locations(config, "4G")

# Print out the generated locations for 4G network
print("Generated locations for 4G network:")
for location in locations_4g:
    print(location)
