**User Registration**

Colllection of APIs used to `register` the user, `verify` the OTP and `login`.


**User Registration API**

POST https://immense-cliffs-30014.herokuapp.com/register

**User Registration**

Colllection of APIs used to `register` the user, `verify` the OTP and `login`.


**User Registration API**

POST https://immense-cliffs-30014.herokuapp.com/register

**Request Body**:
```
{
  "email": "sac2023@gmail.com",
  "name": "sac",
  "password": "1235",
  "phone_number": "917899309972",
  "is_verified": false
}
```

**Response**
`Success`:

HTTP:200
```
{
  "id": 5,
  "email": "sac2023@gmail.com",
  "name": "sac",
  "phone_number": "917899309972",
  "is_verified": false,
  "password": "f60f0244b794b4abcbcf334b72325b7b456b15751cd15200c01b1131"
}
```

`Error`
HTTP:500
```
{
    "msg": "error"
}
```
**Request Body**:
```
{
  "email": "sac2023@gmail.com",
  "name": "sac",
  "password": "1235",
  "phone_number": "917899309972",
  "is_verified": false
}
```

**Response**
`Success`:
 HTTP:200
```
{
  "id": 5,
  "email": "sac2023@gmail.com",
  "name": "sac",
  "phone_number": "917899309972",
  "is_verified": false,
  "password": "f60f0244b794b4abcbcf334b72325b7b456b15751cd15200c01b1131"
}
```

`Error`:
HTTP:500
```
{
    "msg": "error"
}
```

-----------------------------------------------------------------------------------------------------

POST https://immense-cliffs-30014.herokuapp.com/verify

**User Verification**

**Request Body**:
```
{
      "email":"sac2023@gmail.com",
      "otp":"836428",             
      "user_id": "5"              

}
 ```
**Response**
`Success`:
 HTTP:200
```
{
  "msg": "user verified"
}
```
`Error`
 HTTP:500
```
 {
    "msg": "invalid otp"
 }
```
 `Error`
 HTTP:404
 ```
 {
   "msg": "User Doesnt exist"
  }
```   
-----------------------------------------------------------------------------------------------------------------------------

POST https://immense-cliffs-30014.herokuapp.com/login

**User Login**

**Request Body**:
```
{
    "email": "sac2023@gmail.com",
    "password": "1235"
}
```
**Response**
HTTP:200
```
{
  "msg":"success"
}
```
`Error`
HTTP:500
```
 {
  "msg": "invalid credentials"
 }
 ```
 
--------------------------------------------------------------------------------------------------------------        
      

**Notes:**
```
    This application is build using Python-Django and REST Framework, We have also used Dockerso that it creates a isolated ENV to install all the dependicies to work on and Have deployed in Heroku.
```
  
