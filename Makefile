install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 page_loader
	poetry run flake8 tests

coverage:
	poetry run pytest --cov=page_loader --cov-report=xml
