# persistance.py
import random
from typing import List
from entities import Location
from interfaces import LocationRepositoryInterface


class InmemLocationRepository(LocationRepositoryInterface):
    def __init__(self):
        self.Location = {}

    def add(self, location: Location) -> None:
        if location.Location_id in self.Location:
            raise ValueError(f"Location with ID {location.Location_id} already exists.")
        self.Location[location.Location_id] = location

    def get_by_id(self, location_id: int) -> Location:
        location = self.Location.get(location_id)
        if not location:
            raise ValueError(f"Location with ID {location_id} not found.")
        return location

    def get_all(self) -> List[Location]:
        return list(self.Location.values())

    def get_all_by_network_type(self, network_type: str) -> List[Location]:
        # Filter Location by the network type
        return [
            location
            for location in self.Location.values()
            if location.network_type == network_type
        ]

    def get_random_by_network_type(self, network_type: str) -> Location:
        # Filter Location by the network type
        filtered_Location = self.get_all_by_network_type(network_type)

        if not filtered_Location:
            raise ValueError(f"No Location found for network type '{network_type}'.")

        # Return a random location from the filtered list
        return random.choice(filtered_Location)

    def delete(self, location_id: int) -> None:
        if location_id not in self.Location:
            raise ValueError(f"Location with ID {location_id} not found.")
        del self.Location[location_id]

    def update(self, location_id: int, updated_location: Location) -> None:
        if location_id not in self.Location:
            raise ValueError(f"Location with ID {location_id} not found.")
        self.Location[location_id] = updated_location
