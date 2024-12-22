import random
from typing import List
from entities import Location, NetworkElement


class NetworkElementFactory:
    def __init__(self):
        self.network_element_types = {
            "2G": ["BSC", "BTS", "MSC", "SMSC", "HLR"],
            "3G": ["SGSN", "GGSN", "MSC", "HSS", "RNC", "NodeBs"],
            "4G": ["MME", "SGW", "PGW", "HSS", "eNodeBs", "PCRF"],
            "5G": ["AMF", "SMF", "UPF", "NSSF", "PCF", "UDM", "gNodeB", "CU", "DU"],
        }

    def generate_ip(self):
        return f"192.168.{random.randint(0, 255)}.{random.randint(1, 254)}"

    def generate_cell_info(self, network_type, location_id):
        """Generate cell-specific information based on the network type and location_id."""
        if network_type in ["2G", "3G"]:
            lac = location_id  # lac for 2G/3G
            return None, lac, None
        elif network_type in ["4G", "5G"]:
            tac = location_id  # tac for 4G/5G
            return None, None, tac
        return None, None, None

    def assign_function(self, element_type, network_type):
        """Assigns network functions based on element type and network type."""
        functions = {
            "2G": [
                {
                    "element_type": "BSC",
                    "name": "BSC Function",
                    "description": "Controls BTS, radio resource management.",
                },
                {
                    "element_type": "BTS",
                    "name": "BTS Function",
                    "description": "Handles radio communication with mobile devices.",
                },
                {
                    "element_type": "MSC",
                    "name": "MSC Function",
                    "description": "Manages voice call routing and switching.",
                },
                {
                    "element_type": "SMSC",
                    "name": "SMSC Function",
                    "description": "Handles SMS messaging gateway.",
                },
                {
                    "element_type": "HLR",
                    "name": "HLR Function",
                    "description": "Database for subscriber information.",
                },
            ],
            "3G": [
                {
                    "element_type": "SGSN",
                    "name": "SGSN Function",
                    "description": "Handles mobile packet switched data.",
                },
                {
                    "element_type": "GGSN",
                    "name": "GGSN Function",
                    "description": "Gateway for packet-switched data.",
                },
                {
                    "element_type": "MSC",
                    "name": "MSC Function",
                    "description": "Voice call routing and switching.",
                },
                {
                    "element_type": "HSS",
                    "name": "HSS Function",
                    "description": "Manages user profiles and authentication.",
                },
                {
                    "element_type": "RNC",
                    "name": "RNC Function",
                    "description": "Manages NodeBs in the network.",
                },
                {
                    "element_type": "NodeBs",
                    "name": "NodeBs Function",
                    "description": "3G base stations, similar to BTS.",
                },
            ],
            "4G": [
                {
                    "element_type": "MME",
                    "name": "MME Function",
                    "description": "Mobility management in LTE networks.",
                },
                {
                    "element_type": "SGW",
                    "name": "SGW Function",
                    "description": "Gateway for radio access to core network.",
                },
                {
                    "element_type": "PGW",
                    "name": "PGW Function",
                    "description": "Packet gateway for external networks.",
                },
                {
                    "element_type": "HSS",
                    "name": "HSS Function",
                    "description": "Manages user profiles and authentication.",
                },
                {
                    "element_type": "eNodeBs",
                    "name": "eNodeBs Function",
                    "description": "4G base stations.",
                },
                {
                    "element_type": "PCRF",
                    "name": "PCRF Function",
                    "description": "Policy control and charging rules.",
                },
            ],
            "5G": [
                {
                    "element_type": "AMF",
                    "name": "AMF Function",
                    "description": "Handles UE registration and mobility.",
                },
                {
                    "element_type": "SMF",
                    "name": "SMF Function",
                    "description": "Manages session establishment.",
                },
                {
                    "element_type": "UPF",
                    "name": "UPF Function",
                    "description": "Routes user data and provides bearer control.",
                },
                {
                    "element_type": "NSSF",
                    "name": "NSSF Function",
                    "description": "Determines network slice for services.",
                },
                {
                    "element_type": "PCF",
                    "name": "PCF Function",
                    "description": "Policy management for user traffic.",
                },
                {
                    "element_type": "UDM",
                    "name": "UDM Function",
                    "description": "Manages subscriber data.",
                },
                {
                    "element_type": "gNodeB",
                    "name": "gNodeB Function",
                    "description": "5G base station.",
                },
                {
                    "element_type": "CU",
                    "name": "CU Function",
                    "description": "Handles control in 5G RAN.",
                },
                {
                    "element_type": "DU",
                    "name": "DU Function",
                    "description": "Handles lower layers in 5G RAN.",
                },
            ],
        }

        return [
            func
            for func in functions.get(network_type, [])
            if func["element_type"] == element_type
        ]

    def create_network_element(self, network_type, element_type, location_id):
        """Create a single network element."""
        cell_id, lac, tac = self.generate_cell_info(network_type, location_id)

        element_info = {
            "element_id": random.randint(1000, 9999),
            "element_name": f"{network_type}_{element_type}_{random.randint(1000, 9999)}",
            "network_type": network_type,
            "ip_address": self.generate_ip(),
            "location_id": location_id,
            "status": random.choice(["Active", "Inactive"]),
            "function": self.assign_function(element_type, network_type),
        }

        # Include cell_id, lac, or tac based on network type
        if cell_id and lac:
            element_info.update({"cell_id": cell_id, "lac": lac})
        elif tac:
            element_info.update({"tac": tac})

        return NetworkElement(**element_info)

    def create_network_elements(
        self, network_type, element_type, location_ids, num_elements=1
    ):
        """Creates multiple network elements based on network type, element type, and location."""
        elements = []
        location_ids = [
            location_ids[i % len(location_ids)] for i in range(num_elements)
        ]

        for location_id in location_ids:
            network_element = self.create_network_element(
                network_type, element_type, location_id
            )
            elements.append(network_element)

        return elements


