from tinydb import TinyDB

# Load the config.json as TinyDB database
db = TinyDB("../config.json")

customers_home = []
customers_national = []
customers_international = []
networks_3g = []
networks_4g = []
bearers_list = []

# Access the 'customers' table
customers_table = db.table("customers")
customers = customers_table.all()

# Iterate through customers and categorize them by customer type
for customer_data in customers:
    for cus_key, cus_info in customer_data.items():
        customer_type = cus_info.get("customer_type")
        msisdn = cus_info.get("msisdn")
        imsi = cus_info.get("imsi")
        imei = cus_info.get("imei")
        customer = {"cus_key": cus_key, "msisdn": msisdn, "imsi": imsi, "imei": imei}
        if customer_type == "home":
            customers_home.append(customer)
        elif customer_type == "national":
            customers_national.append(customer)
        elif customer_type == "international":
            customers_international.append(customer)

# Access the 'nodes' table for network information
nodes_table = db.table("nodes")
nodes = nodes_table.all()

# Iterate through nodes and categorize them by network type
for node_data in nodes:
    for node_key, node_info in node_data.items():
        network_type = node_info.get("network_type")
        if network_type == "3G":
            networks_3g.append(node_info)
        elif network_type == "4G":
            networks_4g.append(node_info)

# Access the 'bearers' table
bearers_table = db.table("bearers")
bearers = bearers_table.all()

# Iterate through bearers and store their information
for bearer_data in bearers:
    for bearer_key, bearer_info in bearer_data.items():
        bearer = {
            "Bearer_ID": bearer_info.get("Bearer_ID"),
            "Bearer_Type": bearer_info.get("Bearer_Type"),
            "QoS": bearer_info.get("QoS"),
        }
        bearers_list.append(bearer)

# Print the categorized customers, networks, and bearers
print("Home Customers:", customers_home)
print("National Customers:", customers_national)
print("International Customers:", customers_international)
print("3G Networks:", networks_3g)
print("4G Networks:", networks_4g)
print("Bearers:", bearers_list)
