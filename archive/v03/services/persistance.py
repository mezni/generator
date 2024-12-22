import random
from entities import Location, NetworkElement
from interfaces import LocationRepositoryInterface, NetworkElementRepositoryInterface

# In-memory example of LocationRepository
class InMemoryLocationRepository(LocationRepositoryInterface):
    def __init__(self):
        self.locations = {}

    def add(self, location: Location) -> None:
        self.locations[location.Location_id] = location

    def get_by_id(self, location_id: int) -> Location:
        return self.locations.get(location_id)

    def get_all(self) -> List[Location]:
        return list(self.locations.values())

    def get_all_by_network_type(self, network_type: str) -> List[Location]:
        return [loc for loc in self.locations.values() if loc.network_type == network_type]

    def get_random_by_network_type(self, network_type: str) -> Location:
        matching_locations = [loc for loc in self.locations.values() if loc.network_type == network_type]
        if matching_locations:
            return random.choice(matching_locations)
        return None

    def delete(self, location_id: int) -> None:
        if location_id in self.locations:
            del self.locations[location_id]

    def update(self, location_id: int, updated_location: Location) -> None:
        self.locations[location_id] = updated_location

# In-memory example of NetworkElementRepository
class InMemoryNetworkElementRepository(NetworkElementRepositoryInterface):
    def __init__(self):
        self.network_elements = {}

    def add(self, network_element: NetworkElement) -> None:
        self.network_elements[network_element.element_id] = network_element

    def get_by_id(self, element_id: int) -> NetworkElement:
        return self.network_elements.get(element_id)

    def get_all(self) -> List[NetworkElement]:
        return list(self.network_elements.values())

    def get_all_by_network_type(self, network_type: str) -> List[NetworkElement]:
        return [ne for ne in self.network_elements.values() if ne.network_type == network_type]

    def update(self, element_id: int, updated_network_element: NetworkElement) -> None:
        self.network_elements[element_id] = updated_network_element

    def delete(self, element_id: int) -> None:
        if element_id in self.network_elements:
            del self.network_elements[element_id]
