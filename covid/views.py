from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import get_csv_data, add_csv_data, update_csv_data, delete_csv_data
from .serializers import CovidDataSerializer
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema, OpenApiParameter


class CovidDataAPIView(APIView):
    pagination_class = PageNumberPagination

    @extend_schema(
        parameters=[
            OpenApiParameter('id', int, OpenApiParameter.QUERY, description='ID of the data to retrieve'),
            OpenApiParameter('key_column', str, OpenApiParameter.QUERY, description='Column to filter data on'),
            OpenApiParameter('key_value', str, OpenApiParameter.QUERY, description='Value to filter data on')
        ],
        responses={200: CovidDataSerializer(many=True)},
    )

    def get(self, request, id=None, key_column=None, key_value=None):
        try:
            data = get_csv_data()
            
            if id:
                instance = next((item for item in data if item['id'] == id), None)
                if instance:
                    serializer = CovidDataSerializer(instance)
                    return Response(serializer.data)
                return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
            
            elif key_column and key_value:
                if key_column == 'id':
                    key_value = int(key_value)
                filtered_data = [item for item in data if item.get(key_column) == key_value]
            else:
                filtered_data = data

            paginator = self.pagination_class()
            paginated_data = paginator.paginate_queryset(filtered_data, request)
            serializer = CovidDataSerializer(paginated_data, many=True)
            return paginator.get_paginated_response(serializer.data)
        
        except Exception as e:
            print(f"Exception: {str(e)}")
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        try:
            new_data = request.data
            df = add_csv_data(new_data)
            serializer = CovidDataSerializer(new_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        try:
            updated_data = request.data
            updated_data['id'] = id
            df = update_csv_data(updated_data)
            return Response(updated_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            df = delete_csv_data(id, key_column='id')
            return Response({'detail': 'object deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
