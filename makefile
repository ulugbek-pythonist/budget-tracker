run:
	python manage.py runserver 8001

migs:
	python manage.py makemigrations

mig:
	python manage.py migrate

super:
	python manage.py createsuperuser