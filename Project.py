students = []
student1 = {
    "name": "doremon",
    "roll": "101",
     "maths": 90,
    "science": 85,
   "social": 88,
    " total": 263,
    "grade": "A+"
}

student2 ={
    "name": "ninja",
    "roll": "102",
    "maths": 80,
    "science": 79,
    "social": 74,
    "total": 253,
    "grade": "A"
}

student3 ={
    "name": "oggy",
    "roll": "103",
    "maths": 60,
    "science": 65,
    "social": 68,
    " total": 193,
    "grade": "B"
}

student4={

    "name": "vikash",
    "roll": "104",
    "maths": 50,
    "science": 55,
    "social": 58,
    "total": 195,
    "grade": "C"
}
students.append(student1)
students.append(student2)
students.append(student3)
students.append(student4)
for student in students:
     print("Name:", student["name"])



mark=int(input("enter the average mark"))
if mark >=90:
    print("A+")
elif mark >=75 and mark <= 89:
    print("A")
elif mark >= 60 and mark <=74:
    print("B")
elif mark >=50 and mark <=64:
    print("C")
else:
    print("below 40 - fail")

mark=int(input("enter the average mark"))

students = []
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    maths = int(input("Enter Maths marks: "))
    science = int(input("Enter Science marks: "))
    social = int(input("Enter Social marks: "))
    
 total = maths + science + social
average = total / 3

if average >= 90:
        grade = "A+"
elif average >= 75:
        grade = "A"
elif average >= 60:
        grade = "B"
elif average >= 50:
        grade = "C"
else:
     grade = "Fail"

student = {
        "name": name,
        "roll": roll,
        "maths": maths,
        "science": science,
        "social": social,
        "total": total,
        "average": average,
        "grade": grade
    }

students.append(student)
print("Student added successfully!")
print("Grade:", grade)

add_student()
student1={
      "name": "doremon",
     "roll": "101",
     "maths": 90,
     "science": 85,
     "social": 88,
     "total": 263,
     "grade": "A+"
}
student2={

    "name": "ninja",
    "roll": "102",
    "maths": 80,
    "science": 79,
    "social": 74,
    "total": 253,
    "grade": "A"
 }
student3={
    "name": "oggy",
    "roll": "103",
    "maths": 60,
    "science": 65,
    "social": 68,
    " total": 193,
    "grade": "B"

}
student4={

      "name": "vikash",
      "roll": "104",
      "maths": 50,
      "science": 55,
      "social": 58,
      "total": 195,
      "grade": "C"
}
students.append(student1)
print("ALL THE RECORDS")
print(s)


students = ["doremon","ninja","oggy","vikash"]
for student in students:
    print("students name:",student)

students =[

{
     "name": "doremon",
      "roll": "101",
      "maths": 90,
      "science": 85,
      "social": 88,
      "total": 263,
      "grade": "A+"
},
{
    "name": "ninja",
    "roll": "102",
    "maths": 80,
    "science": 79,
    "social": 74,
    "total": 253,
    "grade": "A"
},
{
    "name": "oggy",
    "roll": "103",
    "maths": 60,
    "science": 65,
    "social": 68,
    " total": 193,
    "grade": "B"
},
{

      "name": "vikash",
      "roll": "104",
      "maths": 50,
      "science": 55,
      "social": 58,
      "total": 195,
      "grade": "C"
}

]
students =[]

if  not students:
    print("no students record found")
else:
    for student in students:
        total= student ["maths"] + student ["science"] + ["social"]
        

students = [
    {"roll": 101, "name": "doremon", "maths": 90, "science": 85, "social": 88, "grade": "A+"},
    {"roll": 102, "name": "ninja", "maths": 70, "science": 65, "social": 75, "grade": "A"},
    {"roll": 103, "name": "oggy", "maths": 60, "science": 55, "social": 58, "grade": "B"},
    {"roll": 104, "name": "vikash", "maths": 55, "science": 50, "social": 58, "grade": "C"}
]

roll_to_search = int(input("Enter roll number to search: "))
print("Searching for roll number:", roll_to_search)

if student["roll"] == roll_to_search:
         total = student["maths"] + student["science"] + student["social"]
         average = total / 3

print("Student Report Card")
print("")
print("Name       :", student["Name"])
print("Roll No.   :", student["roll"])
print("Maths      :", student["maths"])
print("Science    :", student["science"])
print("Social     :", student["social"])
print("Total Marks:", total)
print("Grade      :", student["grade"])
print(" ")

if not found:
     print("No student found with that roll number")

students = [
    {"name": "doremon", "roll": "101", "maths": 85, "science": 90, "social": 88},
    {"name": "ninja", "roll": "102", "maths": 78, "science": 84, "social": 80},
    {"name": "oggy", "roll": "103", "maths": 62, "science": 69, "social": 65},
    {"name": "vikash", "roll": "104", "maths": 50, "science": 59, "social": 55}
]

roll_to_delete = input("Enter the roll number of the student to delete: ")
found = False
for student in students:
    if student["roll"] == roll_to_delete:
        students.remove(student)
        found = True
        print(f"Student with roll number {roll_to_delete} has been deleted")
        break
if not found:
    print("Error: Student with that roll number not found")

for s in students:
    print(s)

def print_report_card(student):
    total = student["maths"] + student["science"] + student["social"]
    average = total / 3

    if average >= 90:
        grade = "A+"
    elif average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "Fail"

print("STUDENT REPORT CARD")
print(" ")
print(f"Name       : {student['name']}")
print(f"Roll No.   : {student['roll']}")
print(f"Maths      : {student['maths']}")
print(f"Science    : {student['science']}")
print(f"Social     : {student['social']}")
print(" ")
print(f"Total      : {total}")
print(f"Average    : {round(average, 2)}")
print(f"Grade      : {grade}")
print(" ")
