"""project_tenant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from tenant import views
from django.conf import settings
from django.conf.urls.static import static
from tenant import admin_urls, agent_urls

urlpatterns = [
    path('admin/', include(admin_urls)),
    path('agent/', include(agent_urls)),
    path('admin/', admin.site.urls),

    path('login/', views.do_login, name='login'),
    path('reset_password', include('password_reset.urls'),
         name='password_reset_recover'),
    re_path('^$', views.index, name='index'),
    re_path('^agent_registration/$', views.agent_registration,
            name='agent_registration'),
    re_path('^tenant/$', views.tenant_index, name='tenant_index'),
    path('tenant/<str:tenant_name>/', views.tenant_details,
         name='tenant_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
