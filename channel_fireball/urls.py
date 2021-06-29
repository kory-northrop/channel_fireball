"""
URLs for channel_fireball.
"""
from django.conf.urls import url  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    url(r'', TemplateView.as_view(template_name="channel_fireball/base.html")),
]
