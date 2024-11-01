from django.urls import path
from inventory import views
from django.shortcuts import render, redirect

urlpatterns = [
    path('', lambda request: redirect('admin_login')),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/signup/', views.admin_signup, name='admin_signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_supplier/', views.add_supplier, name='add_supplier'),
    path('add_transporter/', views.add_transporter, name='add_transporter'),
    path('edit_transporter/<str:id>/', views.edit_transporter, name='edit_transporter'),  # Add this line
    path('delete_transporter/<str:id>/', views.delete_transporter, name='delete_transporter'),  # Add this line
    path('add_items/', views.add_items, name='add_items'),
    path('view_items/', views.view_items, name='view_items'),
    path('edit_item/<str:id>/', views.edit_item, name='edit_item'),  # Add this line
    path('delete_item/<str:id>/', views.delete_item, name='delete_item'),  # Add this line
    path('logout/', views.logout_view, name='logout'),
    path('populate_items/', views.populate_items, name='populate_items'),
    path('edit_supplier/<str:id>/', views.edit_supplier, name='edit_supplier'),
    path('delete_supplier/<str:id>/', views.delete_supplier, name='delete_supplier'),
]
