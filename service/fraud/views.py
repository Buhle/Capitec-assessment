from .models import Transaction, FraudAlert
from .utils import FraudUtils
from .serializers import TransactionSerializer, FraudSerializer
from rest_framework import generics


class TransactionView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        # Save transaction
        transaction = serializer.save()

        # Check for fraud detection
        FraudUtils().is_fraudulent(transaction)


class FraudAlertsView(generics.RetrieveAPIView):
    queryset = FraudAlert.objects.all()
    serializer_class = FraudSerializer
    # lookup_field = "transaction__id"


class FraudAlertListView(generics.ListAPIView):
    queryset = FraudAlert.objects.all()
    serializer_class = FraudSerializer
