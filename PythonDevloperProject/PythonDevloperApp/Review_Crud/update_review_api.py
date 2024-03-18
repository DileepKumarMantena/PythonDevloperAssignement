from rest_framework import generics
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from ..serializers import ReviewPostSerializer
from ..models import ReviewModel


class ReviewUpdateApi(generics.GenericAPIView):
    serializer_class = ReviewPostSerializer

    def put(self, request, *args,id):
        try:
            userdata = ReviewModel.objects.get(id=id)

            s = ReviewPostSerializer(userdata, data=request.data)
            s.is_valid(raise_exception=True)
            s.save()

            return Response({
                'message': 'Successful',
                'Result': True,
                'HasError': False,
                'status': 200
            })
        except ReviewModel.DoesNotExist as e:
            return Response({
                'message': 'Not Updated',
                'Result':False,
                'HasError': True,
                'status': 400
            })