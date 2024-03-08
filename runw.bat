call .env\Scripts\activate.bat
cd app
python manage.py runserver
cd ..
call .env\Scripts\deactivate.bat