from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', views.home, name='homePage'),
    path('search/', views.search_results, name='search_results'),
    path('search_id/<id>', views.display, name='display'),
    # path('notFound', vi)


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)