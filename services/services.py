import random
from typing import List, Optional, Dict, Union
from interfaces import SubscriberRepository
from entities import Subscriber
from factories import SubscriberFactory


class SubscriberService:
    def __init__(self, repository: SubscriberRepository):
        self.repository = repository
        self.factory = SubscriberFactory()

    def create_subscriber(
        self,
        subscriber_id: int,
        subscriber_type: str,
        account_type: str,
        account_status: str,
        mcc: str,
        mnc: str,
        country_code: str = None,
        ndc_ranges: List[Union[int, tuple]] = None,
        prefixes: List[str] = None,
        digits: int = 6,
    ) -> Subscriber:
        """
        Create and save a subscriber using the provided parameters.
        """
        msisdn = self.factory.generate_msisdn(
            msisdn_type=subscriber_type,
            country_code=country_code,
            ndc_ranges=ndc_ranges,
            prefixes=prefixes,
            digits=digits,
        )
        imsi = self.factory.generate_imsi(mcc=mcc, mnc=mnc)
        imei = self.factory.generate_imei()
        sim_id = self.factory.generate_sim_id()

        subscriber = Subscriber(
            subscriber_id=subscriber_id,
            subscriber_type=subscriber_type,
            msisdn=msisdn,
            imsi=imsi,
            imei=imei,
            sim_id=sim_id,
            account_type=account_type,
            account_status=account_status,
        )

        self.repository.save(subscriber)
        return subscriber

    def get_all_subscribers(self) -> List[Subscriber]:
        return self.repository.get_all()

    def get_random_subscriber_by_type(
        self, subscriber_type: str
    ) -> Optional[Subscriber]:
        return self.repository.get_random_by_type(subscriber_type)

    def create_subscribers(self, config: Dict) -> List[Subscriber]:
        """
        Create multiple subscribers based on the provided configuration.
        """
        subscriber_seq = random.randint(10000, 20000)
        subscribers = []

        # Iterate through the configuration and create subscribers
        for subscriber_type, msisdn_config in config["msisdn"].items():
            for _ in range(msisdn_config["count"]):
                subscriber = self.create_subscriber(
                    subscriber_id=subscriber_seq,
                    subscriber_type=subscriber_type,
                    account_type="prepaid",  # Assume "prepaid" for simplicity
                    account_status="active",  # Assume "active" for simplicity
                    mcc="404",  # Example MCC
                    mnc="100",  # Example MNC
                    country_code=msisdn_config.get("country_code"),
                    ndc_ranges=msisdn_config.get("ndc_ranges"),
                    prefixes=msisdn_config.get("prefixes"),
                    digits=msisdn_config.get("digits"),
                )
                subscriber_seq += 1
                subscribers.append(subscriber)

        return subscribers
