students = {
    "G0G": ["Godric", "G", "Cherry Unicorn"],
    "S0G": ["Salazar", "S", "Dragon Heartstring"],
    "H0G": ["Helga", "H", "Pine Kangaroo"],
    "R0G": ["Rowena", "R", "Redwood Eagle Spinx Hair"]
}

FNAME = 0
LNAME = 1
WAND = 2

find_student = "H0G"

# Is in?
if find_student in students:
    print("Student was found")
else:
    print("Student doesn't exist")
exit()

#Show student roster
for student_id in students:
    student = students[student_id]
    print(f"{student[FNAME]} {student[LNAME]} uses a {student[WAND]} wand")