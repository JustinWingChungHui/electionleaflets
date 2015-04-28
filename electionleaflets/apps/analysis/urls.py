from django.conf.urls import patterns, include, handler500, url
from django.conf import settings
from django.views.decorators.cache import cache_page


from .views import AnalysisHomeView, ReportView, AnalysisStartRedirectView

urlpatterns = patterns(
    '',
    url(r'^/$', AnalysisHomeView.as_view(),
        name='analysis'),
    url(r'^/start$', AnalysisStartRedirectView.as_view(),
        name='analysis_start'),
    url(r'^/reports$', cache_page(60*5)(ReportView.as_view()),
        name='reports'),
)

