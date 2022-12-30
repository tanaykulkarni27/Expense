from datetime import datetime
import sqlite3


con = sqlite3.connect('main/database.db',check_same_thread=False)

cursor = con.cursor()

def commit():
	con.commit()
class trade:	
	def create_table(self):
		cursor.execute('''
		CREATE TABLE "TRADE" (
			"type"	VARCHAR(255),
			"name"	VARCHAR(255),
			"date"	VARCHAR(255)
			"quantity"	INTEGER,
			"price"	INTEGER,
			"total"	INTEGER,
			"TRADE_ID" INTEGER,
			"IS_END" BOOLEAN
		);
		''')
		commit();
	def get_all(self,trade_id=None):
		if trade_id == None:
			x = cursor.execute('''SELECT * FROM TRADE''')
			y = dict();
			for i in x:
				y[i[6]] = i[1]
			return y
		return cursor.execute(f'''SELECT * FROM TRADE WHERE TRADE_ID == '{trade_id}' ''')

	def insert(self,tp,name,quantity,price,Trade_Id,emotion):
		total = float(price * quantity)
		date = str(datetime.today().strftime('%d-%m-%y'))
		cursor.execute(f'''INSERT INTO TRADE(type,name,date,quantity,price,total,TRADE_ID,IS_END,Reason) VALUES('{tp}','{name}','{date}',{quantity},{price},{total},{Trade_Id},0,'{emotion}')''')
		commit()
		
	def init(self):
		cursor.execute('''TRUNCATE TRADE''')
		commit()
	def end_trade(self,trade_id):
		cursor.execute(f'''UPDATE TRADE SET IS_END = 1 WHERE TRADE_ID == trade_id''')
		commit()
class PnL:
	def create_table(self):
		cursor.execute('''
		CREATE TABLE "PnL" (
		"date"	DATE DEFAULT current_timestamp,
		"profit"	INTEGER
		)
		'''	
		);
	def insert(self,profit):
		date = str(datetime.today().strftime('%d-%m-%y'))
		chk = cursor.execute(f'''SELECT * FROM PnL WHERE date == '{date}' ''');
		ok = False
		total = 0
		for i in chk:
			total += i[1]
			ok = True
		if ok:
			total += profit
			cursor.execute(f'''UPDATE PnL SET profit = {total} WHERE date == '{date}' ''');
		else:
			cursor.execute(f'''INSERT INTO PnL(date,profit) VALUES('{date}',{profit})''')
		commit()
	def get_all(self):
		return cursor.execute('''SELECT * FROM PnL''')


class Expense:
	def create_table(self):
		cursor.execute('''
		CREATE TABLE Expense (
			Date	VARCHAR(255),
			Amount INTEGER
		);
		''')
		commit();
	def insert(self,amount):
		date = str(datetime.today().strftime('%d-%m-%y'))
		chk = cursor.execute(f'''SELECT * FROM Expense WHERE Date == '{date}' ''');
		ok = False
		total = 0
		for i in chk:
			total += i[1]
			ok = True
		if ok:
			total += amount
			cursor.execute(f'''UPDATE Expense SET Amount = {total} WHERE Date == '{date}' ''');
		else:
			cursor.execute(f'''INSERT INTO Expense(Date,Amount) VALUES('{date}',{amount})''')
		commit()
	def get_all(self):
		return cursor.execute(f'''SELECT * FROM Expense''')

class Income:
	def create_table(self):
		cursor.execute('''
		CREATE TABLE Income (
			Date	VARCHAR(255),
			Amount INTEGER
		);
		''')
		commit();
	def insert(self,amount):
		date = str(datetime.today().strftime('%m-%y'))
		chk = cursor.execute(f'''SELECT * FROM Income WHERE Date == '{date}' ''');
		ok = False
		total = 0
		for i in chk:
			total += i[1]
			ok = True
		if ok:
			total += amount
			cursor.execute(f'''UPDATE Income SET Amount = {total} WHERE Date == '{date}' ''');
		else:
			cursor.execute(f'''INSERT INTO Income(Date,Amount) VALUES('{date}',{amount})''')
		commit()
	def get_all(self):
		return cursor.execute(f'''SELECT * FROM Income''')
class schedule:
	def insert(self,date,work):
		cursor.execute(f'insert into schedule(date,work) values("{date}","{work}")');
		commit();
	def delete(self,id):
		cursor.execute(f'delete from schedule where id = {id}');
		commit();
	def get_all(self):
		return cursor.execute(f'select * from schedule order by date');