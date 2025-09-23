from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path( "",views.index, name='Home'),
    path( "about",views.about, name='about'),
    path('services/', views.services, name='services'),  # General services page
    path('services/<str:service_name>/', views.services, name='service_details'),  # Dynamic service page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('pricing/', views.pricing, name='pricing'),  # Add this line for Pricing page
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
