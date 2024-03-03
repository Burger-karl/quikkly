from django import forms
from .models import Delivery


class StartDeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['package_name', 'pickup_address', 'recipient_name', 'recipient_phone', 'recipient_address']


class AssignDeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['rider']