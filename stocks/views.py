from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from stocks.forms import UserCustomerForm,ExtendedUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as login
from django.db import connection
from datetime import date
import json,requests
from . import urls
from .models import Stocks,Currency,Purchased


def refresh():
	cursor = connection.cursor()
	cursor.execute("TRUNCATE stocks_stocks")
	symbol_ticker=['AAPL','HOG','HPQ','INTC','KO','MSFT','T','WMT','FB','GOOG',]
	for x in symbol_ticker:
		url = "https://www.worldtradingdata.com/api/v1/stock?api_token=enG5wFUsWzEgSTuTIKncA2KgXd2HCzTumMSo1sZZQEXzGkviSbMQvET1rlqU&symbol="+ x
		stck = requests.get(url)
		stcks = json.loads(stck.content)
		data = stcks['data'][0]
		print()
		st_obj = Stocks(
			Symbol = data['symbol'],
			Company = data['name'],
    		Price = str(data['price']),
    		Currency = data['currency'],
    		Open = str(data['price_open']),
    		Close = str(data['close_yesterday']),
   			High = str(data['day_high']),
    		Low = str(data['day_low']),
    		DayChange = str(data['change_pct']) +'%',
    		StockExchange = data['stock_exchange_short'],
		)
		st_obj.save()
	mprice = Stocks.objects.get(id=6).Price
	mcomp = Stocks.objects.get(id=6).Company

	aprice = Stocks.objects.get(id=1).Price
	acomp = Stocks.objects.get(id=1).Company

	fprice = Stocks.objects.get(id=9).Price
	fcomp = Stocks.objects.get(id=9).Company

	

	cursor = connection.cursor()
	cursor.execute("TRUNCATE stocks_currency")
	url = "https://www.worldtradingdata.com/api/v1/forex?sort=newest&api_token=enG5wFUsWzEgSTuTIKncA2KgXd2HCzTumMSo1sZZQEXzGkviSbMQvET1rlqU&base="
	arr = ['CAD', 'GBP', 'EUR', 'PKR', 'KWD', 'SAR','CNY']
	base = 'USD'

	info = requests.get(url + base)
	info = json.loads(info.content)
	info = info['data']
	for z in arr:
		var = info[z]
		c_obj = Currency(
			Name = z,
			Price = var,
			Base = base,
		)
		c_obj.save()
	
	price1 = Currency.objects.get(id=3).Price
	comp1 = Currency.objects.get(id=3).Name

	price2 = Currency.objects.get(id=1).Price
	comp2 = Currency.objects.get(id=1).Name

	price3 = Currency.objects.get(id=4).Price
	comp3 = Currency.objects.get(id=4).Name

	price4 = Currency.objects.get(id=6).Price
	comp4 = Currency.objects.get(id=6).Name

	context = {
		'mprice':mprice,
		'mcompany':mcomp,
		'aprice':aprice,
		'acompany':acomp,
		'fprice':fprice,
		'fcompany':fcomp,
		'price1':price1,
		'comp1':comp1,
		'price2':price2,
		'comp2':comp2,
		'price3':price3,
		'comp3':comp3,
		'price4':price4,
		'comp4':comp4,
	}

	return context
# Create your views here.
def home(request):
	
	context = refresh()

	return render(request,'stocks/index.html',context)
def aboutus(request):
	return HttpResponse('<center><h1>You Wanna Know About us Nigga</h1></center>')
def signup(request):
	if request.method == 'POST':
		form = ExtendedUserCreationForm(request.POST)
		customer_form = UserCustomerForm(request.POST)
		if form.is_valid() and customer_form.is_valid():
			user = form.save()
			customer = customer_form.save(commit=False)
			customer.user = user

			customer.save()

			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username,password=password)
			login(request,user)
			
			return redirect('/')
	else:
		form = ExtendedUserCreationForm()
		customer_form = UserCustomerForm()

	context = {'form' : form, 'customer_form' : customer_form}
	return render(request ,'stocks/signup.html',context)

def Stockdata(request):
	refresh()
	context = Stocks.objects.all()
	return render(request,'stocks/stocksdata.html',{'context':context})

def Currencydata(request):
	refresh()
	context = Currency.objects.all()
	return render(request,'stocks/currencydata.html',{'context':context})

@login_required
def profile(request):
	refresh()
	investmentdata = Purchased.objects.filter(User_id=request.user.id)
	investments = []
	for obj in investmentdata:
		profloss=0
		if obj.identifier == 'Stocks':
			x = int(obj.Quantity,10)
			y = float(obj.Investment)
			nprice = Stocks.objects.get(Symbol=obj.Name).Price
			nprice = float(nprice)
			oprice = y/x
			profloss = (nprice-oprice)*x
			profloss = str(profloss)
		else:
			x = int(obj.Quantity,10)
			y = float(obj.Investment)
			nprice = Currency.objects.get(Name=obj.Name).Price
			nprice = float(nprice)
			oprice = y/x
			profloss = (nprice-oprice)*x
			profloss = str(profloss)

		investment={
			'Name': obj.Name,
			'Type': obj.identifier,
			'Investment': obj.Investment,
			'Quantity': obj.Quantity,
			'profloss':	profloss
		}
		investments.append(investment)
	context = {
		'investments':investments
	}
	return render(request,'stocks/userinfo.html',context)

def currencydetail(request,id):
	context = Currency.objects.get(id=id)
	return render(request,'stocks/currency.html',{'context':context})

def stockdetail(request,id):
	context = Stocks.objects.get(id=id)
	return render(request,'stocks/stock.html',{'context':context})

@login_required
def purchasestock(request,id):
	refresh()
	context = Stocks.objects.get(id=id)
	if request.method == 'POST':
		quantity = request.POST.get('Quantity','')
		pin = request.POST.get('Pin','')
		quan = int(quantity,10)
		pre = Stocks.objects.get(id=id).Price
		print(pre)
		price = float(pre)
		newprice = price*quan
		print(newprice)
		nprice = str(newprice)

		pur_obj = Purchased(
			User = request.user,
			Name = Stocks.objects.get(id=id).Symbol,
			identifier = 'Stocks',
			Quantity = quantity,
			Investment = nprice,
		)
		pur_obj.save()

		return redirect('/userinfo')

	return render(request,'stocks/purchasestock.html',{'context':context})

@login_required
def purchasecurrency(request,id):
	refresh()
	context = Currency.objects.get(id=id)
	if request.method == 'POST':
		quantity = request.POST.get('Quantity','')
		pin = request.POST.get('Pin','')
		quan = int(quantity,10)
		pre = Currency.objects.get(id=id).Price
		print(pre)
		price = float(pre)
		newprice = price*quan
		print(newprice)
		nprice = str(newprice)

		pur_obj = Purchased(
			User = request.user,
			Name = Currency.objects.get(id=id).Name,
			identifier = 'Currency',
			Quantity = quantity,
			Investment = nprice,
		)
		pur_obj.save()

		return redirect('/userinfo')

	return render(request,'stocks/purchasecurrency.html',{'context':context})