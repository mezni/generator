import random
from typing import List, Union
from entities import Subscriber


class SubscriberFactory:
    def generate_msisdn(
        self,
        msisdn_type: str,
        country_code=None,
        ndc_ranges=None,
        prefixes=None,
        digits=6,
    ) -> str:
        try:
            if digits < 1:
                raise ValueError("The 'digits' parameter must be a positive integer.")

            if msisdn_type in ("home", "national"):
                if not country_code or not ndc_ranges:
                    raise ValueError(
                        "'country_code' and 'ndc_ranges' are required for 'home' or 'national' types."
                    )

                if isinstance(ndc_ranges, int):
                    ndc_value = ndc_ranges  # Use the single integer as the NDC
                elif isinstance(ndc_ranges, (list, tuple)) and len(ndc_ranges) == 2:
                    selected_range = random.choice(ndc_ranges)
                    ndc_value = random.randint(selected_range[0], selected_range[1])
                else:
                    raise ValueError(
                        "'ndc' must be an integer or a range (list/tuple) with two values."
                    )

                subscriber_number = random.randint(
                    10 ** (digits - 1), 10**digits - 1
                )  # Random subscriber number
                return f"{country_code}{ndc_value}{subscriber_number}"

            elif msisdn_type == "international":
                if not prefixes:
                    raise ValueError("'prefixes' is required for 'international' type.")

                selected_prefix = random.choice(prefixes)  # Randomly select a prefix
                subscriber_number = random.randint(
                    10 ** (digits - 1), 10**digits - 1
                )  # Random subscriber number
                return f"{selected_prefix}{subscriber_number}"

            else:
                raise ValueError(f"Invalid msisdn_type: {msisdn_type}")
        except ValueError as e:
            return f"Error generating MSISDN: {str(e)}"

    def generate_imsi(self, mcc: str, mnc: str) -> str:
        if not mcc.isdigit() or not mnc.isdigit():
            raise ValueError("MCC and MNC must be numeric strings.")

        subscriber_number = random.randint(100000000, 999999999)
        return f"{mcc}{mnc}{subscriber_number}"

    def generate_imei(self) -> str:
        try:
            # Generate the first 14 digits of the IMEI
            imei = [str(random.randint(0, 9)) for _ in range(14)]

            # Calculate the Luhn checksum digit
            total_sum = 0
            for i in range(14):
                digit = int(imei[i])
                if i % 2 == 1:  # Double every second digit
                    digit *= 2
                    if digit > 9:  # If doubling results in two digits, subtract 9
                        digit -= 9
                total_sum += digit

            # Compute the check digit
            check_digit = (10 - (total_sum % 10)) % 10
            imei.append(str(check_digit))

            # Return the full IMEI as a string
            return "".join(imei)
        except Exception as e:
            return f"Error generating IMEI: {str(e)}"

    def generate_sim_id(self) -> str:
        return f"SIM-{random.randint(100000000000000, 999999999999999)}"

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
    ) -> Subscriber:
        return Subscriber(
            subscriber_id=subscriber_id,
            subscriber_type=subscriber_type,
            msisdn=self.generate_msisdn(
                msisdn_type=subscriber_type,
                country_code=country_code,
                ndc_ranges=ndc_ranges,
                prefixes=prefixes,
            ),
            imsi=self.generate_imsi(mcc=mcc, mnc=mnc),
            imei=self.generate_imei(),
            sim_id=self.generate_sim_id(),
            account_type=account_type,
            account_status=account_status,
        )
