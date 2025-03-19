from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path("", views.home, name = "home"),
    path("upload/", views.uploadPdf, name = 'upload_pdf'),
    path("about/", views.about, name = 'about'),
    path("future/", views.future, name = 'future')
]

