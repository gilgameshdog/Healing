from rest_framework.response import Response
from .serializers import CategoriaSerializer
from rest_framework.views import APIView
from rest_framework import status


class CategoriaAPI(APIView):
    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            categoria = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
