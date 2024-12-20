from datetime import datetime, timedelta
import random
from tinydb import TinyDB
from entities import Customer, Network, Bearer, CallDetailRecord
from entities import CustomerAggregate, NetworkAggregate, BearerAggregate

class CDRGeneratorService:
    def __init__(self,home_customers,national_customers,international_customers,networks_3g,networks_4g,bearers):  
        self.call_seq = int(datetime.now().timestamp())

    def generate_cdr(self,call_type):
        self.call_seq = self.call_seq+1
        end_time = datetime.now() 
        duration_seconds = random.randint(0, 3600) 
        start_time = end_time - timedelta(seconds=duration_seconds)
        cdr = CallDetailRecord(
        call_id = self.call_seq,
        call_type=call_type,
        duration = duration_seconds,
        start_time = start_time,
        end_time = end_time
        )
        return cdr
        
    def generate_cdrs(self):
        cdrs = []
        for _ in range(5):  
            cdr = self.generate_cdr(call_type="voice")
            cdrs.append(cdr)
        return cdrs

class DataLoaderService:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.customer_aggregate = CustomerAggregate()
        self.network_aggregate = NetworkAggregate()
        self.bearer_aggregate = BearerAggregate()

    def load_customers(self):
        customers_table = self.db.table("customers")
        customers = customers_table.all()

        for customer_data in customers:
            for cus_key, cus_info in customer_data.items():
                customer = Customer(
                    cus_key=cus_key,
                    msisdn=cus_info.get("msisdn"),
                    imsi=cus_info.get("imsi"),
                    imei=cus_info.get("imei"),
                    customer_type=cus_info.get("customer_type"),
                )
                self.customer_aggregate.add_customer(customer)

    def load_networks(self):
        nodes_table = self.db.table("nodes")
        nodes = nodes_table.all()

        for node_data in nodes:
            for node_key, node_info in node_data.items():
                network = Network(
                    network_type=node_info.get("network_type"),
                    plmn=node_info.get("plmn"),
                    rnc_id=node_info.get("rnc_id"),
                    lac=node_info.get("lac"),
                    cell_id=node_info.get("cell_id"),
                    MSC_Address=node_info.get("MSC_Address"),
                    SGSN_Address=node_info.get("SGSN_Address"),
                    GGSN_Address=node_info.get("GGSN_Address", None),
                    SGW_Address=node_info.get("SGW_Address", None),
                    PGW_Address=node_info.get("PGW_Address", None),
                    MME_Address=node_info.get("MME_Address", None),
                )
                self.network_aggregate.add_network(network)

    def load_bearers(self):
        bearers_table = self.db.table("bearers")
        bearers = bearers_table.all()

        for bearer_data in bearers:
            for bearer_key, bearer_info in bearer_data.items():
                bearer = Bearer(
                    bearer_id=bearer_info.get("Bearer_ID"),
                    bearer_type=bearer_info.get("Bearer_Type"),
                    qos=bearer_info.get("QoS"),
                )
                self.bearer_aggregate.add_bearer(bearer)

    def get_results(self):
        home_customers, national_customers, international_customers = (
            self.customer_aggregate.get_all_customers()
        )
        networks_3g, networks_4g = self.network_aggregate.get_all_networks()
        bearers = self.bearer_aggregate.get_all_bearers()
        return (
            home_customers,
            national_customers,
            international_customers,
            networks_3g,
            networks_4g,
            bearers,
        )

    def print_results(self):
        home_customers, national_customers, international_customers = (
            self.customer_aggregate.get_all_customers()
        )
        networks_3g, networks_4g = self.network_aggregate.get_all_networks()
        bearers = self.bearer_aggregate.get_all_bearers()

        print("Home Customers:", home_customers)
        print("National Customers:", national_customers)
        print("International Customers:", international_customers)
        print("3G Networks:", networks_3g)
        print("4G Networks:", networks_4g)
        print("Bearers:", bearers)


