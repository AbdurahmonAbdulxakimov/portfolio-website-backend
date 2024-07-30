from django.urls import path
from apps.contents import views


app_name = 'contents'

urlpatterns = [
    path("SiteContentList/", views.SiteContentListView.as_view(), name="site_content_list"),
    path("SiteContentDetail/<str:key>/", views.SiteContentRetriveView.as_view(), name="site_content_detail"),
    path("SkillList/", views.SkillListView.as_view(), name="skill_list"),
    path("Resume/", views.ResumeRetriveView.as_view(), name="resume"),
]