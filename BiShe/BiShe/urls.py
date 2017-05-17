"""BiShe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from FinancialVirtualization import views as show_views
import sys
reload(sys)
sys.setdefaultencoding('utf8')

urlpatterns = [
    url(r'^$', show_views.home, name = 'home'),
    url(r'^index.html', show_views.home, name='home'),
    url(r'^introduction/index.html', show_views.home, name='home'),
    url(r'^login.html', show_views.login, name='login'),
    url(r'^register.html', show_views.register, name='register'),
    url(r'^contact.html', show_views.contact, name='contact'),
    url(r'^baidumap.html', show_views.baidumap, name='baidumap'),
    url(r'^introduction/login.html', show_views.login, name='login'),
    url(r'^introduction/register.html', show_views.register, name='register'),
    url(r'^introduction/contact.html', show_views.contact, name='contact'),
    url(r'^introduction/baidumap.html', show_views.baidumap, name='baidumap'),

    url(r'^function/query_stock.html', show_views.default_highstocks,name='defalut_highstocks'),
    url(r'^search', show_views.search_stock, name='search_stock'),
    url(r'^404.html', show_views.wrong, name='wrong'),
    url(r'^admin/', admin.site.urls),
]