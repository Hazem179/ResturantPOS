from django.urls import path
from . import views



app_name = 'core'
urlpatterns = [
path('', views.home, name='home'),
path('categories/', views.categories, name='categories'),
path('products/', views.products, name='products'),
]
 