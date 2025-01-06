from rest_framework import serializers

from ...models import SkilsModel


class BaseSkilsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkilsModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListSkilsSerializer(BaseSkilsSerializer):
    class Meta(BaseSkilsSerializer.Meta): ...


class RetrieveSkilsSerializer(BaseSkilsSerializer):
    class Meta(BaseSkilsSerializer.Meta): ...


class CreateSkilsSerializer(BaseSkilsSerializer):
    class Meta(BaseSkilsSerializer.Meta): ...
