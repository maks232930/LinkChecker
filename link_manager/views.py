from rest_framework import viewsets

from link_manager.models import Link
from link_manager.serializers import LinkSerializers


class LinkViewSet(viewsets.ModelViewSet):
    """
        API endpoint для управления объектами Link.
        Позволяет выполнять операции CRUD (Create, Retrieve, Update, Delete) над объектами Link.
    """
    queryset = Link.objects.all()
    serializer_class = LinkSerializers
