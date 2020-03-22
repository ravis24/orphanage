"""blood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static 
from blood1 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blood/signup',views.signup),
    url(r'^blood/donate/$',views.donate),
    url(r'^blood/contact/$',views.contact),
    url(r'^blood/feedback/$',views.feedback),
    url(r'^blood/tips/$',views.tips),
    url(r'^blood/find/$',views.find),
    url(r'^blood/donar_feedback/$',views.donor_feedback),
    url(r'^blood/apply_volunteer/$',views.apply_v),
    url(r'^blood/success/$',views.success),
    url(r'^blood/childprotection/$',views.childpro),
    url(r'^blood/startnonprofit/$',views.nonprofit),
    url(r'^blood/supporters/$',views.supporter),
    url(r'^blood/life_as_a_volunteer/$',views.life),
    url(r'^blood/donate_goods/$',views.goods),
    url(r'^blood/sponsorship/$',views.sponsor),
    url(r'^blood/mission_statement/$',views.mstatement),


]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

