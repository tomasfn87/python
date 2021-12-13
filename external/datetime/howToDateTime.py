import datetime, sys
sys.path.append("/home/morbi/filtering")
from texto import Texto as T # https://github.com/tomasfn87/filtering/blob/main/texto.py

months = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11,
    "december": 12
}

today = datetime.date.today()

day = today.strftime("%d") 
month = today.strftime("%m")
year = today.strftime("%Y")

month_names_dict = months.keys()

for month_name in month_names_dict:
    if month == str(months[month_name]):
        month = month_name

day = T.turnIntoEnglishOrdinalNumber(day)
month = month.capitalize()

print(f"Today's {month} {day} {year}.", end = " ")
if month == "December":
    print("Merry Christmas and a Happy New Year!")
else:
    print("Have a good day!")
