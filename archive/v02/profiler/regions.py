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

# Function to group cities based on their geographical region
def group_cities_by_region(cities):
    northern_region = []
    mid_region = []
    western_region = []
    
    for city, (lat, lon) in cities.items():
        if lat >= 35.0:  # North
            northern_region.append(city)
        elif 33.0 <= lat < 35.0:  # Mid
            mid_region.append(city)
        else:  # West
            western_region.append(city)
    
    return {
        "Northern Region": northern_region,
        "Mid Region": mid_region,
        "Western Region": western_region
    }

# Group cities
grouped_cities = group_cities_by_region(cities)

# Print results
for region, cities_in_region in grouped_cities.items():
    print(f"{region}: {', '.join(cities_in_region)}")
