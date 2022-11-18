requirements:
	pip install -r requirements.txt

run:
	docker build -t pokerapi .
	docker run pokerapi

unit_test: requirements
	pytest tests/unit

test: unit_test