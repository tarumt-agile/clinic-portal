# STEP-BY-STEP GUIDE ON HOW TO INSTALL TYPEHSI

## What you guys need to do
### paste inside your vscode terminel
```git clone https://github.com/yourusername/clinic-portal.git``` <br>
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

## You Guys can ignore these one below
### Step 4: Create a virtual environment

```jsx
python -m venv venv
```

## activate venv in ur terminel

```jsx
venv\Scripts\Activate.ps1
```

### Step 5: Install Django

```jsx
python -m pip install django 
```

### Check it worked:

```jsx
python -m django --version
```

### Step 6: Create the Django project

```jsx
django-admin startproject clinic_portal .
```

### Step 7: Run it

```jsx
python manage.py runserver
```

### Step 8: Create your first app

Stop the server (Ctrl+C), then create your first module — start with accounts (login/roles):

```jsx
python manage.py startapp accounts
```

### Step 9: Set up the database

By default Django uses SQLite (fine for development, no setup needed):

```jsx
python manage.py migrate
```

## Step 10: Create an admin login

```jsx
python manage.py createsuperuser
```
