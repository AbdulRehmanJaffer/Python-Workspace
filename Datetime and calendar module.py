"""from datetime import date , time , datetime

today = date.today()
now = datetime.now()

print("Today the date is,", today)
print("The time right now is, ", now)"""

#printing calendar
"""import calendar

cal = calendar.calendar(2026)
print(cal)"""

#displays calender with days with numbers in brackets
"""import calendar

cal = calendar.Calendar()
weeks = cal.monthdays2calendar(2026, 4)

for week in weeks:
    print(week)"""

"""import calendar

cal = calendar.Calendar()
year = cal.yeardayscalendar(2026)

print(year[0])"""

#Trip expenditure

def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsbourgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    if days>7:
        return 40*days - 50
    if days>3:
        return 40*days - 20
    else:
        40*days

def total_cost(city, nights, days, spending_money):
    return rental_car_cost(days) + hotel_cost(nights) + plane_ride_cost(city) + spending_money
print("The total cost was: ", total_cost("Los Angeles", 5, 6, 320))


