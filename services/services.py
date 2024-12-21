# service.py
from typing import List
from entities import Location
from interfaces import LocationRepositoryInterface


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
