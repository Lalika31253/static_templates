from django.contrib import admin
from django.urls import path, include
from stat_pgs_tmpl import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
   
    path('accounts/', include('accounts.urls')),

    path('home/', views.home),
    path('contact/', views.contact),
    path('about/', views.about),
    path('news/', views.news),
]