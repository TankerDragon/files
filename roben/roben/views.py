from os import stat
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def ping(request):
    if request.method == 'GET':
        return Response(status=status.HTTP_200_OK)

    if request.method == 'POST':
        print(request.data)
        print(request.headers)
        return Response(status=status.HTTP_200_OK)
