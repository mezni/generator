import random
from datetime import datetime, timedelta
from interfaces import ConfigRepository


class CDRGeneratorService:
    def __init__(self, config_repository: ConfigRepository):
        self.config_repository = config_repository
        self.call_seq = int(datetime.now().timestamp())

    def generate_cdr(self, call_type: str):
        self.call_seq += 1
        end_time = datetime.now()
        duration_seconds = random.randint(0, 3600)
        start_time = end_time - timedelta(seconds=duration_seconds)

        customer = self.config_repository.get_random_customer("home")

        return {
            "call_id": self.call_seq,
            "call_type": call_type,
            "start_time": start_time,
            "end_time": end_time,
            "duration": duration_seconds,
            "msisdn": customer.msisdn,
        }

    def generate_cdrs(self, count=5):
        """Generate multiple CDRs."""
        cdrs = []
        for _ in range(count):
            cdr = self.generate_cdr(call_type="home")
            cdrs.append(cdr)
            print(cdr)
        return cdrs
