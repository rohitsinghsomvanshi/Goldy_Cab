from urllib.parse import quote

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import BookingForm
from .models import Cab, TaxiRoute

BUSINESS_PHONE = "6307542965"
BUSINESS_EMAIL = "goldycabservices@gmail.com"


def home(request):
    form = BookingForm()

    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            # Check mandatory Terms & Conditions checkbox
            if request.POST.get("terms") != "on":
                messages.error(
                    request,
                    "Please accept the Terms & Conditions before booking."
                )
            else:
                # Save booking only after terms are accepted
                booking = form.save()

                summary = (
                    f"Hello GOLDY CAB SERVICES, I submitted an online booking. "
                    f"Booking ID: {booking.pk}; "
                    f"Name: {booking.customer_name}; "
                    f"Phone: {booking.phone}; "
                    f"Trip: {booking.get_trip_type_display()}; "
                    f"Pickup: {booking.pickup}; "
                    f"Drop: {booking.dropoff}; "
                    f"Date: {booking.travel_date}; "
                    f"Time: {booking.travel_time}; "
                    f"Passengers: {booking.passengers}; "
                    f"Cab: {booking.cab_type or 'Not specified'}."
                )

                whatsapp_url = (
    f"https://wa.me/91{BUSINESS_PHONE}"
    f"?text={quote(summary)}"
)

                request.session["booking_id"] = booking.pk

                return redirect(whatsapp_url)

        else:
            messages.error(
                request,
                "Please correct the highlighted fields."
            )

    cabs = Cab.objects.filter(is_active=True)
    popular_routes = TaxiRoute.objects.filter(is_active=True).order_by("sort_order", "destination")

    return render(
        request,
        "index.html",
        {
            "form": form,
            "business_phone": BUSINESS_PHONE,
            "business_email": BUSINESS_EMAIL,
            "cabs": cabs,
            "popular_routes": popular_routes,
        }
    )


def services(request):
    return render(
        request,
        "services.html",
        {
            "business_phone": BUSINESS_PHONE,
            "business_email": BUSINESS_EMAIL,
        }
    )


def about(request):
    return render(
        request,
        "about.html",
        {
            "business_phone": BUSINESS_PHONE,
            "business_email": BUSINESS_EMAIL,
        }
    )


def contact(request):
    return render(
        request,
        "contact.html",
        {
            "business_phone": BUSINESS_PHONE,
            "business_email": BUSINESS_EMAIL,
        }
    )
    
def route_detail(request, slug):
    route = get_object_or_404(
        TaxiRoute,
        slug=slug,
        is_active=True
    )

    return render(
        request,
        "route_detail.html",
        {
            "route": route,
            "business_phone": BUSINESS_PHONE,
            "business_email": BUSINESS_EMAIL,
        }
    )    