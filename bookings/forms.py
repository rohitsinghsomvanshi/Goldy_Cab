from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "customer_name", "phone", "email", "trip_type", "pickup", "dropoff",
            "travel_date", "travel_time", "passengers", "cab_type", "notes",
        ]
        widgets = {
            "travel_date": forms.DateInput(attrs={"type": "date", "min": "2026-01-01"}),
            "travel_time": forms.TimeInput(attrs={"type": "time"}),
            "notes": forms.Textarea(attrs={"rows": 3, "placeholder": "Flight details, luggage, or other requirements"}),
            "passengers": forms.NumberInput(attrs={"min": 1, "max": 20}),
        }

    def clean_phone(self):
        phone = self.cleaned_data["phone"].strip()
        digits = "".join(ch for ch in phone if ch.isdigit())
        if len(digits) < 10 or len(digits) > 15:
            raise forms.ValidationError("Enter a valid phone number (10–15 digits).")
        return phone
