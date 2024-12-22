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


# Instantiate the in-memory repository
location_repo = InMemoryLocationRepository()

# Instantiate the LocationService with the repository
location_service = LocationService(location_repo)

# Generate and add locations for all network types
locations = location_service.generate_and_add_locations(config)

# Print out the generated locations
for location in locations:
    print(location)

network_elements_repo = InMemoryNetworkElementRepository()
network_element_service = NetworkElementService(
    network_config, location_repo, network_elements_repo
)

# Generate network elements for all configured networks
network_elements = network_element_service.generate_and_add_network_elements()

for ne in network_elements:
    print(ne)
