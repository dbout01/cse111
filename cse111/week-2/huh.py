#IMPORT LIBRARIES FOR FUNCTIONS TO WORK PROPERLY
import math
from datetime import datetime

#DEFINES WHAT PROGRAMME IS GOING TO DO
def car_tire_pressure(w, r, d):     #<- parameters
    return math.pi * w ** 2 * r * (w * r + 2540 * d) / 10000000000 

#FUNCTION TO OPEN FILE AND WRITE RESULTS TO IT
def openfile(filename, v, current_date_and_time):
    with open(filename, 'a') as file:
        file.write(f"Date and time: {current_date_and_time:%Y-%m-%d %H:%M:%S}, Width: {width}, Ratio: {ratio}, Diameter: {dia}, Volume: {v:.2f} liters\n")

#ASKS USER FOR INPUT
width = int(input("Enter the width of the tire in mm (ex 205): ")) #Asks for width
ratio = int(input("Enter the aspect ratio of the tire (ex 60): ")) #Asks for ratio
dia = int(input("Enter the diameter of the wheel in inches (ex 15): ")) #Asks for diamter

v = car_tire_pressure (width, ratio, dia) #<- arguments (refers to parameters)

#GET CURRENT DATE AND TIME
current_date_and_time = datetime.now()

#OUTPUT
print(f"The approximate volume is {v:.2f} liters")
print(f"Today's date is {current_date_and_time:%Y-%m-%d %H:%M:%S}") 

#CALL FUNCTION TO OPEN FILE AND WRITE RESULTS TO IT
filename = 'results.txt'
openfile(filename, v, current_date_and_time)