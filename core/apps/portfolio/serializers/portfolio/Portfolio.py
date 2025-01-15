from rest_framework import serializers

from ...models import PortfolioModel, SkilsModel
from core.apps.portfolio.serializers.portfolio.Skils import BaseSkilsSerializer


class SkilsSerializers(serializers.ModelSerializer):
    class Meta:
        model = SkilsModel
        fields = ['name']

class BasePortfolioSerializer(serializers.ModelSerializer):
    skils = SkilsSerializers(many=True)  

    class Meta:
        model = PortfolioModel
        fields = ['name', 'category', 'skils', 'image', 'description', 'git_url', 'project_url']


class ListPortfolioSerializer(BasePortfolioSerializer):
    class Meta(BasePortfolioSerializer.Meta): ...


class RetrievePortfolioSerializer(BasePortfolioSerializer):
    class Meta(BasePortfolioSerializer.Meta): ...


class CreatePortfolioSerializer(BasePortfolioSerializer):
    class Meta(BasePortfolioSerializer.Meta): ...
