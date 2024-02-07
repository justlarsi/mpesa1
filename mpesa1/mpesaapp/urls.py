from django.urls import path

from mpesaapp import views


app_name = "mpesaapp"

urlpatterns = [
    path('', views.home, name="home"),
    path('token', views.token, name='token'),
    path('pay', views.pay, name='pay'),
    path('mpesaapp', views.mpesaapp, name="mpesaapp")

]