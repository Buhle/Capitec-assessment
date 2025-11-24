from rest_framework import serializers
from .models import Transaction, FraudAlert


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class FraudSerializer(serializers.ModelSerializer):
    transaction_id = serializers.CharField(read_only=True)

    class Meta:
        model = FraudAlert
        fields = "__all__"
