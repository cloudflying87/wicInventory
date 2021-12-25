from django.urls import path
# from inventory.views import InventoryAutComplete
from . import views

urlpatterns = [
    
    path('', views.login_user, name="login_user"),
    path('checkout', views.checkout, name="checkout"),
    path('report', views.report, name="report"),
    path('logout', views.logout_user, name="logout_user"),
    # path('autocomplete', InventoryAutComplete.as_view(),name='autocomplete')
]