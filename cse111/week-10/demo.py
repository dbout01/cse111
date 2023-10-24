# Outline for Exceptions - one way to do it

filename = None

while file == None:
    filename = input(...)
    try:
        file = open(filename, "rt") #opens the file so you don't have to open it later
    except:
        print(...)
        file = None

...

for line in file: #prints lines in the file
    print(line)



file.close() #closes the file