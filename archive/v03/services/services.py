import random
from typing import List
from entities import Location, NetworkElement
from interfaces import LocationRepositoryInterface, NetworkElementRepositoryInterface


def calculate_grid_steps(config: dict) -> dict:
    """Calculate grid steps for each network type."""
    min_lat, max_lat = config["Latitude"]
    min_lon, max_lon = config["Longitude"]
    
    # Calculate latitude and longitude steps for each network type
    grid_steps = {}
    for network_type, network_config in config["network_configs"].items():
        rows = network_config["rows"]
        cols = network_config["cols"]
        lat_step = (max_lat - min_lat) / rows
        lon_step = (max_lon - min_lon) / cols
        grid_steps[network_type] = (lat_step, lon_step)
    
    return grid_steps


def generate_location(
    network_type: str,
    region_name: str,
    location_id: int,
    lat_min: float,
    lat_max: float,
    lon_min: float,
    lon_max: float
) -> Location:
    """Generate a location for a given region."""
    return Location(
        location_id,
        region_name,
        network_type,
        round(lat_min, 2),
        round(lat_max, 2),
        round(lon_min, 2),
        round(lon_max, 2)
    )


def generate_and_add_locations(self, config: dict) -> List[Location]:
    """Generates locations for all network types and adds them to the repository."""
    
    locations = []
    grid_steps = calculate_grid_steps(config)
    location_id = 1000  # Initial location ID
    
    for network_type, network_config in config["network_configs"].items():
        rows = network_config["rows"]
        cols = network_config["cols"]
        region_names = network_config["region_names"]

        # Ensure region names match grid size
        if len(region_names) != rows * cols:
            raise ValueError(f"The number of region names for {network_type} must match {rows * cols}.")
        
        # Get latitude and longitude step size for the grid
        lat_step, lon_step = grid_steps[network_type]
        region_counter = 0
        
        # Generate locations for each region in the grid
        for i in range(rows):
            for j in range(cols):
                region_name = region_names[region_counter]
                region_counter += 1
                
                lat_min = config["Latitude"][0] + i * lat_step
                lat_max = config["Latitude"][0] + (i + 1) * lat_step
                lon_min = config["Longitude"][0] + j * lon_step
                lon_max = config["Longitude"][0] + (j + 1) * lon_step
                
                location = generate_location(
                    network_type, region_name, location_id, lat_min, lat_max, lon_min, lon_max
                )
                self.repository.add(location)
                locations.append(location)
                
                location_id += 1  # Increment location ID for next location
                
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
        self.element_count = network_config

    def generate_ip(self) -> str:
        """Generate a random IP address."""
        return ".".join(str(random.randint(0, 255)) for _ in range(4))

    def generate_cell_info(self, network_type: str, element_type: str):
        """Generate cell info based on network type and element type."""
        if network_type in ["2G", "3G"] and "BTS" in element_type:
            return random.randint(1, 9999), random.randint(1, 255), None
        elif network_type in ["4G", "5G"] and ("eNodeBs" in element_type or "gNodeB" in element_type):
            return None, None, random.randint(1, 255)
        return None, None, None

    def assign_function(self, element_type: str, network_type: str) -> List[dict]:
        """Assign functions to network elements."""
        function_list = []
        functions_by_network = {
            "2G": [
                {"element_type": "BSC", "name": "BSC Function", "description": "Base Station Controller"},
                {"element_type": "BTS", "name": "BTS Function", "description": "Base Transceiver Station"},
                {"element_type": "MSC", "name": "MSC Function", "description": "Mobile Switching Center"},
                {"element_type": "SMSC", "name": "SMSC Function", "description": "SMS Center"},
                {"element_type": "HLR", "name": "HLR Function", "description": "Home Location Register"}
            ],
            "3G": [
                {"element_type": "SGSN", "name": "SGSN Function", "description": "Serving GPRS Support Node"},
                {"element_type": "GGSN", "name": "GGSN Function", "description": "Gateway GPRS Support Node"},
                # Add other functions as needed...
            ],
            # Add more network types (4G, 5G) similarly...
        }
        
        for func in functions_by_network.get(network_type, []):
            if element_type == func["element_type"]:
                function_list.append(func)
        
        return function_list

    def generate_element_info(self, network_type: str, element_type: str) -> dict:
        """Generate element information."""
        cell_id, lac, tac = self.generate_cell_info(network_type, element_type)
        
        element_info = {
            "element_id": random.randint(1000, 9999),
            "element_name": f"{network_type}_{element_type}_{random.randint(1000, 9999)}",
            "network_type": network_type,
            "ip_address": self.generate_ip(),
            "location_id": 1,  # Replace with dynamic location if needed
            "status": random.choice(["Active", "Inactive"]),
            "function": self.assign_function(element_type, network_type)
        }
        
        if cell_id is not None and lac is not None:
            element_info["cell_id"] = cell_id
            element_info["lac"] = lac
        if tac is not None:
            element_info["tac"] = tac
        
        return element_info

    def generate_elements(self, network_type: str, element_type: str, num_elements: int = 5) -> List[dict]:
        """Generate a list of network elements."""
        return [self.generate_element_info(network_type, element_type) for _ in range(num_elements)]

    def generate_network_elements(self, network_type: str) -> dict:
        """Generate network elements for the specified network type."""
        network_elements = {}
        
        for element_type in self.network_element_types.get(network_type, []):
            num_elements = self.element_count.get(network_type, {}).get(element_type, 1)
            generated_elements = self.generate_elements(network_type, element_type, num_elements)
            
            for element_info in generated_elements:
                network_element = NetworkElement(**element_info)
                self.repository.add(network_element)
            
            network_elements[element_type] = generated_elements
        
        return network_elements
