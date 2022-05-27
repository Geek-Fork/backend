from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt

from .serializers import AnimeSerializer
from .use_cases.anime_list import get_anime_list


@csrf_exempt
@api_view(("POST",))
@permission_classes((AllowAny,))
def anime_test(request: Request) -> Response:
    """
    View function for anime_test page
    """
    serializer = AnimeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response(get_anime_list(), status=status.HTTP_200_OK)
