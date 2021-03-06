from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from psb_learning.users.views import CurrentUserView

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/auth/users/me/", CurrentUserView.as_view()),
    path("api/auth/", include('djoser.urls')),
    path("api/auth/", include('djoser.urls.jwt')),
    path("api/testing", include("psb_learning.testing.urls")),
    path("api/projects", include("psb_learning.projects.urls"))
]

urlpatterns += [
    path('api/schema/',
         SpectacularAPIView.as_view(),
         name='schema'),
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    path('api/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
