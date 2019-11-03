# JukeTap API

## Getting Started

### Prerequisites

- Python 3.6
- Some sort of environment manager (we use anything from virtualenv to Anaconda)
- [Postman](https://www.getpostman.com/)

### Setup

```
git clone git@github.com:aakashsethi20/JukeTap_API.git
```

Once cloned, spin up a virtual environment and install dependencies:

```
pip install -r requirements.txt
```

Then, set up environment variables:

1. create a new file called `.env`
  1.1 For Windows, you can skip this step
2. set the following environment variables
  2.1 For Windows,  set the environment variables in the virtual environment

```
DJANGO_SECRET_KEY=<any random string>
DEBUG=True
```

### Run locally

The first time that you run the server locally, you will need to make migrations and migrate to create a SQLite DB file. To do this:

```
python manage.py makemigrations
python manage.py migrate
```

And then run the server:

```
python manage.py runserver
```

The API server should be running at [`http://127.0.0.1`](http://127.0.0.1). Checkout the API documentation [here](https://github.com/aakashsethi20/JukeTap_API/#). <-- Insert API documentation link.

## Postman Collection

The Postman collection for the project is an organic document and will grow as the API grows. It's handy for quick endpoint testing.

Install Postman by following the directions on its [official website](https://www.getpostman.com/) and import the collection from the repository.
