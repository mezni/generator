from typing import List
from dataclasses import dataclass

@dataclass
class Subscriber:
    """
    Represents a mobile network subscriber with essential attributes.
    """
    subscriber_id: int
    subscriber_type: str  # Home, National, International
    msisdn: str
    imsi: str
    imei: str
    sim_id: str
    account_type: str  # Prepaid, Postpaid
    account_status: str  # Active, Inactive, Suspended, etc.