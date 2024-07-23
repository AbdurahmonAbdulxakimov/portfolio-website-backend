from rest_framework import serializers

from apps.contents.models import SiteContent, Skill, Resume


class SiteContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteContent
        fields = ('key', 'value')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('title',)


class ResumeSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = Resume
        fields = (
            'id',
            'file',
            'updated_at',
            'created_at',
        )

    def get_file(self, obj):
        req = self.context.get('request')
        if req:
            return req.build_absolute_uri(obj.file.url)
        return obj.file.url