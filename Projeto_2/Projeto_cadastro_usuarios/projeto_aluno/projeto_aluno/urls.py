from django.urls import path
from app_aluno import views
urlpatterns = [
    path('',views.home,name='home'),

    path('usuarios/',views.usuarios,name='list_usuarios'),

]
