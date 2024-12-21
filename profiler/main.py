import random

# Define the country and cities in Tunisia
country = "Tunisia"
cities = [
    "Tunis", "Sfax", "Sousse", "Bizerte", "Gabès", "Kairouan", 
    "Nabeul", "Tozeur", "Monastir", "Gafsa", "Mahdia", "Sidi Bouzid"
]

# Network types as variables
NETWORK_2G = '2G'
NETWORK_3G = '3G'
NETWORK_4G = '4G'
NETWORK_5G = '5G'

# Generate random latitude and longitude for a location in Tunisia
def generate_lat_lon():
    lat = round(random.uniform(33.0, 37.5), 6)  # Approximate latitudes of Tunisia
    lon = round(random.uniform(7.0, 11.5), 6)   # Approximate longitudes of Tunisia
    return lat, lon

# Location types based on urban/rural classification
location_types = ["Urban", "Suburban", "Rural"]

# Function to generate TAC (Tracking Area Code) for 3G and 4G
def generate_TAC():
    return random.randint(100, 999)  # Random TAC between 100 and 999

# Function to generate LAC (Location Area Code) for 2G and 3G
def generate_LAC():
    return random.randint(1, 255)  # LAC ranges from 1 to 255

# Function to generate a cell ID for NodeB/eNodeB/gNodeB
def generate_cell_id():
    return random.randint(1, 10000)  # Cell ID between 1 and 10000

# Function to generate Location ID based on network type and city
def generate_location_id(network_type, city):
    return f"{network_type[:2]}-{city[:3].upper()}-{random.randint(1000, 9999)}"

# Function to generate RNC for 3G, BSC for 2G, or eNodeB/gNodeB for 4G/5G
def generate_rnc_bsc_enodeb_gnodeb(network_type):
    if network_type == NETWORK_3G:
        return f"RNC-{random.randint(100, 999)}"  # Random RNC ID for 3G
    elif network_type == NETWORK_2G:
        return f"BSC-{random.randint(100, 999)}"  # Random BSC ID for 2G
    elif network_type == NETWORK_4G:
        return f"eNodeB-{random.randint(1000, 9999)}"  # Random eNodeB ID for 4G
    elif network_type == NETWORK_5G:
        return f"gNodeB-{random.randint(1000, 9999)}"  # Random gNodeB ID for 5G
    return None

# Function to generate location information for 2G, 3G, 4G, and 5G elements
def generate_location_info(network_type):
    city = random.choice(cities)
    lat, lon = generate_lat_lon()
    location_type = random.choice(location_types)
    
    # Generate TAC for 3G and 4G
    TAC = generate_TAC() if network_type in [NETWORK_3G, NETWORK_4G, NETWORK_5G] else None
    
    # Generate LAC for 2G and 3G
    LAC = generate_LAC() if network_type in [NETWORK_2G, NETWORK_3G] else None
    
    # Generate a cell ID for NodeB/eNodeB/gNodeB
    cell_id = generate_cell_id()

    # Generate Location ID based on network type and city
    location_id = generate_location_id(network_type, city)

    # Generate RNC/BSC/eNodeB/gNodeB
    rnc_bsc_enodeb_gnodeb = generate_rnc_bsc_enodeb_gnodeb(network_type)

    # Return a dictionary with location details for each network type
    return {
        "Location ID": location_id,
        "Country": country,
        "Network Type": network_type,
        "City": city,
        "Latitude": lat,
        "Longitude": lon,
        "Location Type": location_type,
        "TAC": TAC,
        "LAC": LAC,
        "Cell ID": cell_id,
        "RNC/BSC/eNodeB/gNodeB": rnc_bsc_enodeb_gnodeb
    }

# Generate location variables for each network type
location_2g = generate_location_info(NETWORK_2G)
location_3g = generate_location_info(NETWORK_3G)
location_4g = generate_location_info(NETWORK_4G)
location_5g = generate_location_info(NETWORK_5G)

# Store the generated locations in a list or dictionary
locations = {
    "2G": location_2g,
    "3G": location_3g,
    "4G": location_4g,
    "5G": location_5g
}

# Print the generated locations
for network, loc in locations.items():
    print(f"Location for {network} network:")
    for key, value in loc.items():
        print(f"{key}: {value}")
    print("\n")
