

### Step 4: Create a virtual environment

```jsx
python -m venv venv
```

activate venv in ur terminel

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

### Step 10: Create an admin login

```jsx
python manage.py createsuperuser
```

SUPERUSER (admin)
username: pizza
email: pizza@gmail.com
password: 123