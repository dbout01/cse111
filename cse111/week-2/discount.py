from datetime import datetime

discount_rate = 0.10

sales_tax_rate = 0.06

subtotal = float(input('Please enter the subtotal'))

today = datetime.now();

weekday = today.weekday();

if subtotal >= 50 and (weekday ==1 or weekday ==2):
    discount = round(subtotal * discount_rate, 2)