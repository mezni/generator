# interfaces.py
from abc import ABC, abstractmethod
from typing import List
from entities import Location


class LocationRepositoryInterface(ABC):
    @abstractmethod
    def add(self, location: Location) -> None:
        """Add a new location to the repository."""
        pass

    @abstractmethod
    def get_by_id(self, location_id: int) -> Location:
        """Retrieve a location by its ID."""
        pass

    @abstractmethod
    def get_all(self) -> List[Location]:
        """Retrieve all Location."""
        pass

    @abstractmethod
    def get_all_by_network_type(self, network_type: str) -> List[Location]:
        """Retrieve all Location filtered by network type."""
        pass

    @abstractmethod
    def get_random_by_network_type(self, network_type: str) -> Location:
        """Retrieve a random location filtered by network type."""
        pass

    @abstractmethod
    def delete(self, location_id: int) -> None:
        """Delete a location by its ID."""
        pass

    @abstractmethod
    def update(self, location_id: int, updated_location: Location) -> None:
        """Update an existing location."""
        pass
