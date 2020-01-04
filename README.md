# P1rateRad1o
Django App to Interface with a Radio Device to send POCSAG messages

## Steps to Run the Project
	1. `pip3 install django`
	2. `export SECRET_KEY=<mysecretkey>`
        3. `python3 manage.py makemigrations`
        4. `python3 manage.py migrate`
	5. `python3 manage.py runserver`

Data is stored in a local sqlite3 DB

To create a superuser:
	`python3 manage.py createsuperuser`
