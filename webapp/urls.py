from django.urls import path
from webapp import views

urlpatterns=[
    path('hompage/',views.hompage,name="hompage"),
    path('productpage/<brand_name>',views.productpage,name="productpage"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('savecontact/',views.savecontact,name="savecontact"),
    path('singleproduct<int:prid>/',views.singleproduct,name="singleproduct"),
    path('registerpage/', views.registerpage, name="registerpage"),
    path('saveregister/', views.saveregister, name="saveregister"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('cartpage/', views.cartpage, name="cartpage"),
    path('savecart/', views.savecart, name="savecart"),
    path('deletecart<int:cartid>/', views.deletecart, name="deletecart"),
    path('checkoutpage/', views.checkoutpage, name="checkoutpage"),
    path('savecheckout/', views.savecheckout, name="savecheckout")

]