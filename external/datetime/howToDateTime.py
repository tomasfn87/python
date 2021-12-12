import datetime

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

if day in ["1", "01"]:
    day += "st"
elif day in ["2", "02"]:
    day += "nd"
elif day in ["3", "03"]:
    day += "rd"
else:
    day += "th"

print(f"Today's {month} {day} {year}.", end = " ")
if month == "december":
    print("Merry Christmas and a Happy New Year!")
else:
    print("Have a good day!")
