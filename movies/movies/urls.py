from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/person/', include('apps.person.api.urls')),
    url(r'^api/movie/', include('apps.movie.api.urls')),
    url(r'^docs/', include_docs_urls(title='Movie API', public=True))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
