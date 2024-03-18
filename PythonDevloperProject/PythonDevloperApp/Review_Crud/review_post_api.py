from rest_framework import generics
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from ..serializers import ReviewPostSerializer
from rest_framework.parsers import MultiPartParser

@parser_classes((MultiPartParser,))
class ReviewPostApi(generics.GenericAPIView):
    serializer_class = ReviewPostSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response({
                'message': 'Successful',
                'Result': ReviewPostSerializer(user).data,
                'HasError': False,
                'status': 200
            })
        except Exception as e:
            return Response({
                'message': 'Fail',
                'Result': [],
                'HasError': True,
                'status': 400
            })