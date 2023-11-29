"""wishlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Common_Home),
    path('home/', views.Common_Home),
    path('SignUp/', views.Customer_Registration),
    path('SignIn/',views.SignIn,name='Sign In'),
    path('ShopSignUp/', views.Shop_Registration),
    path('AdminHome/',views.Admin_Home,name='Admin Home'),
    path('Shop_Home/',views.Shop_Home,name='Shop_Home Home'),
    path('Customer_Home/',views.Customer_Home,name='Customer Home'),
    path('CustomerHome/',views.Customer_Home,name='Customer Home'),
    path('AboutUs/',views.About_Us,name='About Us'),
    path('ContactUs/',views.Contact,name='Contact Us'),
    path('Gallery/',views.Gallery,name='Gallery'),
# -------------Admin------------------
    path('AdminAddCategory/',views.Admin_Add_Category,name='Admin Add Category'),
    path('AdminRemoveCategory/',views.AdminRemoveCategory,name='AdminRemoveCategory'),
    path('AdminViewCustomers/',views.Admin_View_Customers,name='Admin View Customers'),
    path('Admin_View_Feedback/',views.Admin_View_Feedback,name='Admin View Admin_View_Feedback'),
    path('Admin_View_Shop/',views.Admin_View_Shop,name='Admin View Admin_View_Shop'),
    path('Admin_View_Approved_Shop/',views.Admin_View_Approved_Shop,name='Admin View Admin_View_Approved_Shop'),
    path('AdminViewShop/',views.Admin_View_Shop,name='Admin View AdminViewShop'),



# -------------customer------------------
    path('Customerviewproduct/',views.Customerviewproduct,name="Customerviewproduct"),
    path('CustomerViewMyBooking/',views.CustomerViewMyBooking,name="CustomerViewMyBooking"),
    path('CustomerViewOrders/',views.CustomerViewOrders,name="CustomerViewOrders"),
    path('CustomerShopping/',views.CustomerShopping,name='CustomerShopping'),
    path('CustomerViewProfile/',views.Customer_View_Profile,name='Customer View Profile'),
    path('CustomerViewProDetails/',views.CustomerViewProDetails,name='CustomerViewProDetails'),
    path('CustomerViewCart/',views.CustomerViewCart,name="CustomerViewCart"),
    path('Customer_AddFeedback/',views.Customer_AddFeedback,name="Customer_AddFeedback"),
    
    path('payment1/',views.payment1,name='payment1'),
    path('payment2/',views.payment2,name='payment2'),
    path('payment3/',views.payment3,name='payment3'),
    path('payment4/',views.payment4,name='payment4'),
    path('payment5/',views.payment5,name='payment5'),
# -------------shop------------------
    path('ShopAddProduct/',views.Shop_Add_Product,name='Shop Add Product'),
    path('ShopViewMyProduct/',views.Shop_View_My_Product,name='Shop View My Product'),
    path('ShopRemoveProduct/',views.ShopRemoveProduct,name='ShopRemoveProduct'),
    path('ShopUpdateProduct/',views.ShopUpdateProduct,name='ShopUpdateProduct'),
    path('ShopViewOrders/',views.Shop_View_Orders,name='Shop View Orders'),
    path('Shop_View_payment/',views.Shop_View_payment,name='Shop View Shop_View_payment'),

    
]
