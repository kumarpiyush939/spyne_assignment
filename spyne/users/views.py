from rest_framework import generics
from .models import SpyneUser as User
from .serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer
    # print(request.method)
    def get_queryset(self):
        name = self.kwargs.get('name')
        if name:
            return User.objects.filter(name__icontains=name)
        else:
            return User.objects.none()
