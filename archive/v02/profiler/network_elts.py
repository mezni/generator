import random

# Define network types
NETWORK_2G = '2G'
NETWORK_3G = '3G'
NETWORK_4G = '4G'
NETWORK_5G = '5G'

# Function to generate random IP address
def generate_ip():
    return f"192.168.{random.randint(0, 255)}.{random.randint(1, 254)}"

# Function to generate network element information
def generate_network_element_info(network_type, element_type):
    # Common properties for all network elements
    element_info = {
        "Element ID": random.randint(1000, 9999),
        "Element Name": f"{network_type}_{element_type}_{random.randint(1000, 9999)}",
        "IP Address": generate_ip(),
        "Location": f"Datacenter {random.choice(['A', 'B', 'C'])}",
        "Status": random.choice(['Active', 'Inactive']),
        "Function": None  # This will be populated based on network type
    }
    
    # Populate function based on network type and element
    if network_type == NETWORK_2G:
        if "BSC" in element_type:
            element_info["Function"] = "Control and manage base stations (BTS), Radio resource management"
        elif "BTS" in element_type:
            element_info["Function"] = "Connects to mobile devices, handles radio communication"
        elif "MSC" in element_type:
            element_info["Function"] = "Manages voice call routing and switching"
        elif "SMSC" in element_type:
            element_info["Function"] = "SMS messaging gateway"
        elif "HLR" in element_type:
            element_info["Function"] = "Database for subscriber information"
    
    elif network_type == NETWORK_3G:
        if "SGSN" in element_type:
            element_info["Function"] = "Session management, mobility management"
        elif "GGSN" in element_type:
            element_info["Function"] = "Gateway for data traffic, routing to external networks"
        elif "MSC" in element_type:
            element_info["Function"] = "Voice and data call routing, handover management"
        elif "RNC" in element_type:
            element_info["Function"] = "Radio network controller, manages NodeBs"
        elif "NodeB" in element_type:
            element_info["Function"] = "Radio access, interfaces with user devices"
    
    elif network_type == NETWORK_4G:
        if "eNodeB" in element_type:
            element_info["Function"] = "Manages the radio access network (evolved NodeB)"
        elif "PGW" in element_type:
            element_info["Function"] = "Packet data gateway, routing of data"
        elif "SGW" in element_type:
            element_info["Function"] = "Serves as the gateway for user data traffic in the EPC"
        elif "MME" in element_type:
            element_info["Function"] = "Session and mobility management"
        elif "PCRF" in element_type:
            element_info["Function"] = "Policy and charging rules function"
    
    elif network_type == NETWORK_5G:
        if "gNodeB" in element_type:
            element_info["Function"] = "Next-generation radio base station for 5G NR"
        elif "SMF" in element_type:
            element_info["Function"] = "Session management function, manages user sessions"
        elif "UPF" in element_type:
            element_info["Function"] = "User plane function, forwards user data traffic"
        elif "AMF" in element_type:
            element_info["Function"] = "Access management function"
        elif "AUSF" in element_type:
            element_info["Function"] = "Authentication server function"
    
    return element_info

# List of elements for each network type
network_elements = {
    "2G": ["BSC", "BTS", "MSC", "SMSC", "HLR"],
    "3G": ["SGSN", "GGSN", "MSC", "RNC", "NodeB"],
    "4G": ["eNodeB", "PGW", "SGW", "MME", "PCRF"],
    "5G": ["gNodeB", "SMF", "UPF", "AMF", "AUSF"]
}

# Generate network element information for each network type
all_network_elements = {}
for network_type, elements in network_elements.items():
    all_network_elements[network_type] = [generate_network_element_info(network_type, element) for element in elements]

# Print generated network element information
for network_type, elements in all_network_elements.items():
    print(f"\nNetwork Elements for {network_type}:")
    for element in elements:
        print(f"  Element Name: {element['Element Name']}")
        print(f"  Element ID: {element['Element ID']}")
        print(f"  IP Address: {element['IP Address']}")
        print(f"  Location: {element['Location']}")
        print(f"  Status: {element['Status']}")
        print(f"  Function: {element['Function']}")
        print("\n")
