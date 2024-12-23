from factories import SubscriberFactory
from persistance import InMemorySubscriberRepository  
from services import SubscriberService

# Example configuration
config = {
    "network": {  # Fixed syntax error here
        "mcc": "212",
        "mnc": "01",
    },
    "msisdn": {
        "home": {
            "country_code": "+216",
            "ndc_ranges": [[30, 35], [50, 55]],
            "digits": 6,
            "count": 10,
        },
        "national": {
            "country_code": "+216",
            "ndc_ranges": [[20, 29], [90, 99]],
            "digits": 6,
            "count": 10,
        },
        "international": {
            "prefixes": ["+2126", "+336", "+441", "+491"],
            "digits": 8,
            "count": 10,
        },
    }
}

# Create the SubscriberService
repository = InMemorySubscriberRepository()  # or your actual repository implementation
subscriber_service = SubscriberService(repository)

# Create subscribers from config
subscribers = subscriber_service.create_subscribers(config)

# Print created subscribers
for subscriber in subscribers:
    print(subscriber)
