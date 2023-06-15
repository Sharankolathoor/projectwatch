from django.urls import path
from wapp import views
urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),
    path('brandpage/',views.brandpage,name="brandpage"),
    path('savebrand/',views.savebrand,name="savebrand"),
    path('displaybrand/',views.displaybrand,name="displaybrand"),
    path('editbrand<int:brandid>/',views.editbrand,name="editbrand"),
    path('updatebrand<int:brandid>/',views.updatebrand,name="updatebrand"),
    path('deletebrand<int:brandid>/',views.deletebrand,name="deletebrand"),
    path('productpage/',views.productpage,name="productpage"),
    path('saveproduct/',views.saveproduct,name="saveproduct"),
    path('displayproduct/',views.displayproduct,name="displayproduct"),
    path('editproduct<int:p_id>/',views.editproduct,name="editproduct"),
    path('updateproduct<int:p_id>/',views.updateproduct,name="updateproduct"),
    path('deleteproduct<int:p_id>/',views.deleteproduct,name="deleteproduct"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminlogout/',views.adminlogout,name="adminlogout")
]