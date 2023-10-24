"""
v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
"""

import math; 

def car_tire_pressure(w, r, d):     #<- parameters (context - helps define function so it can work)
    return math.pi * w ** 2 * r * (w * r + 2540 * d) / 10000000000 


width = int(input("Enter the width of the tire in mm: ")) #205 - Asks for width
ratio = int(input("Enter the aspect ratio of the tire: ")) #60 - Asks for ratio
dia = int(input("Enter the diameter of the wheel in inches: ")) #15 - Asks for diamter

v = car_tire_pressure (width, ratio, dia) #<- arguments (refers to parameters)

print(f"{v:.2f}") #32.92 #displays output