from django.contrib import admin
from .models import Booking, Cab ,TaxiRoute, RouteFare


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer_name",
        "phone",
        "trip_type",
        "travel_date",
        "travel_time",
        "passengers",
        "cab_type",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "trip_type",
        "travel_date",
        "created_at",
    )

    search_fields = (
        "customer_name",
        "phone",
        "pickup",
        "dropoff",
        "email",
    )

    readonly_fields = ("created_at",)

    list_editable = ("status",)

    date_hierarchy = "travel_date"

    ordering = ("-created_at",)


@admin.register(Cab)
class CabAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "rate_per_km",
        "is_active",
        "sort_order",
    )

    list_editable = (
        "rate_per_km",
        "is_active",
        "sort_order",
    )

    search_fields = ("name",)

    list_filter = ("is_active",)
    
    
    from django.contrib import admin
from .models import TaxiRoute, RouteFare


class RouteFareInline(admin.TabularInline):
    model = RouteFare
    extra = 1


@admin.register(TaxiRoute)
class TaxiRouteAdmin(admin.ModelAdmin):
    list_display = (
        "destination",
        "origin",
        "distance_km",
        "is_active",
        "sort_order",
    )
    list_editable = ("is_active", "sort_order")
    list_filter = ("is_active", "origin")
    search_fields = ("origin", "destination")
    prepopulated_fields = {"slug": ("origin", "destination")}
    inlines = [RouteFareInline]


@admin.register(RouteFare)
class RouteFareAdmin(admin.ModelAdmin):
    list_display = (
        "route",
        "cab",
        "one_way_fare",
        "round_trip_fare",
    )
    list_filter = ("route", "cab")
    search_fields = ("route__destination", "cab__name")