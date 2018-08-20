from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from catalogue.models import Product

from .serializers import ProductSerializer


class ProductMixin:
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductListView(ProductMixin, ListAPIView):
    """
    Returns list of all products in DateBase.
    """


class ProductDetailsView(ProductMixin, RetrieveAPIView):
    """
    Returns product details.
    """


class ProductCreateView(ProductMixin, CreateAPIView):
    """
    Creates new product.
    """


class ProductDeleteView(ProductMixin, DestroyAPIView):
    """
    Deletes product from DateBase.
    """


class BadRequestView(APIView):
    """
    Always returns response with status code 400 - needed for test purposes.
    """

    def get(self, *args, **kwargs):
        return Response(status=HTTP_400_BAD_REQUEST)
