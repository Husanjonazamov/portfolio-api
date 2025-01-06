from rest_framework import serializers

from ...models import PortfolioModel


class BasePortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListPortfolioSerializer(BasePortfolioSerializer):
    class Meta(BasePortfolioSerializer.Meta): ...


class RetrievePortfolioSerializer(BasePortfolioSerializer):
    class Meta(BasePortfolioSerializer.Meta): ...


class CreatePortfolioSerializer(BasePortfolioSerializer):
    class Meta(BasePortfolioSerializer.Meta): ...
