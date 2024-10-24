"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
# from task2.views import func_template, ClassTemplate
# from task3.views import shop_template, shoppingcart
# from task4.views import shop_template, shoppingcart
from task5.views import  sign_up_by_html, sign_up_by_django

# Task 5
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sign_up_by_html, name='html_sign_up'),
    path('django_sign_up/', sign_up_by_django, name='django_sign_up'),
]

# Task 4
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', TemplateView.as_view(template_name='fourth_task/platform.html')),
#     path('shop/', shop_template),
#     path('shoppingcart/', shoppingcart)
# ]
# Task 3
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('index/', TemplateView.as_view(
#         template_name='second_task/index.html')),
#     path('func/', func_template),
#     path('class/', ClassTemplate.as_view()),
#
#     path('', TemplateView.as_view(template_name='third_task/platform.html')),
#     path('shop/', shop_template),
#     path('shoppingcart/', shoppingcart)
# ]

# Task 2
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('index/', TemplateView.as_view(
#         template_name='second_task/index.html')),
#     path('func/', func_template),
#     path('class/', ClassTemplate.as_view()),
# ]