import random
from typing import List
from tinydb import TinyDB
from entities import Customer, Network, Bearer
from interfaces import ConfigRepository


class InMemoryConfigRepository(ConfigRepository):
    def __init__(self, db_path: str):
        self.db = TinyDB(db_path)
        self.customers_home = []
        self.customers_national = []
        self.customers_international = []
        self.networks_3g = []
        self.networks_4g = []
        self.bearers = []
        self._load_from_db()

    def _load_from_db(self):
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
                if customer.customer_type == "home":
                    self.customers_home.append(customer)
                elif customer.customer_type == "national":
                    self.customers_national.append(customer)
                elif customer.customer_type == "international":
                    self.customers_international.append(customer)

        networks_table = self.db.table("nodes")
        networks = networks_table.all()

        for network_data in networks:
            for net_key, net_info in network_data.items():
                network = Network(
                    net_key=net_key,
                    network_type=net_info.get("network_type"),
                    plmn=net_info.get("plmn"),
                    rnc_id=net_info.get("rnc_id"),
                    lac=net_info.get("lac"),
                    cell_id=net_info.get("cell_id"),
                    tac=net_info.get("tac"),
                    MSC_Address=net_info.get("MSC_Address"),
                    SGSN_Address=net_info.get("SGSN_Address"),
                    GGSN_Address=net_info.get("GGSN_Address"),
                    SGW_Address=net_info.get("SGW_Address"),
                    PGW_Address=net_info.get("PGW_Address"),
                    MME_Address=net_info.get("MME_Address"),
                )
                if network.network_type == "3G":
                    self.networks_3g.append(network)
                elif network.network_type == "4G":
                    self.networks_4g.append(network)
        bearers_table = self.db.table("bearers")
        bearers = bearers_table.all()

        for bearer_data in bearers:
            for bea_key, bea_info in bearer_data.items():
                bearer = Bearer(
                    bea_key=bea_key,
                    bearer_id=bea_info.get("Bearer_ID"),
                    bearer_type=bea_info.get("Bearer_Type"),
                    qos=bea_info.get("QoS"),
                )
                self.bearers.append(bearer)

    def get_random_customer(self, customer_type: str) -> Customer:
        if customer_type == "home":
            return random.choice(self.customers_home)
        elif customer_type == "national":
            return random.choice(self.customers_national)
        elif customer_type == "international":
            return random.choice(self.customers_international)
        return None

    def get_random_network(self, network_type: str) -> Network:
        if network_type == "3G":
            return random.choice(self.networks_3g)
        elif network_type == "4G":
            return random.choice(self.networks_4g)
        return None

    def get_random_bearer(self) -> Bearer:
        return random.choice(self.bearers)
