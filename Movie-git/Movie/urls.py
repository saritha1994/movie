"""
URL configuration for Movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app1 import views
from django.conf.urls.static import static
from django.conf import settings
app_name='movieapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name='home'),
    # path('add', views.add, name='add'),
    # path('detail/<int:p>', views.detail, name='detail'),
    # path('delete/<int:p>', views.delete, name='delete'),
    # path('edit/<int:p>', views.edit, name='edit'),

    path('',views.HomeView.as_view(),name="home"),
    path('movie/<int:pk>/', views.MovieDetail.as_view(), name='detail'),
    path('add', views.AddMovie.as_view(), name='add'),
    path('edit/<int:pk>', views.MovieUpdate.as_view(), name='edit'),
    path('delete/<int:pk>', views.MovieDelete.as_view(), name='delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
