# ToDO: lista terminw "todo" do odchaczania w ramach danego msc / opcja zamknij miesic
# todo: dodawanie wydatków w kategoriach + faktury
# todo: przeglądanie historii wydatków
# todo: filtrowanie wydatków - domyślnie po year/mth, możliwość zmiany (poprzedni, następny)
# todo: add no payment documents like hour reports, my invoices ect

from django.conf.urls import url

from . import views

app_name = "payments"

urlpatterns = [
    url(r'^$', views.payments_view, name='payments'),
    url(r'^admin/', views.go_admin, name="go-admin"),
    url(r'^tasks/', views.tasks_view, name='tasks'),
    url(r'^download/', views.download, name='download'),
]
