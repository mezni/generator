from abc import ABC, abstractmethod
from typing import List
from entities import Customer, Network, Bearer


class ConfigRepository(ABC):
    @abstractmethod
    def get_random_customer(self, customer_type: str) -> Customer:
        pass

    @abstractmethod
    def get_random_network(self, network_type: str) -> Network:
        pass

    @abstractmethod
    def get_random_bearer(self) -> Bearer:
        pass
