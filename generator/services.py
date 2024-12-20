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
        end_time = self.reference_time - timedelta(minutes=random.randint(1,int(self.switch_dump_time_in_minutes)))
        duration_seconds = random.randint(0, 3600)
        start_time = end_time - timedelta(seconds=duration_seconds)

        source_customer = self.config_repository.get_random_customer("home")
        rand_val = random.random()
        if rand_val < 0.7:
            destination_type = "home"  # 70% chance
        elif rand_val < 0.99:
            destination_type = "national"  # 29% chance
        else:
            destination_type = "international"  # 1% chance
        
        destination_customer = self.config_repository.get_random_customer(destination_type)
        while source_customer == destination_customer:
            destination_customer = self.config_repository.get_random_customer(destination_type)


        return {
            "call_id": self.call_seq,
            "call_type": call_type,
            "call_direction": "OUTGOING",
            "start_time": start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "end_time": end_time.strftime("%Y-%m-%d %H:%M:%S"),
            "duration": duration_seconds,
            "calling_party_number": source_customer.msisdn,
            "called_party_number": destination_customer.msisdn,
        }

    def generate_cdrs(self, count=5):
        cdrs = []
        for _ in range(count):
            cdr = self.generate_cdr(call_type=CallType.VOICE_OUTGOING)
            cdrs.append(cdr)
            print (cdr)
        return cdrs
