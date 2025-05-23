from datetime import datetime
from dateutil.relativedelta import relativedelta

print("Enter ur birthdate(dd/mm/yy): ")
bdate = int(input("Day: "))
bmonth = int(input("Month: "))
byear = int(input("Year: "))
if byear > 25:
    byear += 1900
else:
    byear += 2000


def leap(x):
    if x%4==0:
        return f"{x} is a leap year."
    else:
        return f"{x} is not a leap year."

def age(bdate,bmonth,byear):
    birthday = datetime.strptime(f"{bdate}-{bmonth}-{byear}", "%d-%m-%Y")
    current_date = datetime.now()
    difference = relativedelta(current_date,birthday)
    
    print(f"You are {difference.years} years, {difference.months} months, {difference.days} days, {difference.hours} hours, {difference.minutes} minutes, and {difference.seconds} seconds old.")

print(leap(byear))
# print(time_now.tm_year)
age(bdate,bmonth,byear)