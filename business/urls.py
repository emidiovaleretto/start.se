from django.urls import path

from . import views


urlpatterns = [
    path('register_business/', views.register_business, name='register_business'),
    path('list_businesses/', views.list_businesses, name='list_businesses'),
    path('<int:id>/', views.business_detail, name='business_detail'),
]
