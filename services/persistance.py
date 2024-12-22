import random
from typing import List, Optional
from entities import Location, NetworkElement
from interfaces import LocationRepositoryInterface, NetworkElementRepositoryInterface


class InMemoryLocationRepository(LocationRepositoryInterface):
    def __init__(self):
        self.locations = []

    def add(self, location: Location) -> None:
        self.locations.append(location)

    def get_all(self) -> List[Location]:
        return self.locations

    def get_by_id(self, location_id: int) -> Optional[Location]:
        return next(
            (loc for loc in self.locations if loc.location_id == location_id), None
        )

    def get_by_name(self, name: str) -> Optional[Location]:
        return next((loc for loc in self.locations if loc.name == name), None)

    def get_all_by_network_type(self, network_type: str) -> List[Location]:
        return [loc for loc in self.locations if loc.network_type == network_type]

    def get_random_by_network_type(self, network_type: str) -> Optional[Location]:
        filtered_locations = self.get_all_by_network_type(network_type)
        return random.choice(filtered_locations) if filtered_locations else None

    def delete(self, location_id: int) -> None:
        self.locations = [
            loc for loc in self.locations if loc.location_id != location_id
        ]


class InMemoryNetworkElementRepository(NetworkElementRepositoryInterface):
    def __init__(self):
        self.network_elements = []

    def add(self, network_element: NetworkElement) -> None:
        self.network_elements.append(network_element)

    def get_all(self) -> List[NetworkElement]:
        return self.network_elements

    def get_by_id(self, element_id: int) -> Optional[NetworkElement]:
        return next(
            (elem for elem in self.network_elements if elem.element_id == element_id),
            None,
        )

    def get_by_name(self, name: str) -> Optional[NetworkElement]:
        return next(
            (elem for elem in self.network_elements if elem.element_name == name), None
        )

    def get_by_location_id(self, location_id: int) -> List[NetworkElement]:
        return [
            elem for elem in self.network_elements if elem.location_id == location_id
        ]

    def get_all_by_network_type(self, network_type: str) -> List[NetworkElement]:
        return [
            elem for elem in self.network_elements if elem.network_type == network_type
        ]

    def get_random_by_network_type(self, network_type: str) -> Optional[NetworkElement]:
        filtered_elements = self.get_all_by_network_type(network_type)
        return random.choice(filtered_elements) if filtered_elements else None

    def delete(self, element_id: int) -> None:
        self.network_elements = [
            elem for elem in self.network_elements if elem.element_id != element_id
        ]
