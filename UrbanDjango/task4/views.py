from django.shortcuts import render


# Create your views here.

def shop_template(request):
    prizes = ['Квартира', 'Чайник', 'Ааавтомобииииль']

    context = {
        'prizes': prizes
    }
    return render(request, 'fourth_task/shop.html', context)

def shoppingcart(request):
    return render(request, 'fourth_task/shoppingcart.html')
