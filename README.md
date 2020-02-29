# alpha_blog

alpha_blog is a blogging website which supports multiple regional languages. Blogging, which was once the trend of the decade, is now nearly dead. People spend all their time following social media like Facebook, Instagram & Snapchat and the days of writing and narrating real life experiences are long past gone. I wanted to revitalize the trend with local language support so that many of the users which were never part of the trend can also join in the fun.

# Modules used in developing website
All the template files for the project was made using HTML, CSS & JavaScript. SQLite database was used to store information about posts and users. The business logic for the website was written in python using the Flask Microweb Framework, which allows you to integrate python files with HTML & CSS files to create elegant website. Flask also supports multiple “extensions” to add more functionality. Some of the major modules we used are:

Flask-Bootstrap 
Flask-Bootstrap packages Bootstrap into an extension that mostly consists of a blueprint named ‘bootstrap’. It can also create links to serve Bootstrap from a content delivery network (CDN) and works with no boilerplate code in your application 

Flask-Login 
Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time 

Flask-Mail 
One of the most basic functions in a web application is the ability to send emails to your users.The Flask-Mail extension provides a simple interface to set up SMTP with your Flask application and to send messages from your views and scripts. 

Flask-Moment
Formatting of dates and times in Flask templates using moment.js. 

Flask-WTF 
Simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA. 

Flask-SQLAlchemy 
Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application. It aims to simplify using SQLAlchemy with Flask by providing useful defaults and extra helpers that make it easier to accomplish common tasks. 

PyJWT 
Use of JSON Web Tokens 
User Sign In ([username/password]) => Authentication Server => User Authenticated, JWT Created and return to USER 
USER (User passes [JWT] When making API Calls) => Application server => Application verifies and processes API Call => send data / message to USER

SQLAlchemy 
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL. 
It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language. 

ElasticSearch 
Elasticsearch is a search engine based on the Lucene library. It provides a distributed, multitenant-capable full-text search engine with an HTTP web interface and schema-free JSON documents. Elasticsearch is developed in Java. 
Programming Languages used – Python + HTML/CSS , JavaScript,SQL


# Requirements
alembic==0.9.6
Babel==2.5.1
blinker==1.4
certifi==2017.7.27.1
chardet==3.0.4
click==6.7
dominate==2.3.1
elasticsearch==6.1.1
Flask==1.0.2
Flask-Babel==0.11.2
Flask-Bootstrap==3.3.7.1
Flask-Login==0.4.0
Flask-Mail==0.9.1
Flask-Migrate==2.1.1
Flask-Moment==0.5.2
Flask-SQLAlchemy==2.3.2
Flask-WTF==0.14.2
guess_language-spirit==0.5.3
idna==2.6
itsdangerous==0.24
Jinja2==2.10
Mako==1.0.7
MarkupSafe==1.0
PyJWT==1.5.3
python-dateutil==2.6.1
python-dotenv==0.7.1
python-editor==1.0.3
pytz==2017.2
requests==2.18.4
six==1.11.0
SQLAlchemy==1.1.14
urllib3==1.22
visitor==0.1.3
Werkzeug==0.14.1
WTForms==2.1

//requirements for Heroku
#psycopg2==2.7.3.1
#gunicorn==19.7.1
