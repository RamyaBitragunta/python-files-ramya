a = "pythontutorial"
print('%.6s' % a)


#code to display the current time
import datetime
TodayDate = datetime.datetime.now()
print(TodayDate)
#bt it prints in reverse order i.e year first and then followed by month and day
#so if we want to print it in a normal way
year = TodayDate.strftime("%y")
month = TodayDate.strftime("%m")
day = TodayDate.strftime("%d")
formattedDate = day +'/'+ month +'/'+ year
print(formattedDate)