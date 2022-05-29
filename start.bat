git add . 
git commit -m "added new bill"
git push
python manage.py runserver
@echo off
start "Akal Tools" "http://127.0.0.1:8000/"
pause