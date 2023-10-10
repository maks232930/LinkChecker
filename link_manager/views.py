from django_celery_beat.models import IntervalSchedule, PeriodicTask
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from link_manager.models import Link
from link_manager.serializers import LinkSerializers


class LinkViewSet(viewsets.ModelViewSet):
    """
        API endpoint для управления объектами Link.
        Позволяет выполнять операции CRUD (Create, Retrieve, Update, Delete) над объектами Link.
    """
    queryset = Link.objects.all()
    serializer_class = LinkSerializers

    def perform_create(self, serializer):
        """
            При создании новой ссылки автоматически создается задача LinkChecker для ее проверки.
        """
        existing_task = PeriodicTask.objects.filter(name="LinkChecker").first()

        if not existing_task:
            schedule, created = IntervalSchedule.objects.get_or_create(
                every=180,
                period=IntervalSchedule.SECONDS
            )

            PeriodicTask.objects.create(
                name='LinkChecker',
                task='link_manager.tasks.main_task',
                interval=schedule,
            )

        link = serializer.save()

        return link


@api_view(['PATCH'])
def deactivate_link(request, pk):
    """
        Приостановить или возобновить выполнение задачи LinkChecker для конкретной ссылки.
    """
    if request.method == 'PATCH':
        link = Link.objects.filter(id=pk).first()
        if link:
            link.is_active = not link.is_active
            link.save()

            return Response({'detail': f'Ваша задача: {link.is_active}'}, status=status.HTTP_200_OK)

    return Response({'detail': 'Нет ссылки.'}, status=status.HTTP_404_NOT_FOUND)
