from services import DataLoaderService, CDRGeneratorService


def main():
    data_loader = DataLoaderService("../config.json")

    data_loader.load_customers()
    data_loader.load_networks()
    data_loader.load_bearers()

    (
        home_customers,
        national_customers,
        international_customers,
        networks_3g,
        networks_4g,
        bearers,
    ) = data_loader.get_results()
    cdr_generator_service = CDRGeneratorService(home_customers,national_customers,international_customers,networks_3g,networks_4g,bearers)
    cdrs=cdr_generator_service.generate_cdrs()
    print (cdrs)

if __name__ == "__main__":
    main()
