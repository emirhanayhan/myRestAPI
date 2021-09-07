# myRestAPI
**my rest api with django rest framework**



**How to start in venv**

I.open cmd in venv

II.execute python manage.py runserver command in venv


**How to run tests**

I. open cmd

II. execute python manage.py test in command prompt


**How to start in docker**

I.open cmd

II. execute docker run --publish 8000:8000 djangoapi


**Swagger Docs**

localhost:8000/docapi


**Get User List**

/api/user/


**Create User**

POST/user/
Response:HTTP 201 Created


**Get specific User**

/api/user/userId


**Update**

PUT /user/userId/


**Delete User**

DELETE /user/userId
                                       

**Get Trip List**

/api/trip/


**Create Trip**

POST/trip/
Response:HTTP 201 Created


**Get a specific Trip**

/api/trip/tripId


**Get a specific Trip by user id**

api/trip/withuserid/userId


**Update**

PUT /trip/tripId


**Update by user id**

PUT /trip/withuserid/userId


**Delete Trip**

DELETE /trip/tripId


**Get a non-existent Trip or user**

Response
'errors':
{
'code':404,
'message':'Record can not found'
}
