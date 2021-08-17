# NobleSchool
## How to get running.
* Clone this github repository.
``` git clone https://github.com/daser/nobleschool.git```
* Activate the virtual environment.
```source venv/bin/activate```
* Install all the dependencies from the requirements.txt file
```pip install -r requirements.txt```
* Run the server
```python manage.py runserver```
This shall run the server on the http://localhost:8000/ url.

## Note
* The login view has been implemented and the 'home' view is now restricted, to access it create a super user using
```python manage.py createsuperuser```
* Follow the prompts to enter your username, email and password
* Run the server and go to http://localhost:8000/ you will be redirected to the login route http://localhost:8000/login
* Enter the username and password for the super user you created to access the home page
* You may need to login everytime you restart the server.

