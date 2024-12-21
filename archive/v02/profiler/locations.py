import random

# Cities with approximate latitude and longitude coordinates
cities = {
    "Tunis": (33.8869, 10.1895),
    "Sfax": (34.7403, 10.7611),
    "Sousse": (35.8256, 10.6368),
    "Bizerte": (37.2747, 9.8739),
    "Gabès": (33.8833, 10.1000),
    "Kairouan": (35.6611, 9.8756),
    "Nabeul": (36.4563, 10.7563),
    "Tozeur": (33.9182, 8.1291),
    "Monastir": (35.7593, 10.7561),
    "Gafsa": (34.4281, 8.7769),
    "Mahdia": (35.5060, 11.0622),
    "Sidi Bouzid": (35.0000, 9.5000)
}

# Function to generate 5 random locations within a city
def generate_locations(city, lat, lon, num_locations=5):
    locations = []
    for _ in range(num_locations):
        # Generate random variation within a small radius
        lat_variation = random.uniform(-0.05, 0.05)  # Latitude variation within +- 0.05 degrees
        lon_variation = random.uniform(-0.05, 0.05)  # Longitude variation within +- 0.05 degrees
        
        # Calculate the new location
        new_lat = lat + lat_variation
        new_lon = lon + lon_variation
        
        # Append the new location
        locations.append((round(new_lat, 4), round(new_lon, 4)))
    
    return locations

# Generate locations for each city
city_locations = {}
for city, (lat, lon) in cities.items():
    city_locations[city] = generate_locations(city, lat, lon)

# Print the generated locations
for city, locations in city_locations.items():
    print(f"Locations for {city}:")
    for i, (lat, lon) in enumerate(locations, 1):
        print(f"  Location {i}: Latitude = {lat}, Longitude = {lon}")
    print()
