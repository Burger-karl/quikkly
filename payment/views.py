from django.shortcuts import render, redirect
from .models import Payment
from delivery.models import Delivery
from django.contrib import messages

# Create your views here.

def verify_payment(request, ref):
    payment = Payment.objects.get(ref=ref)
    verified = payment.verify_payment()

    if verified:
        obj = Delivery.objects.get(pk=request.session['delivery'])
        obj.is_verified = True
        obj.save()
        messages.success(request, 'Payment verified. A dispatch rider is coming soon')
        return redirect('dashboard')
    else:
        messages.warning(request, 'Something went wrong with your payment, please try again')
        return redirect('dashboard')