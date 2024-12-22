# service.py
import random
from typing import List
from entities import Location, NetworkElement
from interfaces import LocationRepositoryInterface, NetworkElementRepositoryInterface


class LocationService:
    def __init__(self, repository: LocationRepositoryInterface):
        self.repository = repository  # Dependency injection of repository

    def generate_and_add_locations(
        self, config: dict, network_type: str
    ) -> List[Location]:
        """Generates locations based on the configuration and adds them to the repository."""

        # Get the network-specific configuration from the config dictionary
        network_config = config["network_configs"].get(network_type)

        if not network_config:
            raise ValueError(f"Invalid network type: {network_type}")

        rows = network_config["rows"]
        cols = network_config["cols"]
        region_names = network_config["region_names"]

        if len(region_names) != rows * cols:
            raise ValueError(
                f"The number of region names must match {rows * cols} for a {rows}x{cols} matrix."
            )

        min_lat, max_lat = config["Latitude"]
        min_lon, max_lon = config["Longitude"]

        # Calculate step for both latitude and longitude
        lat_step = (max_lat - min_lat) / rows
        lon_step = (max_lon - min_lon) / cols

        locations = []

        # Set starting location_id based on network_type
        if network_type == "2G":
            location_id = 2000
        elif network_type == "3G":
            location_id = 3000
        elif network_type == "4G":
            location_id = 4000
        elif network_type == "5G":
            location_id = 5000
        else:
            raise ValueError(f"Unsupported network type: {network_type}")

        region_counter = 0

        for i in range(rows):
            for j in range(cols):
                region_name = region_names[region_counter]
                region_counter += 1

                lat_min = min_lat + i * lat_step
                lat_max = min_lat + (i + 1) * lat_step
                lon_min = min_lon + j * lon_step
                lon_max = min_lon + (j + 1) * lon_step

                # Ensure only two decimal places for latitudes and longitudes
                lat_min = round(lat_min, 2)
                lat_max = round(lat_max, 2)
                lon_min = round(lon_min, 2)
                lon_max = round(lon_max, 2)

                # Generate Location entity
                location = Location(
                    location_id,
                    region_name,
                    network_type,
                    lat_min,
                    lat_max,
                    lon_min,
                    lon_max,
                )
                self.repository.add(location)
                locations.append(location)

                location_id += 1  # Increment the location ID

        return locations


