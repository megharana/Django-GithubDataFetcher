"""DjangoGithubDataFetcher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls import include
from MoonmenLogin import views
from rest_framework import routers
from MoonmenLogin.api import views as views2
# from social_django.urls import extra
# from login.views import complete

router = routers.DefaultRouter()
router.register(r'user', views2.UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
   # url(r'^login/', include('MoonmenLogin.urls')),
   
    url(r'auth/social/', views.home, name='auth-social'), #for welcome page
    url(r'auth-social/', include('social_django.urls',namespace='social')),
	url(r'accounts/profile/', views.searchUser, name='getName'), #for searching page
	url(r'^auth/posts/',include(("MoonmenLogin.api.urls",'MoonmenLogin'),namespace='posts-api')),
	url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
	

]
