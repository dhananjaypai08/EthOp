from django.contrib import admin
from django.urls import path
from ethapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blocklookup/', views.blocklookup, name='blocklookup'),
    path('checkbalance/', views.getBalance, name='getBalance'),
    path('maketransactions/', views.transactions_home, name='transactionhome'),
    path('maketransactions/gettransactions', views.get_transactions, name='gettransactions'),
    path('maketransactions/sendtransactions', views.send_transactions, name='sendtransactions'),
]
