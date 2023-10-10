from rest_framework import serializers

from link_manager.models import Link


class LinkSerializers(serializers.ModelSerializer):
    """
    Сериализатор для модели Link.

    Fields:
    - id (автоматически создается)
    - name (название ссылки)
    - url (URL ссылки)
    - condition_type (тип условия проверки)
    - text (текст для поиска на странице, необязательное поле)
    - is_active (флаг активности ссылки)
    - timestamp (время создания или обновления записи, только для чтения)
    - is_result (результат последней проверки, только для чтения)

    При создании или обновлении объекта Link, поля `timestamp` и `is_result`
    автоматически заполняются и являются только для чтения.
    """

    class Meta:
        model = Link
        read_only_fields = ('timestamp', 'is_result')
        fields = '__all__'
