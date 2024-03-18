from rest_framework import generics
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from ..serializers import ReviewGetSerializer
from ..models import ReviewModel

from rest_framework.parsers import MultiPartParser

@parser_classes((MultiPartParser,))
class ReviewGetApi(generics.GenericAPIView):
    serializer_class = ReviewGetSerializer

    def get(self, request, *args, **kwargs):
        try:
            data = ReviewModel.objects.all()
            serializer_class = ReviewGetSerializer(data, many=True)
            return Response({'Message': 'Successful',
                             'Result': serializer_class.data,
                             'HasError': False,
                             'Status': 200})

        except Exception as e:
            return Response({'Message': 'Fail',
                             'Result': [],
                             'HasError': True,
                             'Status': 400})