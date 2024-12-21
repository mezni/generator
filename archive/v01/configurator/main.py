import logging
import yaml
from persistance import (
    TinyDBCustomerRepository,
    TinyDBNodeRepository,
    TinyDBBearerRepository,
)
from services import CustomerService, NodeService, BearerService

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Load YAML configuration
def load_yaml_config(file_path: str):
    with open(file_path, "r") as yaml_file:
        return yaml.safe_load(yaml_file)


# Main entry point
def main():
    # Load config from YAML
    yaml_file = "config.yaml"
    yaml_data = load_yaml_config(yaml_file)

    # Extract db_path and config
    db_path = yaml_data["db_path"]
    config = yaml_data["config"]

    # Initialize repositories and services
    customer_repo = TinyDBCustomerRepository(db_path)
    customer_service = CustomerService(config, customer_repo)
    node_repo = TinyDBNodeRepository(db_path)
    node_service = NodeService(config, node_repo)
    bearer_repo = TinyDBBearerRepository(db_path)
    bearer_service = BearerService(config, bearer_repo)

    # Save data to the database
    customer_service.save_customers()
    node_service.save_nodes()
    bearer_service.save_bearers()

    # Fetch and print random records


#    print(customer_service.get_random("home"))
#    print(node_service.get_random("4G"))
#    print(bearer_service.get_random())

if __name__ == "__main__":
    main()
