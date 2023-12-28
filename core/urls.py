"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from sample.views import index
from sample.views import product_detail
from sample.views import search_results

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('product/1/index.html', index, name='index'),
    path('product/2/index.html', index, name='index'),
    path('product/3/index.html', index, name='index'),
    path('product/4/index.html', index, name='index'),
    path('product/5/index.html', index, name='index'),
    path('product/6/index.html', index, name='index'),
    path('product/7/index.html', index, name='index'),
    path('product/8/index.html', index, name='index'),
     path('product/9/index.html', index, name='index'),
      path('product/10/index.html', index, name='index'),
    path('search/', search_results, name='search_results'),
    path('search/index.html', index, name='index'),       
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)





