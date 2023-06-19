from django.contrib import admin
from django.urls import include, path
from notes.views import NoteCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('notes/', NoteCreateView.as_view(), name='create_note'),
]