class NetworkElementService:
    def __init__(self, network_config, repository: NetworkElementRepositoryInterface):
        self.repository = repository
        self.network_element_types = {
            "2G": ["BSC", "BTS", "MSC", "SMSC", "HLR"],
            "3G": ["SGSN", "GGSN", "MSC", "HSS", "RNC", "NodeBs"],
            "4G": ["MME", "SGW", "PGW", "HSS", "eNodeBs", "PCRF"],
            "5G": ["AMF", "SMF", "UPF", "NSSF", "PCF", "UDM", "gNodeB", "CU", "DU"],
        }

        # Use the passed network config dictionary for element counts
        self.element_count = network_config

    def generate_ip(self):
        return ".".join(str(random.randint(0, 255)) for _ in range(4))

    def generate_cell_info(self, network_type, element_type):
        if network_type in ["2G", "3G"] and "BTS" in element_type:
            cell_id = random.randint(1, 9999)  # Generate a random cell_id
            lac = random.randint(
                1, 255
            )  # Generate a random lac, typically between 1 and 255
            return cell_id, lac, None  # Return cell_id and lac for 2G and 3G
        elif network_type in ["4G", "5G"] and (
            "eNodeBs" in element_type or "gNodeB" in element_type
        ):
            tac = random.randint(1, 255)  # Generate a random TAC for 4G and 5G
            return None, None, tac  # Return TAC for 4G and 5G
        return None, None, None  # No values for other network types

    def assign_function(self, element_type, network_type):
        function_list = []

        # Define functions for different network types
        if network_type == "2G":
            functions_2g = [
                {
                    "element_type": "BSC",
                    "name": "BSC Function",
                    "description": "Control and manage base stations (BTS), Radio resource management",
                },
                {
                    "element_type": "BTS",
                    "name": "BTS Function",
                    "description": "Connects to mobile devices, handles radio communication",
                },
                {
                    "element_type": "MSC",
                    "name": "MSC Function",
                    "description": "Manages voice call routing and switching",
                },
                {
                    "element_type": "SMSC",
                    "name": "SMSC Function",
                    "description": "SMS messaging gateway",
                },
                {
                    "element_type": "HLR",
                    "name": "HLR Function",
                    "description": "Database for subscriber information",
                },
            ]
            for func in functions_2g:
                if element_type == func["element_type"]:
                    function_list.append(func)

        elif network_type == "3G":
            functions_3g = [
                {
                    "element_type": "SGSN",
                    "name": "SGSN Function",
                    "description": "Manages mobile packet switched data for 3G networks",
                },
                {
                    "element_type": "GGSN",
                    "name": "GGSN Function",
                    "description": "Gateway for packet-switched data between the mobile network and external networks",
                },
                {
                    "element_type": "MSC",
                    "name": "MSC Function",
                    "description": "Manages voice call routing and switching",
                },
                {
                    "element_type": "HSS",
                    "name": "HSS Function",
                    "description": "Home Subscriber Server, manages user profiles and authentication",
                },
                {
                    "element_type": "RNC",
                    "name": "RNC Function",
                    "description": "Radio Network Controller for managing NodeBs",
                },
                {
                    "element_type": "NodeBs",
                    "name": "NodeBs Function",
                    "description": "Base stations in 3G networks, similar to BTS",
                },
            ]
            for func in functions_3g:
                if element_type == func["element_type"]:
                    function_list.append(func)

        elif network_type == "4G":
            functions_4g = [
                {
                    "element_type": "MME",
                    "name": "MME Function",
                    "description": "Manages mobility and session for 4G LTE networks",
                },
                {
                    "element_type": "SGW",
                    "name": "SGW Function",
                    "description": "Serves as a gateway between the radio access network and core network",
                },
                {
                    "element_type": "PGW",
                    "name": "PGW Function",
                    "description": "Gateway for user data between the LTE network and external networks",
                },
                {
                    "element_type": "HSS",
                    "name": "HSS Function",
                    "description": "Home Subscriber Server, manages user profiles and authentication",
                },
                {
                    "element_type": "eNodeBs",
                    "name": "eNodeBs Function",
                    "description": "Evolved NodeBs, the 4G base stations",
                },
                {
                    "element_type": "PCRF",
                    "name": "PCRF Function",
                    "description": "Policy Control and Charging Rules Function",
                },
            ]
            for func in functions_4g:
                if element_type == func["element_type"]:
                    function_list.append(func)

        elif network_type == "5G":
            functions_5g = [
                {
                    "element_type": "AMF",
                    "name": "AMF Function",
                    "description": "Handles registration, connection, and mobility management for user equipment (UE)",
                },
                {
                    "element_type": "SMF",
                    "name": "SMF Function",
                    "description": "Manages session establishment, modification, and release",
                },
                {
                    "element_type": "UPF",
                    "name": "UPF Function",
                    "description": "Routes user data to/from the mobile network, provides bearer control",
                },
                {
                    "element_type": "NSSF",
                    "name": "NSSF Function",
                    "description": "Determines the network slice to be used for a given service or UE",
                },
                {
                    "element_type": "PCF",
                    "name": "PCF Function",
                    "description": "Defines and manages policy rules for user traffic, including QoS",
                },
                {
                    "element_type": "UDM",
                    "name": "UDM Function",
                    "description": "Manages subscriber data and handles authentication, authorization, and accounting",
                },
                {
                    "element_type": "gNodeB",
                    "name": "gNodeB Function",
                    "description": "Next generation base station for 5G wireless communication",
                },
                {
                    "element_type": "CU",
                    "name": "CU Function",
                    "description": "Handles control functions in 5G RAN",
                },
                {
                    "element_type": "DU",
                    "name": "DU Function",
                    "description": "Handles lower layers of the protocol stack in 5G RAN",
                },
            ]
            for func in functions_5g:
                if element_type == func["element_type"]:
                    function_list.append(func)

        return function_list

    def generate_element_info(self, network_type, element_type):
        cell_id, lac, tac = self.generate_cell_info(network_type, element_type)

        element_info = {
            "element_id": random.randint(1000, 9999),
            "element_name": f"{network_type}_{element_type}_{random.randint(1000, 9999)}",
            "network_type": network_type,
            "ip_address": self.generate_ip(),
            #            "location_id": f"Datacenter {random.choice(['A', 'B', 'C'])}",
            "location_id": 1,
            "status": random.choice(["Active", "Inactive"]),
            "function": self.assign_function(element_type, network_type),
        }

        if cell_id is not None and lac is not None:
            element_info["cell_id"] = cell_id
            element_info["lac"] = lac
        if tac is not None:
            element_info["tac"] = tac

        return element_info

    def generate_elements(self, network_type, element_type, num_elements=5):
        elements = []
        for _ in range(num_elements):
            element_info = self.generate_element_info(network_type, element_type)
            elements.append(element_info)
        return elements

    def generate_network_elements(self, network_type):
        network_elements = {}

        # Get the number of elements from the config dictionary
        for element_type in self.network_element_types.get(network_type, []):
            num_elements = self.element_count.get(network_type, {}).get(
                element_type, 1
            )  # Default to 1 if not found
            generated_elements = self.generate_elements(
                network_type, element_type, num_elements
            )

            # Add each generated element to the repository
            for element_info in generated_elements:
                print(element_info)
                # Assuming you have a NetworkElement class that takes element_info as arguments
                network_element = NetworkElement(
                    **element_info
                )  # Create the network element instance
                self.repository.add(network_element)  # Add it to the repository

            network_elements[element_type] = generated_elements

        return network_elements