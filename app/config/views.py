from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView


class HomepageView(APIView):

    parser_classes = [JSONParser]

    def get(self, request, format=None):
        return Response({
            'message': 'hello world'
        })
