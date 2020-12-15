from django.urls import path
from manager_app import views
app_name = 'manager_app'


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]
