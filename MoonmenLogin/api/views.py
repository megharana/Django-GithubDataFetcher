from rest_framework.generics import ListAPIView
from rest_framework import viewsets

from MoonmenLogin.models import User
from .serializers import PostSerializer,UserSerializer
class PostListAPIView(ListAPIView):

	queryset=User.objects.all()
	serializer_class=PostSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset=User.objects.all()
	serializer_class=UserSerializer