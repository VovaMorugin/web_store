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



## return 
GET `/api/customer/myorders/`



GET `/api/customer/getuser/`

# Product related endpoints:

## Returns the list of all products categories
GET `/api/product/category/list/`
### Response body:
```json
[
    {
        "id": 2,
        "title": "TVs"
    },
    {
        "id": 3,
        "title": "Cell Phones"
    },
    {
        "id": 4,
        "title": "Video Games"
    },
    {
        "id": 5,
        "title": "Laptops"
    },
    {
        "id": 6,
        "title": "Appliances"
    }
]
```



## Returns product category by id

GET `/api/product/category/get/<int:pk>/`

### Response body for /api/product/category/get/2/:
```json
{
    "title": "TVs",
    "is_active": true
}
```


## Returns product info by id
GET `/api/product/get/<int:pk>/`
### Response body for /api/product/get/5/:
```json
{
    "id": 5,
    "title": "Cell phone with 5G",
    "price": "399.00",
    "old_price": null,
    "quantity": 1,
    "photo": "http://127.0.0.1:8000/media/images/no_photo.jpg",
    "brand": {
        "id": 4,
        "title": "Fake Electronics"
    },
    "description": "so much wow",
    "reviews": []
}
```

## Returns the list of all product from certain category
If there are more than 9 items in the chosen category - pagenation will apply and "Links" will contain information about previous and next page.
GET `/api/product/category/2/products/`
### Response body for /api/product/category/products/:
```json
{
    "links": {
        "next": null,
        "previous": null,
        "next_num_page": null,
        "previous_num_page": null
    },
    "page": 1,
    "pages": 1,
    "count": 2,
    "result": [
        {
            "id": 3,
            "title": "42 inch TV",
            "price": "300.00",
            "old_price": null,
            "photo": "http://127.0.0.1:8000/media/images/no_photo.jpg",
            "brand": {
                "id": 2,
                "title": "Supertech"
            }
        },
        {
            "id": 4,
            "title": "60 inch TV",
            "price": "450.00",
            "old_price": null,
            "photo": "http://127.0.0.1:8000/media/images/no_photo.jpg",
            "brand": {
                "id": 2,
                "title": "Supertech"
            }
        }
    ]
}
```

## Returns the list off all products with pagination
GET `/api/product/all/`
### Response body:
```json
{
    "links": {
        "next": null,
        "previous": null,
        "next_num_page": null,
        "previous_num_page": null
    },
    "page": 1,
    "pages": 1,
    "count": 5,
    "result": [
        {
            "id": 3,
            "title": "42 inch TV",
            "price": "300.00",
            "old_price": null,
            "photo": "http://127.0.0.1:8000/media/images/no_photo.jpg",
            "brand": {
                "id": 2,
                "title": "Supertech"
            }
        },
        {
            "id": 4,
            "title": "60 inch TV",
            "price": "450.00",
            "old_price": null,
            "photo": "http://127.0.0.1:8000/media/images/no_photo.jpg",
            "brand": {
                "id": 2,
                "title": "Supertech"
            }
        },
        {
            "id": 5,
            "title": "Cell phone with 5G",
            "price": "399.00",
            "old_price": null,
            "photo": "http://127.0.0.1:8000/media/images/no_photo.jpg",
            "brand": {
                "id": 4,
                "title": "Fake Electronics"
            }
        },
        {
            "id": 6,
            "title": "Laptop for the BOSS",
            "price": "999.00",
            "old_price": null,
            "photo": "http://127.0.0.1:8000/media/images/no_photo.jpg",
            "brand": {
                "id": 5,
                "title": "PH"
            }
        },
        {
            "id": 7,
            "title": "Wine Fridge",
            "price": "199.00",
            "old_price": null,
            "photo": "http://127.0.0.1:8000/media/images/no_photo.jpg",
            "brand": {
                "id": 4,
                "title": "Fake Electronics"
            }
        }
    ]
}
```

GET `/api/product/brands/get/<int:pk>/`

GET `/api/product/brands/all/`

## Order related endpoints:

POST `/api/order/cart/update/`

GET `/api/order/cart/list/<slug:customer_token>/`

PUT `/api/order/finalize/`

