from abc import ABC, abstractmethod
from typing import List, Optional
import random


class LocationRepositoryInterface(ABC):
    @abstractmethod
    def add(self, location: "Location") -> None:
        """Adds a new location to the repository."""
        pass

    @abstractmethod
    def get_all(self) -> List["Location"]:
        """Retrieves all locations from the repository."""
        pass

    @abstractmethod
    def get_by_id(self, location_id: int) -> Optional["Location"]:
        """Retrieves a location by its ID."""
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Optional["Location"]:
        """Retrieves a location by its name."""
        pass

    @abstractmethod
    def get_all_by_network_type(self, network_type: str) -> List["Location"]:
        """Retrieves all locations filtered by network type."""
        pass

    @abstractmethod
    def get_random_by_network_type(self, network_type: str) -> Optional["Location"]:
        """Retrieves a random location filtered by network type."""
        pass

    @abstractmethod
    def delete(self, location_id: int) -> None:
        """Deletes a location by its ID."""
        pass


class NetworkElementRepositoryInterface(ABC):
    @abstractmethod
    def add(self, network_element: "NetworkElement") -> None:
        """Adds a new network element to the repository."""
        pass

    @abstractmethod
    def get_all(self) -> List["NetworkElement"]:
        """Retrieves all network elements from the repository."""
        pass

    @abstractmethod
    def get_by_id(self, element_id: int) -> Optional["NetworkElement"]:
        """Retrieves a network element by its ID."""
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Optional["NetworkElement"]:
        """Retrieves a network element by its name."""
        pass

    @abstractmethod
    def get_by_location_id(self, location_id: int) -> List["NetworkElement"]:
        """Retrieves all network elements associated with a specific location ID."""
        pass

    @abstractmethod
    def get_all_by_network_type(self, network_type: str) -> List["NetworkElement"]:
        """Retrieves all network elements filtered by network type."""
        pass

    @abstractmethod
    def get_random_by_network_type(
        self, network_type: str
    ) -> Optional["NetworkElement"]:
        """Retrieves a random network element filtered by network type."""
        pass

    @abstractmethod
    def delete(self, element_id: int) -> None:
        """Deletes a network element by its ID."""
        pass
