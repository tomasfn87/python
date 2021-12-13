import datetime, sys
sys.path.append("/home/morbi/filtering")
from texto import Texto as T # https://github.com/tomasfn87/filtering/blob/main/texto.py

def todaysDate(month, day, year):

    months = {
        "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, 
        "june": 6, "july": 7, "august": 8, "september": 9, "october": 10, 
        "november": 11, "december": 12
    }

    month_names_dict = months.keys()

    for month_name in month_names_dict:
        if month == str(months[month_name]):
            month = month_name

    day = T.turnIntoEnglishOrdinalNumber(day)
    month = month.capitalize()

    today = f"Today's {month} {day} {year}."
    if month == "December":
        today += " Merry Christmas and a Happy New Year!"
    else:
        today += " Have a good day!"

    return today

today = datetime.date.today()
day = today.strftime("%d") 
month = today.strftime("%m")
year = today.strftime("%Y")

print(todaysDate(month, day, year))
print(todaysDate("8", "22", "1987"))
print(todaysDate("11", "1", "2001"))
print(todaysDate("10", "2", "2006"))
print(todaysDate("6", "3", "2011"))
