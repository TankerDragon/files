
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# models
from .models import Log
# serializers
from .serializers import LogSerializer


@api_view(['GET', 'POST'])
def ping(request):
    if request.method == 'GET':
        return Response(status=status.HTTP_200_OK)

    if request.method == 'POST':
        print(request.data)
        print(request.headers)

        # check if data is more than 255 characters
        if len(request.data["data"]) > 255:
            request.data["data"] = request.data["data"][:255]
            request.data["is_overloaded"] = True


        logSerilizer = LogSerializer(data=request.data)
        if logSerilizer.is_valid():
            logSerilizer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(logSerilizer.errors, status=status.HTTP_400_BAD_REQUEST)
