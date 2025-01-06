from rest_framework import serializers

from ...models import ResumeModel


class BaseResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListResumeSerializer(BaseResumeSerializer):
    class Meta(BaseResumeSerializer.Meta): ...


class RetrieveResumeSerializer(BaseResumeSerializer):
    class Meta(BaseResumeSerializer.Meta): ...


class CreateResumeSerializer(BaseResumeSerializer):
    class Meta(BaseResumeSerializer.Meta): ...
