from typing import List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class ServiceType:
    service_type_id: int
    network_technology: str
    service_type: str
    bearer_type: str
    managing_node: List[str]
    jitter_range: Tuple[int, int]
    latency_range: Tuple[int, int]
    packet_loss_range: Tuple[int, int]
    call_setup_time_range: Tuple[int, int]
    mos_range: Tuple[int, int]
    volte_flag: Optional[bool] = None
    vowifi_flag: Optional[bool] = None


@dataclass
class NetworkElementType:
    network_element_type_id: int
    network_technology: str
    network_element_name: str
    network_element_desc: str
