# app_name/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('qa/', include('app_name.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path('', views.qa_page, name='qa_page'),
    path('upload_pdf/', views.upload_pdf, name='upload_pdf'),
    path('list_pdfs/<int:floor>/<int:room_number>/<str:section>/', views.list_pdfs, name='list_pdfs'),
]
