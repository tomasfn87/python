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
month.capitalize()

if day in ["1", "01"]:
    # Superscript st
    day += chr(738)
    day += chr(7511)
elif day in ["2", "02"]:
    # Superscript nd
    day += chr(8319)
    day += chr(7496)
elif day in ["3", "03"]:
    # Superscript rd
    day += chr(691)
    day += chr(7496)
else:
    day += chr(7511)
    day += chr(688)

print(f"Today's {month} {day} {year}.", end = " ")
if month == "december":
    print("Merry Christmas and a Happy New Year!")
else:
    print("Have a good day!")
