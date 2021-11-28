
from django.urls import path

from baskets.views import basket_add

app_name = 'baskets'
urlpatterns = [

    path('add/', basket_add, name='basket_add'),

]



