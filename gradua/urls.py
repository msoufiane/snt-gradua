from django.views.generic import TemplateView
from django.conf.urls import include, url
from graphene_django.views import GraphQLView
import os

urlpatterns = [
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
    url(r'^', TemplateView.as_view(template_name="index.html")),
]

if os.environ.get('DJANGO_ENV', 'dev') == 'dev':
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
