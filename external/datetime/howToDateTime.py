import datetime, sys
sys.path.append("/home/morbi/filtering")
from texto import Texto as T # https://github.com/tomasfn87/filtering/blob/main/texto.py

def getTodaysDate():
    today = datetime.date.today()
    month = today.strftime("%m")
    day = today.strftime("%d")
    year = today.strftime("%Y")
    return month, day, year

def toStr(number):
    assert type(number) in [str, int, float]
    if type(number) == float:
        number = int(number)
    if type(number) == int:
        number = str(number)
    return number

def todaysDate(todays_date):
    assert len(todays_date) == 3 and type(todays_date) == tuple
    month, day, year = todays_date[0], todays_date[1], todays_date[2]
    month, day, year = toStr(month), toStr(day), toStr(year)

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

today = getTodaysDate()

print(todaysDate(today))
print(todaysDate(("8", "22", "1987")))
print(todaysDate(("11", "1", "2001")))
print(todaysDate(("10", "2", "2006")))
print(todaysDate(("6", "3", "2011")))
print(todaysDate((9, 5, 1979)))
