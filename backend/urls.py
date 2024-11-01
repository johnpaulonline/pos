from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ItemListCreateView, ItemDetailView, MenuCategoryListCreateView, MenuCategoryDetailView

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('categories/', MenuCategoryListCreateView.as_view(), name='menu-category-list-create'),
    path('categories/<int:pk>/', MenuCategoryDetailView.as_view(), name='menu-category-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
