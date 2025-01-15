from rest_framework import serializers

from ...models import PortfolioModel, SkilsModel, CategoryModel
from core.apps.portfolio.serializers.portfolio.Skils import BaseSkilsSerializer


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['name']
        

class SkilsSerializers(serializers.ModelSerializer):
    class Meta:
        model = SkilsModel
        fields = ['name']


class BasePortfolioSerializer(serializers.ModelSerializer):
    skils = SkilsSerializers(many=True)  
    category = CategorySerializers()  
    

    class Meta:
        model = PortfolioModel
        fields = ['name', 'category', 'skils', 'image', 'description', 'git_url', 'project_url', 'create_at']


class ListPortfolioSerializer(BasePortfolioSerializer):
    class Meta(BasePortfolioSerializer.Meta): ...


class RetrievePortfolioSerializer(BasePortfolioSerializer):
    class Meta(BasePortfolioSerializer.Meta): ...


class CreatePortfolioSerializer(BasePortfolioSerializer):
    class Meta(BasePortfolioSerializer.Meta): ...
