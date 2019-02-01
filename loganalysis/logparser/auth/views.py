from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import permissions, generics
from rest_framework.views import status
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
import jwt


from ..common.base_view import BaseView
from ..serializers import TokenSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(request, username=username, password=password)
        
        if user is not None: 
            login(request, user)

            token = jwt_encode_handler(jwt_payload_handler(user))
            serializer = TokenSerializer(data={
                'token': token
            })

            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)