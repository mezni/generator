from typing import List, Tuple, Optional
from entities import NetworkElementType, ServiceType


class ServiceTypeFactory:
    def __init__(self):
        self.service_types = {
            "2G": {
                "bearer_types": ["Circuit-Switched"],
                "service_types": {
                    "Voice Call": {
                        "nodes": ["MSC"],
                        "bearer_type": "Circuit-Switched",
                        "jitter_range": (0, 5),
                        "latency_range": (100, 500),
                        "throughput_range": (10, 100),
                        "packet_loss_range": (0, 2),
                        "call_setup_time_range": (1000, 3000),
                        "mos_range": (3.0, 3.5),
                    },
                    "SMS": {
                        "nodes": ["SMSC"],
                        "bearer_type": "Circuit-Switched",
                        "jitter_range": (0, 5),
                        "latency_range": (100, 500),
                        "throughput_range": (10, 100),
                        "packet_loss_range": (0, 2),
                        "call_setup_time_range": (1000, 3000),
                        "mos_range": (3.0, 3.5),
                    },
                    "MMS": {
                        "nodes": ["MMSC"],
                        "bearer_type": "Circuit-Switched",
                        "jitter_range": (0, 5),
                        "latency_range": (100, 500),
                        "throughput_range": (10, 100),
                        "packet_loss_range": (0, 2),
                        "call_setup_time_range": (1000, 3000),
                        "mos_range": (3.0, 3.5),
                    },
                },
            },
            "3G": {
                "bearer_types": ["Circuit-Switched", "Packet-Switched"],
                "service_types": {
                    "Voice Call": {
                        "nodes": ["RNC", "MSC"],
                        "bearer_type": "Circuit-Switched",
                        "jitter_range": (5, 20),
                        "latency_range": (50, 200),
                        "throughput_range": (100, 500),
                        "packet_loss_range": (0, 1),
                        "call_setup_time_range": (500, 1500),
                        "mos_range": (3.5, 4.0),
                    },
                    "SMS": {
                        "nodes": ["SMSC"],
                        "bearer_type": "Circuit-Switched",
                        "jitter_range": (5, 20),
                        "latency_range": (50, 200),
                        "throughput_range": (100, 500),
                        "packet_loss_range": (0, 1),
                        "call_setup_time_range": (500, 1500),
                        "mos_range": (3.5, 4.0),
                    },
                    "Data": {
                        "nodes": ["RNC", "GGSN"],
                        "bearer_type": "Packet-Switched",
                        "jitter_range": (5, 20),
                        "latency_range": (50, 200),
                        "throughput_range": (100, 500),
                        "packet_loss_range": (0, 1),
                        "call_setup_time_range": (500, 1500),
                        "mos_range": (3.5, 4.0),
                    },
                    "MMS": {
                        "nodes": ["MMSC"],
                        "bearer_type": "Packet-Switched",
                        "jitter_range": (5, 20),
                        "latency_range": (50, 200),
                        "throughput_range": (100, 500),
                        "packet_loss_range": (0, 1),
                        "call_setup_time_range": (500, 1500),
                        "mos_range": (3.5, 4.0),
                    },
                    "Video Call": {
                        "nodes": ["IMS"],
                        "bearer_type": "Circuit-Switched",
                        "jitter_range": (5, 20),
                        "latency_range": (50, 200),
                        "throughput_range": (100, 500),
                        "packet_loss_range": (0, 1),
                        "call_setup_time_range": (500, 1500),
                        "mos_range": (3.5, 4.0),
                    },
                },
            },
            "4G": {
                "bearer_types": ["Packet-Switched", "VoLTE", "VoWiFi"],
                "service_types": {
                    "Voice Call": {
                        "nodes": ["IMS"],
                        "bearer_type": "VoLTE",
                        "jitter_range": (2, 10),
                        "latency_range": (10, 50),
                        "throughput_range": (500, 1000),
                        "packet_loss_range": (0, 0.5),
                        "call_setup_time_range": (300, 1000),
                        "mos_range": (4.0, 4.5),
                    },
                    "SMS": {
                        "nodes": ["SMSC", "IMS"],
                        "bearer_type": "IMS",
                        "jitter_range": (2, 10),
                        "latency_range": (10, 50),
                        "throughput_range": (500, 1000),
                        "packet_loss_range": (0, 0.5),
                        "call_setup_time_range": (300, 1000),
                        "mos_range": (4.0, 4.5),
                    },
                    "Data": {
                        "nodes": ["eNodeB", "SGW", "PGW"],
                        "bearer_type": "Packet-Switched",
                        "jitter_range": (2, 10),
                        "latency_range": (10, 50),
                        "throughput_range": (500, 1000),
                        "packet_loss_range": (0, 0.5),
                        "call_setup_time_range": (300, 1000),
                        "mos_range": (4.0, 4.5),
                    },
                    "MMS": {
                        "nodes": ["MMSC"],
                        "bearer_type": "Packet-Switched",
                        "jitter_range": (2, 10),
                        "latency_range": (10, 50),
                        "throughput_range": (500, 1000),
                        "packet_loss_range": (0, 0.5),
                        "call_setup_time_range": (300, 1000),
                        "mos_range": (4.0, 4.5),
                    },
                    "Video Call": {
                        "nodes": ["IMS"],
                        "bearer_type": "VoLTE",
                        "jitter_range": (2, 10),
                        "latency_range": (10, 50),
                        "throughput_range": (500, 1000),
                        "packet_loss_range": (0, 0.5),
                        "call_setup_time_range": (300, 1000),
                        "mos_range": (4.0, 4.5),
                    },
                    "VoLTE": {
                        "nodes": ["IMS"],
                        "bearer_type": "VoLTE",
                        "jitter_range": (2, 10),
                        "latency_range": (10, 50),
                        "throughput_range": (500, 1000),
                        "packet_loss_range": (0, 0.5),
                        "call_setup_time_range": (300, 1000),
                        "mos_range": (4.0, 4.5),
                    },
                    "VoWiFi": {
                        "nodes": ["IMS"],
                        "bearer_type": "VoWiFi",
                        "jitter_range": (2, 10),
                        "latency_range": (10, 50),
                        "throughput_range": (500, 1000),
                        "packet_loss_range": (0, 0.5),
                        "call_setup_time_range": (300, 1000),
                        "mos_range": (4.0, 4.5),
                    },
                },
            },
            "5G": {
                "bearer_types": ["Packet-Switched", "VoNR", "VoWiFi", "NB-IoT"],
                "service_types": {
                    "Voice Call": {
                        "nodes": ["IMS"],
                        "bearer_type": "VoNR",
                        "jitter_range": (1, 5),
                        "latency_range": (1, 20),
                        "throughput_range": (1000, 10000),
                        "packet_loss_range": (0, 0.1),
                        "call_setup_time_range": (100, 500),
                        "mos_range": (4.5, 5.0),
                    },
                    "SMS": {
                        "nodes": ["SMSC", "IMS"],
                        "bearer_type": "IMS",
                        "jitter_range": (1, 5),
                        "latency_range": (1, 20),
                        "throughput_range": (1000, 10000),
                        "packet_loss_range": (0, 0.1),
                        "call_setup_time_range": (100, 500),
                        "mos_range": (4.5, 5.0),
                    },
                    "Data": {
                        "nodes": ["gNodeB", "SGW-U", "PGW-C"],
                        "bearer_type": "Packet-Switched",
                        "jitter_range": (1, 5),
                        "latency_range": (1, 20),
                        "throughput_range": (1000, 10000),
                        "packet_loss_range": (0, 0.1),
                        "call_setup_time_range": (100, 500),
                        "mos_range": (4.5, 5.0),
                    },
                    "MMS": {
                        "nodes": ["MMSC"],
                        "bearer_type": "Packet-Switched",
                        "jitter_range": (1, 5),
                        "latency_range": (1, 20),
                        "throughput_range": (1000, 10000),
                        "packet_loss_range": (0, 0.1),
                        "call_setup_time_range": (100, 500),
                        "mos_range": (4.5, 5.0),
                    },
                    "Video Call": {
                        "nodes": ["IMS"],
                        "bearer_type": "VoNR",
                        "jitter_range": (1, 5),
                        "latency_range": (1, 20),
                        "throughput_range": (1000, 10000),
                        "packet_loss_range": (0, 0.1),
                        "call_setup_time_range": (100, 500),
                        "mos_range": (4.5, 5.0),
                    },
                },
            },
        }

    def create_service_type(
        self,
        service_type_id: int,
        network_technology: str,
        service_type: str,
        bearer_type: str,
        managing_node: List[str],
        jitter_range: Tuple[int, int],
        latency_range: Tuple[int, int],
        packet_loss_range: Tuple[int, int],
        call_setup_time_range: Tuple[int, int],
        mos_range: Tuple[int, int],
        volte_flag: Optional[bool] = None,
        vowifi_flag: Optional[bool] = None,
    ) -> ServiceType:
        return ServiceType(
            service_type_id=service_type_id,
            network_technology=network_technology,
            service_type=service_type,
            bearer_type=bearer_type,
            managing_node=managing_node,
            jitter_range=jitter_range,
            latency_range=latency_range,
            packet_loss_range=packet_loss_range,
            call_setup_time_range=call_setup_time_range,
            mos_range=mos_range,
            volte_flag=volte_flag,
            vowifi_flag=vowifi_flag,
        )

    def create_service_types(self) -> List[ServiceType]:
        service_type_id = 1
        service_list = []

        for network_technology, tech_data in self.service_types.items():
            for service_name, service_data in tech_data["service_types"].items():
                managing_node_list = service_data["nodes"]

                for bearer_type in tech_data["bearer_types"]:
                    volte_flag = False
                    vowifi_flag = False
                    peak_download_speed = None
                    peak_upload_speed = None

                    if bearer_type == "VoLTE":
                        volte_flag = True
                    if bearer_type == "VoWiFi":
                        vowifi_flag = True

                    #                    if service_name in ["Data", "MMS", "Video Call", "VoLTE", "VoWiFi"]:
                    #                        peak_download_speed = service_data["throughput_range"][1]
                    #                        peak_upload_speed = service_data["throughput_range"][1]

                    service_type = self.create_service_type(
                        service_type_id,
                        network_technology,
                        service_name,
                        bearer_type,
                        managing_node_list,
                        service_data["jitter_range"],
                        service_data["latency_range"],
                        service_data["packet_loss_range"],
                        service_data["call_setup_time_range"],
                        service_data["mos_range"],
                        volte_flag,
                        vowifi_flag,
                    )
                    service_list.append(service_type)
                    service_type_id += 1

        return service_list


