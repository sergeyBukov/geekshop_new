from django.urls import path

# from baskets.views import basket_add, basket_remove, basket_edit
from admins.views import index, admin_users, admin_users_create, admin_users_update, admin_users_delete

app_name = 'admins'
urlpatterns = [

    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users-create/', admin_users_create, name='admin_users_create'),
    path('users-update/<int:pk>', admin_users_update, name='admin_users_update'),
    path('admin-delete/<int:pk>', admin_users_delete, name='admin_users_update'),
]
