from rest_framework.serializers import ModelSerializer

from catalogue.models import Product


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id', 'title', 'description', 'category', 'manufacturer', 'date_created',
        )
