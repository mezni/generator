class LocationLoaderService:
    def __init__(
        self, repository: LocationRepositoryInterface, factory: LocationFactory
    ):
        self.repository = repository
        self.factory = factory

    def load_locations(self, config: dict):
        locations = self.factory.create_locations(config)
        for location in locations:
            self.repository.add(location)
        return locations


class NetworkElementLoaderService:
    def __init__(
        self,
        network_config: Dict,
        location_repo: LocationRepositoryInterface,
        repository: NetworkElementRepositoryInterface,
        factory: NetworkElementFactory,
    ):
        self.network_config = network_config
        self.location_repo = location_repo
        self.repository = repository
        self.factory = factory

    def generate_and_add_network_elements(self):
        network_elements = []
        for network_type in self.network_config:
            for element_type in self.factory.network_element_types.get(
                network_type, []
            ):
                num_elements = self.network_config[network_type].get(element_type, 1)
                location_ids = [
                    location.location_id
                    for location in self.location_repo.get_all_by_network_type(
                        network_type
                    )
                ]

                # Use the factory to create network elements
                elements = self.factory.create_network_elements(
                    network_type, element_type, location_ids, num_elements
                )

                for element in elements:
                    self.repository.add(element)
                    network_elements.append(element)

        return network_elements
