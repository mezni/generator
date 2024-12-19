class Customer:
    def __init__(self, cus_key, msisdn, imsi, imei, customer_type):
        self.cus_key = cus_key
        self.msisdn = msisdn
        self.imsi = imsi
        self.imei = imei
        self.customer_type = customer_type

    def __repr__(self):
        return f"Customer(cus_key={self.cus_key}, msisdn={self.msisdn}, imsi={self.imsi}, imei={self.imei}, customer_type={self.customer_type})"


class Network:
    def __init__(
        self,
        network_type,
        plmn,
        rnc_id,
        lac,
        cell_id,
        MSC_Address,
        SGSN_Address,
        GGSN_Address=None,
        SGW_Address=None,
        PGW_Address=None,
        MME_Address=None,
    ):
        self.network_type = network_type
        self.plmn = plmn
        self.rnc_id = rnc_id
        self.lac = lac
        self.cell_id = cell_id
        self.MSC_Address = MSC_Address
        self.SGSN_Address = SGSN_Address
        self.GGSN_Address = GGSN_Address
        self.SGW_Address = SGW_Address
        self.PGW_Address = PGW_Address
        self.MME_Address = MME_Address

    def __repr__(self):
        return f"Network(network_type={self.network_type}, plmn={self.plmn}, rnc_id={self.rnc_id}, lac={self.lac}, cell_id={self.cell_id}, MSC_Address={self.MSC_Address})"


class Bearer:
    def __init__(self, bearer_id, bearer_type, qos):
        self.bearer_id = bearer_id
        self.bearer_type = bearer_type
        self.qos = qos

    def __repr__(self):
        return f"Bearer(bearer_id={self.bearer_id}, bearer_type={self.bearer_type}, qos={self.qos})"


class CustomerAggregate:
    def __init__(self):
        self.home_customers = []
        self.national_customers = []
        self.international_customers = []

    def add_customer(self, customer):
        if customer.customer_type == "home":
            self.home_customers.append(customer)
        elif customer.customer_type == "national":
            self.national_customers.append(customer)
        elif customer.customer_type == "international":
            self.international_customers.append(customer)

    def get_all_customers(self):
        return (
            self.home_customers,
            self.national_customers,
            self.international_customers,
        )


class NetworkAggregate:
    def __init__(self):
        self.networks_3g = []
        self.networks_4g = []

    def add_network(self, network):
        if network.network_type == "3G":
            self.networks_3g.append(network)
        elif network.network_type == "4G":
            self.networks_4g.append(network)

    def get_all_networks(self):
        return self.networks_3g, self.networks_4g


class BearerAggregate:
    def __init__(self):
        self.bearers = []

    def add_bearer(self, bearer):
        self.bearers.append(bearer)

    def get_all_bearers(self):
        return self.bearers


class CallDetailRecord:
    def __init__(self, call_id,call_type, duration, start_time, end_time):
        self.call_id = call_id
        self.call_type = call_type
        self.duration = duration
        self.start_time = start_time
        self.end_time = end_time


    def __repr__(self):
        return f"CDR(call_id={self.call_id}, call_type={self.call_type}, duration={self.duration})"