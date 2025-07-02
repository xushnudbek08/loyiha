from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from main.models import Product, Category, color, ssd




# Create your views here.
def home(request):
    return render(request, 'home.html')


def first_page(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def products(request):
    return render(request, 'products.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Noto'g'ri foydalanuvchi nomi yoki parol.")
    return render(request, 'login.html')


def Register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirmPassword')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("bu foydalanuvchi mavjud")
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                login(request, user)
                print("sizga mumkin")
                return redirect('home')
        else:
            print("sizga mumkin emas")
    return render(request, 'register.html')

def logout_view(request):
    auth_logout(request)
    return redirect('login')



def checkout(request):
    return render(request, 'checkout.html')




def product_list(request):
    categories = Category.objects.all()
    colors = color.objects.all()
    ssds = ssd.objects.all()
    selected_category = request.GET.get('category')
    selected_color = request.GET.get('color')
    selected_ssd = request.GET.get('ssd')

    products = Product.objects.all()
    if selected_category and selected_category != "all":
        products = products.filter(category__id=selected_category)
    if selected_color and selected_color != "all":
        products = products.filter(color__id=selected_color)
    if selected_ssd and selected_ssd != "all":
        products = products.filter(ssd__id=selected_ssd)




    text = {
        'products': products,
        'categories': categories,
        'colors': colors,
        'ssds': ssds,
        'selected_category': selected_category,
        'selected_color': selected_color,
        'selected_ssd': selected_ssd
    }
    return render(request, 'products.html', text)
