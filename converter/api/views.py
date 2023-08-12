from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ConverterSerializer
from .utils import get_converted_value


@api_view(["GET"])
def get_value(request):
    """Получение данных."""
    serializer = ConverterSerializer(
        data=request.GET,
    )

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data = {
        "result": get_converted_value(serializer.data)
    }
    return Response(data, status=status.HTTP_200_OK)
