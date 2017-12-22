import django_filters.rest_framework
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status, generics
from rest_framework.response import Response
from catalogManagement.models import Category
from catalogManagement.serializers import CategorySerializer


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('href', 'version', 'lastUpdate', 'name', 'description', 'lifecycleStatus',
                     'parentId', 'isRoot', 'validFor', )

    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print("request data in post:\n{}".format(request.data))
        serializer = CategorySerializer(data=request.data)
        print("serializer dict:\n{}".format(serializer.__dict__))
        print("initial data in serializer:\n{}".format(serializer.initial_data))
        if serializer.is_valid(serializer.initial_data):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(APIView):
    def get_object(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_id, format=None):
        category = Category.objects.get(id=category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, category_id, format=None):
        category = Category.objects.get(id=category_id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
