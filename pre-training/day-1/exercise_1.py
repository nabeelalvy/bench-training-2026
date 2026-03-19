# ======================
# Data types + operators
# ======================

name = 'Nabeel Alvi'
age = 31
is_coffee_drinker = True
salary = 50_000.0

print(f"""
Hi, my name is {name} and my age is {age} years old, 
I do{' not' if not is_coffee_drinker else ''} drink coffee and my salary is {salary} PKR.""")

retirement_age = 60
years_to_retire = retirement_age - age
print(f"""
My years left until retirement: {years_to_retire} years""")

cups_per_day = 3
price_per_coffee = 150.0
days_in_week = 7

print(f"""
My weekly coffee budget is: Rs {price_per_coffee * cups_per_day * days_in_week}""")
