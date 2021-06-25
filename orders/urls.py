from django.urls import path
from .views import OrderProductsList, OrdersList, update_cart, CartList, OrderFinalize

urlpatterns = [
    path('all/', OrdersList.as_view()),
    path('<int:order_id>/', OrderProductsList.as_view()),
    path('cart/update/', update_cart),
    path('cart/list/<slug:customer_token>/', CartList.as_view()),
    path('finalize/', OrderFinalize.as_view())
]
