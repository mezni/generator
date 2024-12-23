from factories import NetworkElementTypeFactory, ServiceTypeFactory

factory = NetworkElementTypeFactory()
elements = factory.create_network_element_types()

for element in elements:
    print(element)


factory = ServiceTypeFactory()
services = factory.create_service_types()

for service in services:
    print(service)
