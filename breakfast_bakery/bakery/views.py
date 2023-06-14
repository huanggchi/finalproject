from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Product
from .models import Feedback
from .models import NewsItem

# Create your views here.
def product_list(request):
    return render(request, 'product.html')
def order(request):
    # 假設菜單項目以字典列表的形式傳遞
    menu_items = [
        {'id': 1, 'name': '豐盛早餐套餐', 'price': 100},
        {'id': 2, 'name': '蔬果營養沙拉', 'price': 80},
        {'id': 3, 'name': '經典美式鬆餅', 'price': 60},
        {'id': 4, 'name': '健康穀物早餐麥片', 'price': 40},
    ]

    cart_items = request.session.get('cart_items', [])

    # 計算總金額
    total_price = sum(item['price'] for item in cart_items)

    context = {
        'menu_items': menu_items,
        'cart_items': cart_items,
        'total_price': total_price
    }

    return render(request, 'order.html', context)

def add_to_cart(request, item_id):
    menu_items = [
        {'id': 1, 'name': '豐盛早餐套餐', 'price': 100},
        {'id': 2, 'name': '蔬果營養沙拉', 'price': 80},
        {'id': 3, 'name': '經典美式鬆餅', 'price': 60},
        {'id': 4, 'name': '健康穀物早餐麥片', 'price': 40},
    ]

    item = next((item for item in menu_items if item['id'] == item_id), None)

    if item:
        cart_items = request.session.get('cart_items', [])
        cart_items.append(item)
        request.session['cart_items'] = cart_items

    return redirect('order')

def remove_from_cart(request, item_id):
    cart_items = request.session.get('cart_items', [])
    for item in cart_items:
        if item['id'] == item_id:
            cart_items.remove(item)
            break
    request.session['cart_items'] = cart_items

    return redirect('order')

def checkout(request):
    # 在此處處理結帳邏輯
    # ...

    # 清空購物車
    request.session['cart_items'] = []

    return redirect('order')

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contactus(request):
    return render(request, 'contact.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # 在這裡可以對表單資料進行處理，例如存入資料庫、寄送電子郵件等
        feedback = Feedback(name=name, email=email, message=message)
        feedback.save()
        # 可以將資料存入資料庫或其他後端儲存機制

        return redirect('contact_success')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact.html', context)

def contact_success(request):
    return render(request, 'contact.html')
def news(request):
    # 獲取最新消息的資料，假設使用 NewsItem 模型來表示最新消息
    news_items = NewsItem.objects.order_by('-publish_date')[:5]

    context = {
        'news_items': news_items
    }

    return render(request, 'news.html', context)