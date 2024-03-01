from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import CategorySerializer
from ..models import Category


class CategoryViewSet(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
