from django.contrib.auth import login
from django.urls import path
from myapp.views import add_show, delete_data, update_view, sign_up, user_login

urlpatterns =[
path('', add_show, name='add_show'),
path('update/<int:id>/', update_view, name='updateview' ),
path('delete/<int:id>/', delete_data, name='deletedata'),
path('signup/', sign_up, name='signup'),
path('login/', user_login, name='login'),

 ]
