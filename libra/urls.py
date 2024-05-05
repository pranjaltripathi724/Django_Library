from django.urls import path
from . import views
from django.contrib import admin 
# from .views import search_view

urlpatterns = [
    path('signup/',views.user_signup),
    path('login/',views.user_login),
    path('',views.front),
    path('showbook/',views.showbook),
    path('showstd/',views.showstd),
    path('addbook/',views.addbook),
    path('addstudent/',views.addstudent),
    path('inputstudent/',views.inputstudent),
    path('inputbook/',views.inputbook),
    path('delete/<int:id>',views.delete),
    path('editbook/<int:id>',views.editbook),
    path('showissue/',views.showissue),
    path('inputissue/',views.inputissue),
    path('issue/',views.issue),
    path('update/<int:id>/',views.update),
    path('logout/',views.user_logout),
    path('Mdelete/<int:id>',views.Mdelete),
    path('Medit/<int:id>',views.Medit),
    path('about/',views.about),
    # path('filterstudent/<int:id>',views.filterstudent),
    path('issuebook/',views.issuebook),
    # path('search/',views.search_view,),  
    

]