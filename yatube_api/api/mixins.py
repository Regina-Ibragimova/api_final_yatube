from rest_framework import mixins
from rest_framework import viewsets

class ListCreateMixin(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    """
    Миксин для списка и создания
    """
    pass

