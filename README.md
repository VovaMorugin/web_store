<h1>Generic web store back end with REST API</h1>

<h2>Written in Python using the Django REST framework, can be used with any frontend that conforms to the following endpoints:</h2>


### Customer related endpoints:


## Create new customer token
POST `/api/customer/create/`


### Response body:
```json
{
  "status": true, 
  "customer_token": "395bce87-0edd-4834-9063-a36311e2f81f"
}
```

## Register user and bind it to the customer by the token created before

POST `/api/customer/registration/`

### Request body
```json
{
    "username": "vmoruhin",
    "password": "asdsad123ASd$",
    "email": "vova.morugin@gmail.com",
    "first_name":"Volodymyr",
    "last_name":"Moruhin",
    "token": "395bce87-0edd-4834-9063-a36311e2f81f"
}
```

### Response body
```json
{
    "id": 15,
    "username": "vmoruhin",
    "email": "vova.morugin@gmail.com",
    "first_name": "Volodymyr",
    "last_name": "Moruhin"
}
```
## JWT authorization endpoints:
- /auth/ return access and refresh tokens, 
- /refresh/ is used when access token is expired

POST `/api/jwt/auth/`
### Request body:
```json
{
    "username": "vmoruhin",
    "password": "asdsad123ASd$"
}
```
### Response body:
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyOTA1MzM1NiwianRpIjoiNTVlNmQ0YjkwMWZhNDYwZWJmNjcwNzYxZTg1MGQzMzYiLCJ1c2VyX2lkIjoxNX0.LJA5LW8TvO4WZayXCf5rzsRkDhYv1Qc9F_NaZqR8bSo",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI4Mjc1NzU2LCJqdGkiOiJmN2UzZjQ3NGVkNDY0NWYwOTUxMmM3Y2QzZWQ1NDQ4NiIsInVzZXJfaWQiOjE1fQ.FeNyuVle0VOG2nqgbqsBKi-wCu5hgqwfOUXojaNjckA"
}
```


POST `/api/jwt/refresh/`
### Request body:
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyOTA1MzM1NiwianRpIjoiNTVlNmQ0YjkwMWZhNDYwZWJmNjcwNzYxZTg1MGQzMzYiLCJ1c2VyX2lkIjoxNX0.LJA5LW8TvO4WZayXCf5rzsRkDhYv1Qc9F_NaZqR8bSo"
}
```
### Response body:
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI4Mjc3MjA0LCJqdGkiOiI2OGU1MzVkZWQyMzY0NjdmOGViMGI5ZjJhMzFkMDdmNSIsInVzZXJfaWQiOjE1fQ.MVR_kyQbHW6_aYPNdOes-TVM5tgLyYWJG-AwazYp0PM"
}
```





GET `/api/customer/myorders/`



GET `/api/customer/getuser/`

## Product related endpoints:

GET `/api/product/category/list/`

GET `/api/product/category/get/<int:pk>/`

GET `/api/product/get/<int:pk>/`

GET `/api/product/category/<int:category_id>/products/`

GET `/api/product/all/`

GET `/api/product/brands/get/<int:pk>/`

GET `/api/product/brands/all/`

## Order related endpoints:

POST `/api/order/cart/update/`

GET `/api/order/cart/list/<slug:customer_token>/`

PUT `/api/order/finalize/`

