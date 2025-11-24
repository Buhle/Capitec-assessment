from django.urls import path
from .views import TransactionView, FraudAlertsView, FraudAlertListView

urlpatterns = [
    path("transaction/", TransactionView.as_view(), name="create-transaction"),
    path("fraud/<int:pk>", FraudAlertsView.as_view(), name="Fraud-alert-detail"),
    path("fraud/alerts/", FraudAlertListView.as_view(), name="fraud-alert-list"),
]
