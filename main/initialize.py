from datetime import datetime
from . import db_handler
Expense = db_handler.Expense

def get_date(dt):
    res = ''
    for i in range(3):
        if dt[i] < 10:
            res += '0';
        res += str(dt[i]);
        if i != 2:
            res += '-';
    return res;
def init(dates):
    ok = True
    date = str(datetime.today().strftime('%d-%m-%y'))
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    for year in range(23,200):
        if not ok:
            break;
        for month in range(1,13):
            if not ok:
                break;
            for day in range(1,32):
                if day > days[month]:
                    break;
                x = get_date([day,month,year])
                # print(x)
                if x not in dates:
                    Expense().insert(0,x);
                if x == date:
                    ok = False
                    break;

#main

def run():
    data = Expense().get_all();
    dates = []
    for i in data:
        dates.append(i[0])
    init(dates)