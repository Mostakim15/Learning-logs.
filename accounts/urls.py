from django.urls import path, include
from .import views
#define the url pattern for account
app_name = 'accounts'
urlpatterns = [
    #include defoult url path
    path("",include('django.contrib.auth.urls')),
    path('register/', views.register, name="register")

]

