from django.urls import path
from . import views 



urlpatterns = [
    path('',views.first_page, name='first_page'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.product_list, name='products'),
    path('login/', views.login_view, name='login'),
    path('register/', views.Register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]

