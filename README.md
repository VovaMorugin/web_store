<h1>Generic web store back end with REST API</h1>

<h2>Written in Python using the Django REST framework, can be used with any frontend that conforms to the following endpoints:</h2>

# Contents
* [Customer related endpoints](#customer-related-endpoints)
* [Product related endpoints](#product-related-endpoints)
* [Order related endpoints](#order-related-endpoints)

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



## return order by list to current authorized user, must pass JWT token in request
GET `/api/customer/myorders/`
### Response body:
```json 
[
    {
        "id": 2,
        "is_ordered": true,
        "time_created": "2021-08-05T19:53:39.987909Z",
        "time_checkout": "2021-08-05T20:06:48.502872Z",
        "time_delivery": null,
        "products": [
            {
                "order_id": 2,
                "product_id": 5,
                "price": "399.00",
                "quantity": 3,
                "product": "Cell phone with 5G"
            },
            {
                "order_id": 2,
                "product_id": 3,
                "price": "300.00",
                "quantity": 1,
                "product": "42 inch TV"
            }
        ]
    }
]
```

## return current authorized user data, could be used in order finalization as default values for order check out form. JWT token must be passed in request
GET `/api/customer/getuser/`
### Response body:
```json
{
    "id": 4,
    "first_name": "Volodymyr",
    "last_name": "Moruhin",
    "phone": null,
    "email": "vova.morugin@gmail.com",
    "time_created": "2021-08-05T18:32:52.014145Z",
    "token": "395bce87-0edd-4834-9063-a36311e2f81f",
    "user": 15
}
```


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

## Returns the list of all products with pagination
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
## Returns the list of items by brand id
GET `/api/product/brands/get/<int:pk>/`
### Response body for /api/product/brands/get/2/:
```json
{
    "id": 2,
    "title": "Supertech",
    "products": [
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
## Returns the list all available brands:
GET `/api/product/brands/all/`
### Response body:

```json
[
    {
        "id": 2,
        "title": "Supertech"
    },
    {
        "id": 4,
        "title": "Fake Electronics"
    },
    {
        "id": 5,
        "title": "PH"
    }
]
```


## Order related endpoints:
## Updates the cart:
"cart_items_count" shows number of unique items in the cart
POST `/api/order/cart/update/`
### Request body:

```json
{
    "token": "395bce87-0edd-4834-9063-a36311e2f81f",
    "product_id": 5,
    "quantity": 3
}
```

### Response body:

```json
{
  "status": true, 
  "cart_items_count": 1}
}
```

## Returns list of items in the cart:
GET `/api/order/cart/list/<customer_token>/`
### Response body for /api/order/cart/list/395bce87-0edd-4834-9063-a36311e2f81f/:

```json
[
    {
        "id": 2,
        "price": "399.00",
        "quantity": 3,
        "order": 2,
        "product": 5
    },
    {
        "id": 3,
        "price": "300.00",
        "quantity": 1,
        "order": 2,
        "product": 3
    }
]
```
## Place an order
PUT `/api/order/finalize/`

### Request body:

```json
{
    "token": "395bce87-0edd-4834-9063-a36311e2f81f",
    "first_name": "Volodymyr",
    "last_name": "Moruhin",
    "email": "vova.morugin@gmail.com",
    "country": "USA",
    "city":"Beverly Hills, CA",
    "post_code":"90210",
    "address":"123 Drive"
}
```

### Response body:

```json
{
    "id": 2,
    "time_created": "2021-08-05T19:53:39.987909Z",
    "time_checkout": "2021-08-05T20:06:48.502872Z",
    "time_delivery": null,
    "is_ordered": true,
    "customer": 4,
    "customer_shipping_address": 2
}
```
