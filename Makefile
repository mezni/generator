# Commands
PYTHON = python3
PIP = $(PYTHON) -m pip
BLACK = $(PYTHON) -m black
FLAKE8 = $(PYTHON) -m flake8
PYTEST = $(PYTHON) -m pytest

# Directories and files
SRC_DIR = ./services
TEST_DIR = tests

# Install dependencies
.PHONY: install
install:
	$(PIP) install -r requirements.txt
	$(PIP) install black flake8 pytest

# Formatting
.PHONY: format
format:
	$(BLACK) $(SRC_DIR)

# Linting
.PHONY: lint
lint:
	$(FLAKE8) $(SRC_DIR)

# Testing
.PHONY: test
test:
	$(PYTEST) $(TEST_DIR)

# Clean up
.PHONY: clean
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
