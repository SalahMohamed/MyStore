from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Product
        fields = ["id", "category", "title", "description",
                  "slug", "regular_price", "product_image"]
