class Bearer:
    def __init__(self, bea_key, bearer_id, bearer_type, qos):
        self.bea_key = bea_key
        self.bearer_id = bearer_id
        self.bearer_type = bearer_type
        self.qos = qos

    def __repr__(self):
        return f"Bearer(bearer_id={self.bearer_id}, bearer_type={self.bearer_type}, qos={self.qos})"


class Network:
    def __init__(
        self,
        net_key,
        network_type,
        plmn,
        rnc_id=None,
        lac=None,
        cell_id=None,
        tac=None,
        MSC_Address=None,
        SGSN_Address=None,
        GGSN_Address=None,
        SGW_Address=None,
        PGW_Address=None,
        MME_Address=None,
    ):
        self.net_key = net_key
        self.network_type = network_type
        self.plmn = plmn
        self.rnc_id = rnc_id
        self.lac = lac
        self.cell_id = cell_id
        self.tac = tac
        self.MSC_Address = MSC_Address
        self.SGSN_Address = SGSN_Address
        self.GGSN_Address = GGSN_Address
        self.SGW_Address = SGW_Address
        self.PGW_Address = PGW_Address
        self.MME_Address = MME_Address

    def __repr__(self):
        if self.network_type == "3G":
            return f"Network(network_type={self.network_type}, plmn={self.plmn}, rnc_id={self.rnc_id}, lac={self.lac}, cell_id={self.cell_id}, MSC_Address={self.MSC_Address}, MSC_SGSN_AddressAddress={self.SGSN_Address}, GGSN_Address={self.GGSN_Address})"
        if self.network_type == "4G":
            return f"Network(network_type={self.network_type}, plmn={self.plmn}, tac={self.tac}, SGW_Address={self.SGW_Address}, PGW_Address={self.PGW_Address}, MME_Address={self.MME_Address})"


class Customer:
    def __init__(self, cus_key, msisdn, imsi, imei, customer_type):
        self.cus_key = cus_key
        self.msisdn = msisdn
        self.imsi = imsi
        self.imei = imei
        self.customer_type = customer_type

    def __repr__(self):
        return f"Customer(cus_key={self.cus_key}, msisdn={self.msisdn}, imsi={self.imsi}, imei={self.imei}, customer_type={self.customer_type})"
