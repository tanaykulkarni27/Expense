from django.shortcuts import render
from django.http import HttpResponse
from . import db_handler as db
from threading import Thread
import os

'''

end trade validate : 
	TOTAL QUANTITY IN SELL == TOTAL QUANTITY IN BUY
calculate profit : 
	total invested value - total sold 

'''
class Cdict():
	def __init__(self):
		self.D = dict() 
	def get(self,x):
		if self.D.get(x) == None:
			return 0
		return self.D.get(x)
	def set(self,key,val):
		self.D[key] = val;
	def __itr__(self):
		return self.D
	def items(self):
		return self.D.items()
	def __str__(self):
		return self.D	
		
def home(req):	
	# data objects
	trade = db.trade()
	PnL = db.PnL()
	
	if req.method == 'POST':
		prof = float(req.POST.get('Profit'))
		PnL.insert(prof)
	
	x = trade.get_all()
	y = []
	for i,j in x.items():
		y.append((i,j))
	y.sort(reverse=True)
	graph = [['date','Profit']]
	Profit = 0
	Loss = 0
	
	X = Cdict() 		
	
	for i in PnL.get_all():
		X.set(i[0],X.get(i[0]) + i[1]);
		if i[1] > 0:
			Profit += i[1]
		else:
			Loss += abs(i[1])
	for i in X.items():
		graph.append([i[0],i[1]]);
		
	return render(req,'PnL.html',{'trades':y,'PnL':graph,'P' : Profit,'L' : Loss})
	
def view_report(req,trade_name,Trade_Id = None):
	trade = db.trade()
	PnL = db.PnL()
	if req.method == "POST":
		name = trade_name
		tp = req.POST.get('type')
		price = float(req.POST.get('price'))
		quantity = int(req.POST.get('quantity'))
		emotion  = req.POST.get("emotion");
		trade.insert(tp,name,quantity,price,Trade_Id,emotion)
	if req.GET.get('TYP') == 'end_trade':
		trade.end_trade(Trade_Id);
	context = dict()
	context['rows'] = trade.get_all(Trade_Id)
	context['IS_END'] = False;
	total_investment = 0
	total_quantity = 0
	for i in trade.get_all(Trade_Id):
		if i[7] == 1:
			context['IS_END'] = True
		if i[0] == 'buy':
			total_investment += i[5];
			total_quantity += i[3];
	context['rows'] = trade.get_all(Trade_Id); 	
	context['TOTAL_INVESTMENT'] = total_investment;
	context['TOTAL_QUANTITY'] = total_quantity;
	return render(req,'report.html',context)	
	
	
def NewTrade(req):
	Trade_Id = None
	trade = db.trade()
	if req.method == "POST":
		with open('main/ID.txt','r') as f:
			Trade_Id = int(f.read().replace('\n',''))
		
		name = req.POST.get('name')
		tp = req.POST.get('type')
		price = float(req.POST.get('price'))
		quantity = int(req.POST.get('quantity'))
		emotion  = req.POST.get("emotion");
		trade.insert(tp,name,quantity,price,Trade_Id,emotion)
		with open('main/ID.txt','w') as f:
			Trade_Id += 1
			f.write(f'{Trade_Id}')
	return render(req,'NewTrade.html')

def main(req):
	if req.method == "POST":
		db.schedule().insert(req.POST.get('date'),req.POST.get('work'));
	elif req.GET.get('type') == "delete":
		db.schedule().delete(req.GET.get('id'));
	context = dict();
	context['data'] = db.schedule().get_all();
	return render(req,'main.html',context)

class IncomeExpense: 
	def ExpenseHandler(self,req):
		if req.method == "POST": 
			if req.POST.get('type') == 'expense':
				amnt = int(req.POST.get('Eamnt'))
				db.Expense().insert(amnt)
		expenses = [['Date','Expense']]
		for i in db.Expense().get_all():
			expenses.append(list(i))
		return {"ExpenseData" : expenses}
	def IncomeHandler(self,req):
		if req.method == "POST": 
			if req.POST.get('type') == 'income':
				amnt = int(req.POST.get('Iamnt'))
				db.Income().insert(amnt)
		incomes = [['Date','Income']]
		for i in db.Income().get_all():
			incomes.append(list(i))
		return {"IncomeData" : incomes}
	def Handler(self,req):
		context = self.ExpenseHandler(req);
		context.update(self.IncomeHandler(req));
		return render(req,'expense.html',context)

