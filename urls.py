"""mysite URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from polls import views
from polls.views import Message
# app_name = 'users'

urlpatterns = [
    path('',views.example,name='example'),
    path('hello_world/',views.hello_world,name='hello_world'),

    path('admin/', admin.site.urls),
    path('',views.function,),
    path('user_id/<int:id>',views.getting_id,name='user_id'),
    path('get_template/',views.index,name='get_template'),
    path('page_not_found/<int:question_id>',views.page_not_found,name='page_not_found'),
    path('detail/<int:question_id>',views.detail,name='detail'),
    path('message/',Message.as_view(),name="message"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)