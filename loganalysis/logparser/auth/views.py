from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import permissions, generics
from rest_framework.views import status
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from ..common.base_view import BaseView
from ..serializers import TokenSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def signup(request):
    user = User.objects.create_user(username=request.data['username'], email=request.data['email'], password=request.data['password'])
    if user is not None: 
        user.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
    
