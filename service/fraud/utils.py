from .models import Transaction, FraudAlert
from django.conf import settings


class FraudUtils:
    def is_fraudulent(self, transaction: Transaction) -> FraudAlert:
        is_fraud = transaction.amount > settings.FRAUD_MAX_AMOUNT
        alert_message = (
            "Transaction exceeds maximum allowed amount."
            if is_fraud
            else "No fraud detected."
        )

        fraud_alert, created = FraudAlert.objects.update_or_create(
            transaction=transaction, is_fraudulent=is_fraud, alert_message=alert_message
        )

        return fraud_alert
