from requests import Response
from rest_framework import  generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.mixins import StaffEditorPermissionMixin
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        email = serializer.validated_data.get('email')
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = title

        serializer.save(content=content)
        # return super().perform_create(serializer)


class ProductDetailAPIView(StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # lookup_field = 'pk'


class ProductUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

        if not instance.content:
            instance.content = instance.title
        # return super().perform_update(serializer)


class ProductDeleteAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    print(lookup_field)

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

# class ProductDetailListAPIView(generics.ListAPIView):
#    queryset = Product.objects.all()
#    serializer_class = ProductSerializer


class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs) 
        return self.list(request, *args, **kwargs)
        

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = 'single time content'
        serializer.save(content=content)


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            # detail view
            #queryset = Product.objects.filter(pk=pk)
            # if not queryset.exist():
            #   raise Http404

            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        else:
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data
            print(data[0])
            return Response(data)

    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)
        # url_args??
