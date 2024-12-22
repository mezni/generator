import logging
from persistance import (
    TinyDBLocationRepository,
    TinyDBNetworkElementRepository,
    InMemoryLocationRepository,
)
from services import LocationLoaderService, NetworkElementLoaderService, LocationService

# Configuration for locations and network elements
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

db_path = "config.json"
# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Repositories (change to InMemory for testing)
location_tinydb_repo = TinyDBLocationRepository(db_path)
network_elements_tinydb_repo = TinyDBNetworkElementRepository(db_path)

# Services
location_loader_service = LocationLoaderService(location_tinydb_repo)
network_element_service = NetworkElementLoaderService(
    network_config, location_tinydb_repo, network_elements_tinydb_repo
)


locations = location_loader_service.generate_and_add_locations(config)


location_repo = InMemoryLocationRepository()
location_service = LocationService(location_repo)
location_service.load_locations(locations)
