from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView


class StudentForm(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()


class Student(APIView):

    def get(self, request):
        return Response({
            'status': 200,
            'message': 'Hello student'
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=StudentForm)
    def post(self, request):
        serializer = StudentForm(data=request.data)
        if serializer.is_valid():
            json = serializer.data
            return Response({
                'status': 200,
                'date': json
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'status': 400,
                'date': "null"
            }, status=status.HTTP_400_BAD_REQUEST)
