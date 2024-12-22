# main.py
from persistance import InMemoryLocationRepository, InMemoryNetworkElementRepository
from services import LocationService, NetworkElementService

# Configuration for Tunisia including network-specific configurations
config = {
    "Country": "Tunisia",
    "Latitude": [30.24, 37.54],
    "Longitude": [7.52, 11.60],
    "network_configs": {
        "2G": {"rows": 3, "cols": 1, "region_names": ["Nord", "Centre", "Sud"]},
        "3G": {"rows": 3, "cols": 1, "region_names": ["Nord", "Centre", "Sud"]},
        "4G": {
            "rows": 3,
            "cols": 2,
            "region_names": [
                "Nord-Est",
                "Nord-West",
                "Centre-Est",
                "Centre-West",
                "Sud-Est",
                "Sud-West",
            ],
        },
        "5G": {
            "rows": 3,
            "cols": 2,
            "region_names": [
                "Nord-Est",
                "Nord-West",
                "Centre-Est",
                "Centre-West",
                "Sud-Est",
                "Sud-West",
            ],
        },
    },
}


network_config = {
    "2G": {"BSC": 20, "BTS": 20, "MSC": 1, "SMSC": 1, "HLR": 1},
    "3G": {"SGSN": 1, "GGSN": 1, "MSC": 1, "HSS": 1, "RNC": 1, "NodeBs": 20},
    "4G": {"MME": 1, "SGW": 1, "PGW": 1, "HSS": 1, "eNodeBs": 20, "PCRF": 1},
    "5G": {
        "AMF": 1,
        "SMF": 1,
        "UPF": 1,
        "NSSF": 1,
        "PCF": 1,
        "UDM": 1,
        "gNodeB": 20,
        "CU": 1,
        "DU": 1,
    },
}

network_repo = InMemoryNetworkElementRepository()
service = NetworkElementService(network_config, network_repo)
network_elements = service.generate_network_elements("4G")
print(network_elements)


# Instantiate the in-memory repository
repo = InMemoryLocationRepository()

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
