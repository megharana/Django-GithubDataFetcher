from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from MoonmenLogin import views
from rest_framework import routers
from MoonmenLogin.api import views as views2


router = routers.DefaultRouter()
router.register(r'user', views2.UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
   
    url(r'auth/social/', views.home, name='auth-social'), #for welcome page
    url(r'auth-social/', include('social_django.urls',namespace='social')),
	url(r'accounts/profile/', views.searchUser, name='getName'), #for searching page
	url(r'^auth/posts/',include(("MoonmenLogin.api.urls",'MoonmenLogin'),namespace='posts-api')),
	url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
	

]
