from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from .serializers import ShortUserSerializer


class CurrentUserView(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = ShortUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
