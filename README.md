# GoatWar

Installa mysql
Per loggare dovresti fare così:
mysql -u root -p
<password bianca>

Solo nel caso non funzionasse il login (come nel mio caso) devi andare a vedere l'utente di default creato in installazione:
cat /etc/mysql/debian.cnf
Troverai le righe user e psw da usare per loggare.
Una volta loggato:
DROP USER 'root'@'localhost';
CREATE USER 'root'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;

Crea database chiamato goatwar:
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
