import random
from datetime import datetime, timedelta
from value_objects import CallType
from interfaces import ConfigRepository


class CDRGeneratorService:
    def __init__(self, config_repository: ConfigRepository):
        self.config_repository = config_repository
        self.call_seq = int(datetime.now().timestamp())
        self.switch_dump_time_in_minutes = 30
        self.reference_time = datetime.now()

    def generate_cdr(self, call_type: str):
        self.call_seq += 1
        end_time = self.reference_time - timedelta(
            minutes=random.randint(1, int(self.switch_dump_time_in_minutes))
        )
        duration_seconds = random.randint(0, 3600)
        start_time = end_time - timedelta(seconds=duration_seconds)

        source_customer = self.config_repository.get_random_customer("home")
        rand_val = random.random()
        if rand_val < 0.7:
            destination_type = "home"
        elif rand_val < 0.99:
            destination_type = "national"
        else:
            destination_type = "international"

        destination_customer = self.config_repository.get_random_customer(
            destination_type
        )
        while source_customer == destination_customer:
            destination_customer = self.config_repository.get_random_customer(
                destination_type
            )

        call_type_rand = random.random()
        if call_type_rand < 0.7:
            call_type = CallType.VOICE_OUTGOING
        elif call_type_rand < 0.95:
            call_type = CallType.SMS_MO
        else:
            call_type = CallType.DATA_SESSION
        cdr = {
            "call_id": self.call_seq,
            "call_type": call_type,
            "call_direction": "Outgoing",
            "start_time": start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "end_time": end_time.strftime("%Y-%m-%d %H:%M:%S"),
            "duration": duration_seconds,
            "calling_party_number": source_customer.msisdn,
            "calling_party_imsi": source_customer.imsi,
            "calling_party_imei": source_customer.imei,
            "called_party_number": destination_customer.msisdn,
            "called_party_imsi": destination_customer.imsi,
        }
        network_rand = random.random()

        if network_rand < 0.5:
            node = self.config_repository.get_random_network("3G")
            cdr["rnc_id"] = node.rnc_id
            cdr["lac"] = node.lac
            cdr["cell_id"] = node.cell_id
            cdr["MSC_Address"] = node.MSC_Address
            cdr["SGSN_Address"] = node.SGSN_Address
            cdr["GGSN_Address"] = node.GGSN_Address
        else:
            node = self.config_repository.get_random_network("4G")
            bearer = self.config_repository.get_random_bearer()
            cdr["tac"] = node.tac
            cdr["SGW_Address"] = node.SGW_Address
            cdr["PGW_Address"] = node.PGW_Address
            cdr["MME_Address"] = node.MME_Address
            cdr["bearer_type"] = bearer.bearer_type
            cdr["bearer_type"] = bearer.bearer_type
            cdr["bearer"] = (
                bearer.bearer_type
                + " "
                + str(bearer.qos["gbr"])
                + " "
                + str(bearer.qos["mbr"])
            )

        return cdr

    def generate_cdrs(self, count=5):
        cdrs = []
        for _ in range(count):
            cdr = self.generate_cdr(call_type=CallType.VOICE_OUTGOING)
            cdrs.append(cdr)
            print(cdr)
        return cdrs
