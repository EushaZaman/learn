import datetime
vacation = datetime.datetime(2024,8,3,15,30)
returndate = datetime.timedelta(days=15)
print(vacation)
print(vacation+returndate)
print((vacation+returndate).strftime("%B %d %Y"))
birthday = "03-2-2001 9:23"
print(birthday)
print(datetime.datetime.strptime(birthday,"%d-%m-%Y %H:%M"))
