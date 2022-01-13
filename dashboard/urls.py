from . import views
from django.urls import path

urlpatterns = [
    path('dashboard', views.index,name='dashboard-index'),
    path('staff/', views.staff,name='staff'),
    path('product/', views.product,name='product'),
    path('product/delete/<int:pk>/', views.product_delete,name='product_delete'),
    path('product/update/<int:pk>/', views.product_update,name='product_update'),
    path('staff/details/<int:pk>/', views.staff_details,name='staff_details'),
    path('order/', views.order,name='order'),
]