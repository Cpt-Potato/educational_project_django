from django.shortcuts import render

from .forms import OrderForm
from .models import Order


def index(request):
    form = OrderForm()
    return render(request, 'pages/index.html', {'form': form})


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name=name, order_phone=phone)
        element.save()
    else:
        return render(request, 'pages/thanks.html')
