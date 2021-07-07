from django.contrib import admin
from django.conf.urls import url, include

from payments import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.payments_view),
    url(r'^payments/', include('payments.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^board/', include('board.urls')),
]
