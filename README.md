# movieApi_DRF

# Welcome to My Api
This is an Api using the django and django rest_framework that has a database with over 1000 rows of data.

## Description
The Api contains several endpoints to get information about movies from the database.
Each movie has the following parameters: movie_id, title, lead_actor, release_year.

## Installation
I used the django package manager to install all of the dependencies for this project
pip insatll django
pip instal djangorestframework.
pipenv shell (to create a virtual environment)
All dependencies are found in the requirements.txt file

## Usage
Use the postman to test the different end points in the Api.
Users can register and get a token.
Anyone can get all movies and also get a particular movie.
Only Registered users can edit, create and delete movies


## Postman Documentation and project URL
This project is hosted on the railway.app cloud provider
All the endpoints are documented on postman web and published. Pls find below the link to the postman Documentation & project url

POSTMAN DOCUMENTATION
https://web.postman.co/workspace/My-Workspace~40b90451-b666-41bf-841d-18c49bd578de/example/29299100-c6774bca-123f-44e1-85d4-2ef76cf94c3c 

PROJECT URL
https://web-production-555f.up.railway.app/

NOTE:
Please use POSTMAN for the API testing. I have provided examples in the documentation to guide the usage.
The browser is not efficient to test all the enpoints.
Only the https://web-production-555f.up.railway.app/get-movies/ endpoint can be effectively tested with the browser
