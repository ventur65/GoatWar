# GoatWar

Installa mysql, logghi e fai:
CREATE DATABASE goatwar;

Dopodichè non so se devi fare anche il superuser di django.
Nel caso ho fatto:
python manage.py createsuperuser
user: admin
pass: admin
email: admin@admin.com

Poi fai makemigrations e migrate:
python manage.py makemigrations
python manage.py migrate
