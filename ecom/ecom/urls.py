from . import settings
from django.conf.urls.static import static # для добавление статических файлов картинко стилей и так далее
from django.contrib import admin
from django.urls import path, include #позволяет определить вложенные маршруты или подмаршруты для некоторого маршрута.
# В качестве параметра она принимает набор маршрутов include(pattern_list)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')), # включает url которые в store
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # добавление статических файлов
