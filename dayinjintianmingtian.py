import datetime
today=datetime.date.today()
oneday=datetime.timedelta(days=1)
yesterday=today-oneday	
tomorrow=today+oneday
print yesterday,today,tomorrow
