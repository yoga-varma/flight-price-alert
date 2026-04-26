from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail

from .models import Alert, Route, PriceSnapshot
from .serializers import AlertSerializer, RouteSerializer, PriceSnapshotSerializer


def check_price_alerts():
    alerts = Alert.objects.filter(is_active=True)
    print("Total alerts:", alerts.count())

    for alert in alerts:
        print("Checking alert:", alert)

        latest_price = PriceSnapshot.objects.filter(
            route=alert.route
        ).order_by('-fetched_at').first()

        if latest_price:
            print("Latest price:", latest_price.price)

            if latest_price.price <= alert.target_price:
                print(f"ALERT 🚨: Price dropped for {alert.route} to {latest_price.price}")

                send_mail(
                    subject="Flight Price Drop Alert 🚨",
                    message=(
                        f"Good news!\n\n"
                        f"Price for {alert.route} dropped to {latest_price.price}.\n"
                        f"Your target price was {alert.target_price}."
                    ),
                    from_email=None,
                    recipient_list=[alert.user.email],
                    fail_silently=False,
                )
            else:
                print("Price not low enough")
        else:
            print("No price data found")


# ALERT APIs

class CreateAlertView(generics.CreateAPIView):
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListAlertView(generics.ListAPIView):
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Alert.objects.filter(user=self.request.user)


class DeleteAlertView(generics.DestroyAPIView):
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Alert.objects.filter(user=self.request.user)


# ROUTE APIs

class CreateRouteView(generics.CreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class ListRouteView(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


# PRICE SNAPSHOT APIs

class CreatePriceSnapshotView(generics.CreateAPIView):
    queryset = PriceSnapshot.objects.all()
    serializer_class = PriceSnapshotSerializer


class ListPriceSnapshotView(generics.ListAPIView):
    queryset = PriceSnapshot.objects.all()
    serializer_class = PriceSnapshotSerializer