class NetworkElementTypeFactory:
    def __init__(self):
        self.network_elements = {
            "2G": [
                (
                    "BTS",
                    "Base Transceiver Station: A base station responsible for radio communication with the mobile station.",
                ),
                (
                    "BSC",
                    "Base Station Controller: Manages multiple BTS units, responsible for call setup and handovers.",
                ),
                (
                    "MSC",
                    "Mobile Switching Center: Routes calls and manages connections in the mobile network.",
                ),
                (
                    "HLR",
                    "Home Location Register: A central database that stores subscriber information and location.",
                ),
                (
                    "VLR",
                    "Visitor Location Register: A temporary database that stores subscriber information for a specific location.",
                ),
                (
                    "AUC",
                    "Authentication Center: Responsible for verifying subscriber identities.",
                ),
                (
                    "SMSC",
                    "Short Message Service Center: Handles SMS delivery between users.",
                ),
                (
                    "GMSC",
                    "Gateway MSC: Routes calls between mobile and other networks like PSTN.",
                ),
            ],
            "3G": [
                (
                    "NodeB",
                    "NodeB: The 3G base station responsible for radio communication.",
                ),
                (
                    "RNC",
                    "Radio Network Controller: Manages NodeBs and controls radio access.",
                ),
                (
                    "MSC",
                    "Mobile Switching Center: Routes calls and manages connections in the mobile network.",
                ),
                (
                    "SGSN",
                    "Serving GPRS Support Node: Responsible for packet-switched data routing.",
                ),
                (
                    "GGSN",
                    "Gateway GPRS Support Node: The node that connects the GPRS network to external data networks.",
                ),
                ("HLR", "Home Location Register: Stores subscriber information."),
                (
                    "VLR",
                    "Visitor Location Register: Temporarily stores subscriber data when they roam.",
                ),
                (
                    "CGF",
                    "Charging Gateway Function: Handles billing and charging for network usage.",
                ),
                ("SMSC", "Short Message Service Center: Manages SMS delivery."),
                (
                    "PCRF",
                    "Policy and Charging Rules Function: Determines user policies and charging.",
                ),
                (
                    "IMS",
                    "The IMS (IP Multimedia Subsystem) is a core network element in modern mobile networks.",
                ),
            ],
            "4G": [
                (
                    "eNodeB",
                    "Evolved NodeB: The base station in 4G LTE, responsible for radio access.",
                ),
                (
                    "EPC",
                    "Evolved Packet Core: The core network architecture for 4G LTE, handling both data and voice services.",
                ),
                (
                    "SGW",
                    "Serving Gateway: Routes data from the eNodeB to the external network.",
                ),
                (
                    "PGW",
                    "PDN Gateway: Provides connectivity between the LTE network and external IP networks.",
                ),
                (
                    "MME",
                    "Mobility Management Entity: Manages mobility and session control for 4G networks.",
                ),
                (
                    "HSS",
                    "Home Subscriber Server: Stores user profile and authentication data.",
                ),
                (
                    "PCRF",
                    "Policy and Charging Rules Function: Manages quality of service and charging policies.",
                ),
                ("SMSC", "Short Message Service Center: Manages SMS delivery."),
                (
                    "VoLTE Gateway",
                    "Voice over LTE Gateway: Facilitates voice communication over the LTE network.",
                ),
                (
                    "IMS",
                    "The IMS (IP Multimedia Subsystem) is a core network element in modern mobile networks.",
                ),
            ],
            "5G": [
                (
                    "gNodeB",
                    "gNodeB: The 5G base station responsible for providing radio access.",
                ),
                (
                    "AMF",
                    "Access and Mobility Management Function: Handles the registration, mobility, and security of users in 5G.",
                ),
                (
                    "SMF",
                    "Session Management Function: Manages the session state in 5G networks.",
                ),
                (
                    "UPF",
                    "User Plane Function: Handles data packet forwarding and routing in 5G.",
                ),
                (
                    "PCF",
                    "Policy Control Function: Manages policy control and charging rules in 5G.",
                ),
                (
                    "AF",
                    "Application Function: Interacts with the 5G core to provide network-related application services.",
                ),
                (
                    "HSS",
                    "Home Subscriber Server: Stores user profile and authentication data.",
                ),
                (
                    "UDM",
                    "Unified Data Management: Manages subscriber data across all network functions.",
                ),
                (
                    "NRF",
                    "Network Repository Function: Handles discovery and management of 5G network functions.",
                ),
                (
                    "VoNR Gateway",
                    "Voice over New Radio Gateway: Facilitates voice communication over the 5G network.",
                ),
                (
                    "NSSF",
                    "Network Slice Selection Function: Manages network slice selection for 5G services.",
                ),
                (
                    "IMS",
                    "The IMS (IP Multimedia Subsystem) is a core network element in modern mobile networks.",
                ),
            ],
        }

    def create_network_element_type(
        self,
        network_element_type_id: int,
        network_technology: str,
        network_element_name: str,
        network_element_desc: str,
    ) -> NetworkElementType:
        return NetworkElementType(
            network_element_type_id=network_element_type_id,
            network_technology=network_technology,
            network_element_name=network_element_name,
            network_element_desc=network_element_desc,
        )

    def create_network_element_types(self) -> List[NetworkElementType]:
        element_types = []
        network_element_type_id = 1
        for network_technology, elements in self.network_elements.items():
            for name, desc in elements:
                element = self.create_network_element_type(
                    network_element_type_id,
                    network_technology,
                    name,
                    desc,
                )
                element_types.append(element)
                network_element_type_id += 1
        return element_types
