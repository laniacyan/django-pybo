from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    # url은 common/login/ 이 된다.
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]

