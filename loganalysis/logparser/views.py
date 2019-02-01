from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Songs
from .serializers import SongsSerializer

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


