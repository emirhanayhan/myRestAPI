# myRestAPI
**my rest api with django rest framework**


BaseUrl = 'Localhost:8080'
---
**How to start in venv**


- open cmd in venv

- execute python manage.py runserver command in venv

---

**How to run tests**


- open cmd

- execute python manage.py test in command prompt

---

**How to start in docker**

- open cmd

- execute docker run --publish 8000:8000 djangoapi

---

**Swagger Docs**

BaseUrl/docapi

---

**URLs**

- BaseUrl/api    

- BaseUrl/docapi      
 
---

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

---
                                       

**Get Trip List**

/api/trip/


**Create Trip**

POST/trip/
Response:HTTP 201 Created


**Get a specific Trip**

/api/trip/tripId


**Get a specific Trip by user id**

api/tripwithuserid/userId


**Update**

PUT /trip/tripId


**Update by user id**

PUT /tripwithuserid/userId


**Delete Trip**

DELETE /trip/tripId


**Get a non-existent Trip or user**

```javascript
'errors':
{
'code':404,
'message':'Record can not found'
}
```
