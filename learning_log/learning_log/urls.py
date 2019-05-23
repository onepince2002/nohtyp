"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
#需參照下列網站修改
#https://blog.csdn.net/m0_38059875/article/details/82793269
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
#    ]

from django.contrib import admin
from django.conf.urls import include, url


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 以下為新增程式碼
    url(r'', include(('learning_logs.urls','appname'), namespace='learning_logs')), # 這行程式碼包含有namespace引數讓我們能將learning_logs的URL和專案中的其他URL區分開來
    # url(r'', include('learning_logs.urls')), # 或者修改为include(pattern_list)这种用法也是可以的！！！

]
