from django.urls import path
# from inventory.views import InventoryAutComplete
from . import views
from .views import TransactionAddView, InventorylistView

urlpatterns = [
    path('', views.login_user, name="login_user"),
    path('add', TransactionAddView.as_view(), name="transaction_add"),
    path('inventory', InventorylistView.as_view(), name='inventory_list'),
    path('checkout', views.checkout, name="checkout"),
    path('report', views.report, name="report"),
    path('reportform', views.report, name="reportform"),
    path('logout', views.logout_user, name="logout_user"),
    # path('autocomplete', InventoryAutComplete.as_view(),name='autocomplete')
]