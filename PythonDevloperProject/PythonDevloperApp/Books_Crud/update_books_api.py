from rest_framework import generics
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from ..serializers import BookPostSerializer
from ..models import BooksModel


class BooksUpdate(generics.GenericAPIView):
    serializer_class = BookPostSerializer

    def put(self, request, *args,id):
        try:
            userdata = BooksModel.objects.get(id=id)

            s = BookPostSerializer(userdata, data=request.data)
            s.is_valid(raise_exception=True)
            s.save()

            return Response({
                'message': 'Successful',
                'Result': True,
                'HasError': False,
                'status': 200
            })
        except BooksModel.DoesNotExist as e:
            return Response({
                'message': 'Not Updated',
                'Result':False,
                'HasError': True,
                'status': 400
            })