# assignment
___________________________________________________________________
USE POSTMAN FOR TESTING APIs
___________________________________________________________________
open cmd
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


1.Sign up (for more information go to : \sign.jpg) :-
  http://127.0.0.1:8000/signup/
  
2.Login (for more information go to : \login.jpg)  :-
  http://127.0.0.1:8000/login/
  
3.show_data : this api show the data of logged user 
              , * add Authorization in Headers of postman with token (login to get token)
              , * pass user_id with url (login to get user_id)
              , * (for more information go to : \show.jpg) 
               :- 
  http://127.0.0.1:8000/show_data/5/
  
