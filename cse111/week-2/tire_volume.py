import math
from datetime import datetime

#DEFINES PARAMETERS
def car_tire_pressure(w, r, d):
    return math.pi * w ** 2 * r * (w * r + 2540 * d) / 10000000000 

#ASKS USER FOR TIRE DIMENSIONS
width = int(input("Enter the width of the tire in mm: "))
ratio = int(input("Enter the aspect ratio of the tire: "))
dia = int(input("Enter the diameter of the wheel in inches: "))

v = car_tire_pressure (width, ratio, dia)

#GETS CURRENT DATE
current_date = datetime.now().strftime('%Y-%m-%d')

#OPENS .TXT FILE FOR APPENDING
with open('volumes.txt', 'a') as file:
    # Write the current date, tire dimensions, and volume to file
    file.write(f"{current_date}, {width}, {ratio}, {dia}, {v:.2f} \n")

#PRINTS OUTPUT
print(f"The approxiamte volume is {v:.2f} liters")