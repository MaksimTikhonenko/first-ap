from django.urls import path
from . import views

urlpatterns = [
    path('healthcheck', views.healthcheck, name='healthcheck'),
    # path('product', views.create_product, name='create_product'),
    # path('procuct/<int:student_id>', views.get_product, name='get_product'),
    # path('product', views.get_product, name='get_product'),
]
