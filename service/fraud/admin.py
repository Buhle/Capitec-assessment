from django.contrib import admin
from .models import Transaction, FraudAlert


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "amount", "reference", "created_at")
    search_fields = ("user_id", "reference")
    list_filter = ("created_at",)


class FraudAlertAdmin(admin.ModelAdmin):
    list_display = ("id", "transaction", "is_fraudulent", "alert_message", "created_at")
    search_fields = ("transaction__reference", "alert_message")
    list_filter = ("is_fraudulent", "created_at")


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(FraudAlert, FraudAlertAdmin)
