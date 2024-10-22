from django.shortcuts import render


# Create your views here.

def shop_template(request):
    context = {
        'home': 'Квартира',
        'kettle': 'Чайник',
        'car': 'Ааавтомобииииль'

    }
    return render(request, 'third_task/shop.html', context)

def shoppingcart(request):
    return render(request, 'third_task/shoppingcart.html')
