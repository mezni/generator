from factories import SubscriberFactory
factory = SubscriberFactory()

# Define the required inputs
subscriber_id = 1
subscriber_type = "international"
account_type = "prepaid"
account_status = "Active"
mcc = "404"  # Mobile Country Code (e.g., India)
mnc = "10"   # Mobile Network Code (e.g., Airtel India)
country_code = "+216"  # Country code for MSISDN
ndc_ranges = [(50, 55), (30, 35)]  # List of NDC ranges for MSISDN
prefixes = ["+91", "+92", "+93"]  # List of international prefixes

# Create a subscriber
subscriber = factory.create_subscriber(
    subscriber_id=subscriber_id,
    subscriber_type=subscriber_type,
    account_type=account_type,
    account_status=account_status,
    mcc=mcc,
    mnc=mnc,
    country_code=country_code,
    ndc_ranges=ndc_ranges,
    prefixes=prefixes,
)


print (subscriber)