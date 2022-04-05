from django.urls import path

from inventory.models import Transactions
from . import views
from .views import PumpCheckout, TransactionAddView, InventorylistView, TransactionsView, UpdateInventory,InventoryDropView, PumpCheckin, PumpStatus

urlpatterns = [
    path('', views.login_user, name="login_user"),
    path('add', TransactionAddView.as_view(), name="transaction_add"),
    path('pumpcheckout', PumpCheckout.as_view(), name="pump_checkout"),
    path('pumpcheckin', PumpCheckin.as_view(), name="pump_checkin"),
    path('pumpstatus', PumpStatus.as_view(), name="pump_status"),
    path('inventory', InventoryDropView.as_view(), name="inventory"),
    path('report', TransactionsView.as_view(), name="report"),
    path('logout', views.logout_user, name="logout_user"),
    path('ajax/manfacture-inventory', views.get_manufacture, name='ajax_manufacture'),
    path('ajax/transactions', views.transactions, name='ajax_transactions' ),
    path('ajax/pumpstatus', views.pumpstatus, name='ajax_pumpstatus' )

    # path('updateinventory', UpdateInventory.as_view(), name="updateinventory"),
    # path('inventory', InventorylistView.as_view(), name='inventory_list'),
    # path('checkout', views.checkout, name="checkout"),
    # path('inventory-autocomplete/<str:item>', InventoryAutoComplete.as_view(), name='inventory_autocomplete'),
]