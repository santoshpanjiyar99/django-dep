from django.conf.urls import url
from basicapp import views


app_name='basicapp'
urlpatterns=[
    url('register/',views.register,name='register'),
    url('user_login/', views.user_login, name='user_login')

]