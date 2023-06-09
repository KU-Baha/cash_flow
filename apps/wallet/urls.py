from django.urls import path
from .views import HomePage, AccountListView, AccountCreateView, account_update, account_delete, TransactionView

urlpatterns = [
    path('', HomePage.as_view(), name='index'),

    path('accounts/', AccountListView.as_view(), name='account'),
    path('account-create/', AccountCreateView.as_view(), name='account-create'),
    path('account-update/<int:pk>/', account_update, name='account-update'),
    path('accounts-delete/<int:pk>/', account_delete, name='account-delete'),

    path('transaction/', TransactionView.as_view(), name='transaction'),
]
