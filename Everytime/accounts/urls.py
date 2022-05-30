from django.urls import path
from accounts import views as accounts
urlpatterns = [
    path('login/', accounts.login, name='login'),
    path('register/', accounts.register, name='register'),
    path('logout/', accounts.logout, name='logout')
]
