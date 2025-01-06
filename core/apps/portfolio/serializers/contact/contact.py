from rest_framework import serializers

from ...models import ContactModel


class BaseContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListContactSerializer(BaseContactSerializer):
    class Meta(BaseContactSerializer.Meta): ...


class RetrieveContactSerializer(BaseContactSerializer):
    class Meta(BaseContactSerializer.Meta): ...


class CreateContactSerializer(BaseContactSerializer):
    class Meta(BaseContactSerializer.Meta): ...
