from django.urls import path
from .views import OrderProductsList, OrdersList

urlpatterns = [
    path('all/', OrdersList.as_view()),
    path('<int:order_id>/', OrderProductsList.as_view())
]
