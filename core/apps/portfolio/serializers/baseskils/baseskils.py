from rest_framework import serializers

from ...models import BaseskilsModel


class BaseBaseskilsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseskilsModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListBaseskilsSerializer(BaseBaseskilsSerializer):
    class Meta(BaseBaseskilsSerializer.Meta): ...


class RetrieveBaseskilsSerializer(BaseBaseskilsSerializer):
    class Meta(BaseBaseskilsSerializer.Meta): ...


class CreateBaseskilsSerializer(BaseBaseskilsSerializer):
    class Meta(BaseBaseskilsSerializer.Meta): ...
