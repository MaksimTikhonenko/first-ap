from django.urls import path
from . import views

urlpatterns = [
    path('healthcheck', views.healthcheck, name='healthcheck'),
    path('product', views.create_product, name='create_product'),
    # path('procuct/<int:product_id>', views.get_product, name='get_product'),
    path('get_product', views.get_product, name='get_product'),
    path('del_prod', views.del_product, name='del_product'),
    path('person', views.create_person, name='create_person'),
    path('get_person', views.get_person, name='get_person'),
]
