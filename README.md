<h1>Generic web store back end with REST API</h1>

<h2>Written in Python using the Django REST framework, can be used with any frontend that conforms to the following endpoints:</h2>


## Customer related endpoints:

POST `/api/customer/create/`

POST `/api/customer/registration/`

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

