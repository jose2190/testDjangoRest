from django.conf.urls import url

from .views import PersonAPIView, PersonRUDView

urlpatterns = [
    url(r'^$', PersonAPIView.as_view(), name='person-listcreate'),
    url(r'^(?P<pk>\d+)/$', PersonRUDView.as_view(), name='person-rud')
]
