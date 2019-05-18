from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='stocks-home'),
    path('aboutus/', views.aboutus, name='stocks-aboutus'),
	path('signup/', views.signup, name='signup'),
	path('login/', auth_views.LoginView.as_view(template_name='stocks/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='stocks/logout.html'), name='logout'),
    path('userinfo/',views.profile,name='userinfo'),
    path('stocksdata/',views.Stockdata,name='stocksdata'),
    path('currencydata/',views.Currencydata,name='currencydata'),
    path('currency/<id>',views.currencydetail,name='currencydetail'),
    path('stock/<id>',views.stockdetail,name='stockdetail'),
    path('purchasestock/<id>',views.purchasestock,name='purchasingstocks'),
    path('purchasecurrency/<id>',views.purchasecurrency,name='purchasingcurrencies'),
]

urlpatterns += staticfiles_urlpatterns()