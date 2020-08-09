from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('reactapp.urls')),
    path('auth/', obtain_jwt_token),
]

urlpatterns = urlpatterns +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
