install:
	pip install -r requiremnts.txt
	python3 manage.py makemigrations
	python3 manage.py migrate
mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
run:
	python3 manage.py runserver