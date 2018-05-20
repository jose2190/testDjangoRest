from django.conf.urls import url

from .views import MovieAPIView, MovieRUDView

urlpatterns = [
    url(r'^$', MovieAPIView.as_view(), name='movie-listcreate'),
    url(r'^(?P<pk>\d+)/$', MovieRUDView.as_view(), name='movie-rud')
]
