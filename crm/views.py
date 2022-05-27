from django.shortcuts import render

from cms.models import Slider
from price.models import Card, Service
from .forms import OrderForm
from .models import Order


def index(request):
    slides = Slider.objects.all()
    card_1, card_2, card_3 = Card.objects.all()
    services = Service.objects.all()
    form = OrderForm()
    context = {
        'slides': slides,
        'card_1': card_1,
        'card_2': card_2,
        'card_3': card_3,
        'services': services,
        'form': form
    }
    return render(request, 'pages/index.html', context)


def thanks(request):
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    element = Order(order_name=name, order_phone=phone)
    element.save()
    return render(request, "pages/thanks.html", {'name': name})
