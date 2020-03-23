# colorifix

Execute by running the following line in the command window:

> python manage.py runserver

The database db.sqlite3 is set up with some dummy data. It can be accessed with [DB Browser for Sqlite](https://sqlitebrowser.org/)

To update the database schema or create a new one:

> python manage.py makemigrations Viewer

> python manage.py sqlmigrate Viewer 0001

> python manage.py migrate