class LocationFactory:
    def __init__(self):
        pass

    def create_location(
        self,
        location_id,
        location_name,
        network_type,
        lat_min,
        lat_max,
        lon_min,
        lon_max,
    ) -> Location:
        """Create a single Location object."""
        return Location(
            location_id=location_id,
            location_name=location_name,
            network_type=network_type,
            lat_min=lat_min,
            lat_max=lat_max,
            lon_min=lon_min,
            lon_max=lon_max,
        )

    def create_locations(self, config: dict) -> List[Location]:
        """Generates a list of locations based on the configuration."""
        locations = []  # Will store all the generated locations

        # Iterate over each network type in the config
        for network_type in config["network_configs"]:
            network_config = config["network_configs"].get(network_type)

            if not network_config:
                raise ValueError(f"Invalid network type: {network_type}")

            rows = network_config["rows"]
            cols = network_config["cols"]
            location_names = network_config["region_names"]

            if len(location_names) != rows * cols:
                raise ValueError(
                    f"The number of region names must match {rows * cols} for a {rows}x{cols} matrix."
                )

            min_lat, max_lat = config["Latitude"]
            min_lon, max_lon = config["Longitude"]

            lat_step = (max_lat - min_lat) / rows
            lon_step = (max_lon - min_lon) / cols

            location_id_base = {"2G": 2000, "3G": 3000, "4G": 4000, "5G": 5000}

            if network_type not in location_id_base:
                raise ValueError(f"Unsupported network type: {network_type}")

            location_id = location_id_base[network_type]
            region_counter = 0

            for i in range(rows):
                for j in range(cols):
                    location_name = location_names[region_counter]
                    region_counter += 1

                    lat_min = min_lat + i * lat_step
                    lat_max = min_lat + (i + 1) * lat_step
                    lon_min = min_lon + j * lon_step
                    lon_max = min_lon + (j + 1) * lon_step

                    lat_min = round(lat_min, 2)
                    lat_max = round(lat_max, 2)
                    lon_min = round(lon_min, 2)
                    lon_max = round(lon_max, 2)

                    location = self.create_location(
                        location_id,
                        location_name,
                        network_type,
                        lat_min,
                        lat_max,
                        lon_min,
                        lon_max,
                    )
                    locations.append(location)

                    location_id += 1  # Increment the location ID

        return locations
