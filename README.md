# Awards

#### An app for the week 10 project,

12/21/2018

#### By **Sam Kasyoki**

## Description
This is an application that will allow a user to post a project he/she has created and get it reviewed by his/her peers based on 3 different criteria:
1. Design
2. Usability
3. Content

## Link to live site

https://sam10105-awards.herokuapp.com/

## User Stories
1. View posted projects and their details.
2. Post a project to be rated/reviewed.
3. Rate/ review other users' projects.
4. Search for projects.
5. View projects overall score.
6. View my profile page.

## Admin Credentials
- USERNAME = 'samkasyoki'
- PASSWORD = 'samisbae1'

### Technologies Used

- HTML
- CSS
- django-Bootstrap4
- Python3.6
- Heroku
- Django

## Setup/Installation Requirements

### Prerequisites
To use this application, you will need:
- git
- python
- django
- postgresql

### Clone the repo and checkout into the project folder.

- `git clone https://github.com/sam10105/awards.git`
- `cd awards`

### Create and activate the virtual environment

- `python3.6 -m venv virtual`
- `source virtual/bin/activate`

### Install the dependencies

Install dependancies that will create an environment for the app to run.

- `pip install -r requirements.txt`

### Create an .env file and replace the following with your settings:

- SECRET_KEY='342s(s(!hsjd998sde8$=o4$3m!(o+kce2^97kp6#ujhi'
- DEBUG=True
- DB_NAME='awards'
- DB_USER='user'
- DB_PASSWORD='password'
- DB_HOST='127.0.0.1'
- MODE='dev'
- ALLOWED_HOSTS='.localhost','.herokuapp.com','.127.0.0.1'
- DISABLE_COLLECTSTATIC=1

### Make migrations to your database
- `python3.6 manage.py migrate`

### Run `manage.py` in the terminal

- `python3.6 manage.py runserver`

### Known Bugs
None at the moment

### License
Copyright (c) 2018 **Sam Kasyoki**

This project is licensed under the [MIT License](LICENSE).
