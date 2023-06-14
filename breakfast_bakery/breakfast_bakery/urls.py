"""
URL configuration for breakfast_bakery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import bakery.views as bakery
urlpatterns = [
    path("admin/", admin.site.urls),
    path('products/', bakery.product_list),
    path('order/', bakery.order, name='order'),
    path('add_to_cart/<int:item_id>/', bakery.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', bakery.remove_from_cart, name='remove_from_cart'),
    path('checkout/', bakery.checkout, name='checkout'),
    path('', bakery.index, name='index'),
    path('about/', bakery.about),
    path('contact/', bakery.contactus),
    path('contact_submit/', bakery.contact, name='contact_submit'),
    path('contact_success/', bakery.contact_success, name='contact_success'),
    path('news/', bakery.news, name='news'),
]
