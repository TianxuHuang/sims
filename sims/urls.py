"""
URL configuration for sims project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# 导入必要的模块
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from student import views

# URL 路由配置列表
urlpatterns = [
    # 管理后台 URL
    path('admin/', admin.site.urls),
    # 默认首页 - 显示学生列表
    path('', views.list_student, name='home'),
    # 学生应用的 URL 路由
    path('student/', include('student.urls')),
    # 班级应用的 URL 路由
    path('classes/', include('classes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 静态媒体文件 URL 配置
