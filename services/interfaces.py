from abc import ABC, abstractmethod
from typing import List, Optional
from entities import Subscriber  

class SubscriberRepository(ABC):
    @abstractmethod
    def save(self, subscriber: Subscriber) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[Subscriber]:
        pass

    @abstractmethod
    def get_random_by_type(self, subscriber_type: str) -> Subscriber:
        pass
