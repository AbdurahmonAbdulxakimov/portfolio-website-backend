from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.contents import models, serializers


class SiteContentListView(ListAPIView):
    serializer_class = serializers.SiteContentSerializer
    queryset = models.SiteContent.objects.all()


class SiteContentRetriveView(RetrieveAPIView):
    serializer_class = serializers.SiteContentSerializer
    queryset = models.SiteContent.objects.all()
    lookup_field = "key"


class SkillListView(ListAPIView):
    serializer_class = serializers.SkillSerializer
    queryset = models.Skill.objects.all()


class ResumeRetriveView(RetrieveAPIView):
    serializer_class = serializers.ResumeSerializer
    queryset = models.Resume.objects.all()

    def get_object(self):
        return self.get_queryset().last()