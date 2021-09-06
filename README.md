# myRestAPI
**my rest api with django rest framework**


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
