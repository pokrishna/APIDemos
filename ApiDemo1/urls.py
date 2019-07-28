"""ApiDemo1 URL Configuration

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
from django.urls import path, include
from myapp import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register('test-viewset',views.TestViewSet,base_name='test-viewset')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/',views.rhttp),
    # path('api1/',views.rjson),
    # path('api/',include('rest_framework.urls')),
    # path('capi/',views.EmployeeCBV.as_view()),
    #path('api/',views.EmpCBV3.as_view()),
    #path('',views.TestApiView.as_view()),
    #path('',include(router.urls)),
    #path('api/',views.TestAPIView2.as_view()),
    path('api/',views.EmployeeCreateAPIView.as_view()),

]
