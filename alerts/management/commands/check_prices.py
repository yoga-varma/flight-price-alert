from django.core.management.base import BaseCommand
from alerts.views import check_price_alerts


class Command(BaseCommand):
    help = "Check flight prices and trigger alerts"

    def handle(self, *args, **kwargs):
        self.stdout.write("Checking flight price alerts...")
        check_price_alerts()
        self.stdout.write(self.style.SUCCESS("Done checking alerts"))