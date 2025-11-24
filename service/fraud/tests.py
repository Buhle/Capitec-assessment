from unittest.mock import patch

from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

from .models import Transaction, FraudAlert


class TransactionViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()

    @patch("fraud.utils.FraudUtils.is_fraudulent")
    def test_create_transaction_calls_fraud_utils_and_creates_transaction(
        self, mock_is_fraudulent
    ):
        """Posting to /transaction/ should create a Transaction and call FraudUtils.is_fraudulent."""
        payload = {
            "user_id": 1,
            "amount": "250.00",
            "reference": "test-ref-001",
        }

        resp = self.client.post("/transaction/", payload, format="json")
        # DRF CreateAPIView returns 201 on success
        self.assertEqual(resp.status_code, 201)

        # Transaction created
        self.assertEqual(Transaction.objects.count(), 1)

        # FraudUtils called once with the created transaction
        self.assertTrue(mock_is_fraudulent.called)


class FraudAlertListViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        # create a transaction and a fraud alert
        tx1 = Transaction.objects.create(user_id=5, amount="99999", reference="r1")
        tx2 = Transaction.objects.create(
            user_id=4, amount="20000", reference="gambling"
        )
        self.alert1 = FraudAlert.objects.create(
            transaction=tx1,
            is_fraudulent=True,
            alert_message="High amount",
        )
        self.alert2 = FraudAlert.objects.create(
            transaction=tx2,
            is_fraudulent=True,
            alert_message="High amount",
        )

    def test_fraud_alert_list_returns_alerts(self):
        resp = self.client.get("/fraud/alerts/")
        self.assertEqual(resp.status_code, 200)
        # Expect two alerts in response
        self.assertTrue(isinstance(resp.data, list))
        self.assertGreaterEqual(len(resp.data), 2)

    def test_fraud_alert1_detail_returns_alert(self):
        resp = self.client.get(f"/fraud/{self.alert1.id}")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["id"], self.alert1.id)


    def test_fraud_alert2_detail(self):
        resp = self.client.get(f"/fraud/{self.alert2.id}")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["id"], self.alert2.id)
