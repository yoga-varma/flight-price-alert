from celery import shared_task
from alerts.views import check_price_alerts

@shared_task
def check_price_alerts_task():
    print("Checking flight price alerts...")
    check_price_alerts()
    print("Done checking alerts")