import random
from typing import List, Optional
from entities import Subscriber
from interfaces import SubscriberRepository


class InMemorySubscriberRepository(SubscriberRepository):
    def __init__(self):
        self._subscribers = []

    def save(self, subscriber: Subscriber) -> None:
        """Save a subscriber to the repository."""
        self._subscribers.append(subscriber)

    def get_all(self) -> List[Subscriber]:
        """Get all subscribers."""
        return self._subscribers

    def get_random_by_type(self, subscriber_type: str) -> Optional[Subscriber]:
        """Get a random subscriber by subscriber type."""
        filtered_subscribers = [
            sub for sub in self._subscribers if sub.subscriber_type == subscriber_type
        ]
        if filtered_subscribers:
            return random.choice(filtered_subscribers)
        return None
