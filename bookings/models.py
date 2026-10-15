from django.db import models
from django.utils.text import slugify

class Booking(models.Model):
    TRIP_CHOICES = [
        ("local", "Local / Within City"),
        ("airport", "Airport Transfer"),
        ("outstation", "Outstation"),
        ("oneway", "One-way"),
        ("roundtrip", "Round Trip"),
    ]
    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("confirmed", "Confirmed"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]
    customer_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    trip_type = models.CharField(max_length=20, choices=TRIP_CHOICES)
    pickup = models.CharField(max_length=255)
    dropoff = models.CharField(max_length=255)
    travel_date = models.DateField()
    travel_time = models.TimeField()
    passengers = models.PositiveSmallIntegerField(default=1)
    cab_type = models.CharField(max_length=80, blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.customer_name} — {self.travel_date} ({self.get_status_display()})"
class Cab(models.Model):

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cabs/")
    rate_per_km = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name
    
    
    from django.db import models
from django.utils.text import slugify


class TaxiRoute(models.Model):
    origin = models.CharField(max_length=100, default="Delhi")
    destination = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    distance_km = models.PositiveIntegerField(default=0)
    estimated_time = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="routes/",
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "destination"]
        verbose_name = "Taxi Route"
        verbose_name_plural = "Taxi Routes"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                f"{self.origin}-to-{self.destination}"
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.origin} to {self.destination}"


class RouteFare(models.Model):
    route = models.ForeignKey(
        TaxiRoute,
        on_delete=models.CASCADE,
        related_name="fares"
    )
    cab = models.ForeignKey(
        "Cab",
        on_delete=models.PROTECT,
        related_name="route_fares"
    )
    capacity = models.CharField(max_length=50, blank=True)
    one_way_fare = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    round_trip_fare = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    includes = models.CharField(max_length=255, blank=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "cab__name"]
        unique_together = ("route", "cab")

    def __str__(self):
        return f"{self.route} - {self.cab.name}"