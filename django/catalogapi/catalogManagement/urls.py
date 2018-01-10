from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # ex: /catalogManagement/category/
    url(r'^category/?$', views.CategoryListView.as_view()),
    # ex: /catalogManagement/category/5/
    url(r'^(category/[a-zA-Z\-]*(?P<pk>[0-9]+))/?$', views.CategoryDetailView.as_view()),
    # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
