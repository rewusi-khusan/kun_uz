from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from news.views import index, categories_view, category_detail, yangilik_view

urlpatterns = [
    path('', index, name='home'),
    path('categories/', categories_view, name='categories_view'),
    path('categories/<int:id>/', category_detail, name='category_detail'),
    path('yangilik/<str:slug>/', yangilik_view, name='new_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)