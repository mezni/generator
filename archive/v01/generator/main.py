from persistance import InMemoryConfigRepository
from services import CDRGeneratorService

config_repository = InMemoryConfigRepository("../config.json")

cdr_generator = CDRGeneratorService(config_repository=config_repository)

cdrs = cdr_generator.generate_cdrs(count=5)
for cdr in cdrs:
    print(cdr)
