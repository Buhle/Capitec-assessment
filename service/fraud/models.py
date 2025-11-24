from django.db import models


class Transaction(models.Model):
    user_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    reference = models.CharField(max_length=255)

    def __str__(self):
        return f"Transaction of {self.amount} at {self.created_at}"


class FraudAlert(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    is_fraudulent = models.BooleanField(default=False)
    alert_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Fraud Alert for Transaction {self.transaction.id}"
