from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from rest_framework import permissions, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework_jwt.settings import api_settings

from .models import Songs
from .serializers import SongsSerializer, TokenSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

def adminPage(request):
    return render(request, 'logparser/adminpage.html', {})


def logView(request):
    context = {'anyerror': True}
    return render(request, 'logparser/logview.html', context)


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def get_all_song_view(request):
    queryset = Songs.objects.all()
    serializer = SongsSerializer(queryset, many=True)
    return Response(serializer.data)


class LoginView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(request, username=username, password=password)
        
        if user is not None: 
            login(request, user)
            serializer = TokenSerializer(data={
                'token': jwt_encode_handler(jwt_payload_handler(user))
            })
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)