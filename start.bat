title AKALTOOLS
echo WELCOME TO AKALTOOLS
git add . 
git commit -m "added new bill"
git push 
"C:\Users\THEUSER\AppData\Local\Google\Chrome\Application\chrome.exe"
start "Akal Tools" "http://127.0.0.1:8000/"
python manage.py runserver
