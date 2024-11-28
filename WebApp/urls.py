from django.urls import path
from WebApp import views
urlpatterns = [
    path('home/',views.homepage,name="home"),
    path('Product_page/',views.Productpage,name="Product_page"),
    path('About_us/',views.Aboutpage,name="About_us"),
    path('Contact_us/',views.Contactpage,name="Contact_us"),
    path('Save_Contact/',views.Save_Contact,name="Save_Contact"),
    path('Product_filtered/<cat_name>/',views.filtered_products,name="Product_filtered"),
    path('Single_product/<int:pro_id>/',views.Singleproductpage,name="Single_product"),
    path('',views.Login_pages,name="Login_pages"),
    path('Signup_pages/',views.Signup_page,name="Signup_pages"),
    path('Signup_pageSave/',views.Save_Signup,name="Signup_pageSave"),
    path('User_login/',views.User_login,name="User_login"),
    path('User_logout/',views.User_logout,name="User_logout"),
    path('Save_cart/',views.Save_Cart,name="Save_cart"),
    path('Cart/',views.Cartpage,name="Cart"),
    path('CartRemove/<int:Cart_id>/',views.Removecart,name="CartRemove"),
    path('Check_out/',views.Checkoutpage,name="Check_out"),
    path('Save_Billing/',views.Save_BillingDetails,name="Save_Billing"),
    path('Make_Payment/',views.Paymentpage,name="Make_Payment"),
    path('Blog/',views.Blog_pages,name="Blog"),
    path('Services/',views.Service_pages,name="Services")



]