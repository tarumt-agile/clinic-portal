# STEP-BY-STEP GUIDE ON HOW TO INSTALL TYPEHSI

## What you guys need to do
make sure you have ```python``` in your laptop if not get here:
<a>https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe</a>
then go vscode extension get ```django```

open a folder for this project, then open that project folder in your vscode.

### paste inside your vscode terminel
```git clone https://github.com/ligitpizza/clinic-portal.git``` <br>
```cd clinic-portal```<br>
```python -m venv venv```<br>
```venv\Scripts\Activate.ps1```<br>
```python -m pip install -r requirements.txt```<br>
```python manage.py migrate```<br>
```python manage.py createsuperuser```<br>

### admin address:
```http://127.0.0.1:8000/admin```<br>

### SUPERUSER (admin) <br>
username: pizza <br>
email: pizza@gmail.com <br>
password: 123 <br>

<hr>

## Additonal steps 
### Step 1: Create a virtual environment

```jsx
python -m venv venv
```

## activate venv in ur terminel

```jsx
venv\Scripts\Activate.ps1
```

### Step 2: Install Django

```jsx
python -m pip install django 
```

### Check it worked:

```jsx
python -m django --version
```

### Step 3: Create the Django project

```jsx
django-admin startproject clinic_portal .
```

### Step 4: Run it

```jsx
python manage.py runserver
```

### Step 5: Create your first app

Stop the server (Ctrl+C), then create your first module — start with accounts (login/roles):

```jsx
python manage.py startapp accounts
```

### Step 6: Set up the database

By default Django uses SQLite (fine for development, no setup needed):

```jsx
python manage.py migrate
```

## Step 7: Create an admin login

```jsx
python manage.py createsuperuser
```
