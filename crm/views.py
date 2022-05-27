from django.shortcuts import render

from cms.models import Slider
from price.models import Card, Service
from .models import Order


def index(request):
    slides = Slider.objects.all()
    card_1, card_2 = Card.objects.all()
    services = Service.objects.all()
    context = {
        'slides': slides,
        'card_1': card_1,
        'card_2': card_2,
        'services': services
    }
    return render(request, 'pages/index.html', context)


def thanks(request):
    if request.POST:
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        element = Order(order_name=name, order_phone=phone)
        element.save()
    else:
        return render(request, "pages/thanks.html")
