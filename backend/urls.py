"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('app', views.app_view, name='app'),
    path('admin/', admin.site.urls),
    path('login', LoginView.as_view(), name="login"),
    path('signup', views.signup_view, name="signup"),
    path('logout', LogoutView.as_view(), name="logout")
    # path("accounts/", include("django.contrib.auth.urls")),
]

"""
django.contrib.auth.urls provides

# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']

Django by default will look within a templates folder called registration for auth templates.
The login template is called login.html.

Basically is you want to create templates for those view,
you must do in in templates/registration/



"""
