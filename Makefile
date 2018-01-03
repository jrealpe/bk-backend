install:
	pip install -r requirements.txt
	./manage.py migrate
	./manage.py loaddata fixtures/auth.json
	./manage.py loaddata fixtures/ec_provinces.json
	./manage.py loaddata fixtures/ec_cities.json
