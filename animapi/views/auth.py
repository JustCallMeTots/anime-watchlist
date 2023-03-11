from animapi.models import Watcher
from rest_framework.decorators import api_view
from rest_framework.response import Response
from animapi.serializers import WatcherSerializer


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated Watcher

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

    watcher = Watcher.objects.filter(uid=uid).first()

    if watcher is not None:
        watcher = Watcher.objects.get(uid=uid)
        serializer = WatcherSerializer(watcher)

        return Response(serializer.data)
    else:
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new watcher for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    watcher = Watcher.objects.create(
        bio=request.data['bio'],
        uid=request.data['uid']
    )

    data = {
        'id': watcher.id,
        'uid': watcher.uid,
        'bio': watcher.bio
    }
    return Response(data)