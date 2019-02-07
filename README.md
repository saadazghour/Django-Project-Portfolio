# Personal Portfolio

A Simple Portfolio and Blog app build with Django and templates styled with Bootstrap framework .

# Running the Project Locally

## First, clone the repository to your local machine :

```bash
git clone https://github.com/SAzghour/Django-Project-Portfolio.git
```

## Create a virtual environment :

```bash
$ python -m venv .venv
```

## Activate the virtual environment on Windows :


```bash
$ source venv/Scripts/activate
```

## Install the requirements :

```bash
$ pip install -r requirements.txt
```

## Run collect static :

```bash
$ python manage.py collectstatic
```

## To create an superuser account, use this command :

```bash
$ python manage.py createsuperuser
```

## Apply the migrations :

```bash
$ python manage.py migrate
```

## Finally, run the development server :

```bash
$ python manage.py runserver
```

<b>The project will be available at :   </b>  **http://localhost:8000**