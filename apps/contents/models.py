from django.db import models
from ckeditor.fields import RichTextField
from apps.common.models import BaseModel


class SiteContent(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = 'Site Content'
        verbose_name_plural = 'Site Contents'


class Resume(BaseModel):
    file = models.FileField(upload_to='resumes', max_length=255)


class Skill(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title