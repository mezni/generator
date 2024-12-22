import random
from typing import List
from dataclasses import dataclass


@dataclass
class Subscriber:
    subscriber_id: int
    subscriber_type: str  # home, national, international
    msisdn: str
    imsi: str
    imei: str
    sim_id: str
    account_type: str  # prepaid, postpaid
    account_status: str  # Active, Inactive, Suspended, etc.


@dataclass
class NetworkElement:
    network_type: str
    element_id: int
    element_name: str
    ip_address: str
    location_id: int
    status: str
    function: List[dict]
    cell_id: int = None
    lac: int = None
    tac: int = None


@dataclass
class Location:
    network_type: str
    location_id: int
    location_name: str
    lat_min: float
    lat_max: float
    lon_min: float
    lon_max: float
