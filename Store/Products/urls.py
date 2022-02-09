from django.urls import path
from .views import Views

urlpatterns = [
    path('', Views.main_page, name='main-page'),
    path('add/', Views.add_product, name='add-product'),
    path('update/<id>/', Views.update_product, name='upadate-product'),
    path('delete/<id>/', Views.delete_product, name='delete-product'),
]