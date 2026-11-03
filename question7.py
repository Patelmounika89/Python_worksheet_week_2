students={
    "Vaishnavi":{"marks":85,"Grade":"A"},
    "Sneha":{"marks":92,"Grade":"A+"},
    "Swapna":{"marks":75,"Grade":"B+"},
    "Mounika":{"marks":95,"Grade":"A+"},
    "Priya":{"marks":65,"Grade":"B"},
}
print("student Records")
for  name,details in students.items():
    print("Name:",name)
    print("Marks:",details["marks"])
    print("Grade:",details["Grade"])
    print()
highest_student=""
highest_marks=0
for name,details in students.items():
    if details["marks"]>highest_marks:
       highest_marks= details["marks"]
       highest_student=name
print("Student with Highest Marks")
print("Name:",highest_student)
print("Marks:", highest_marks)
print("Grade:",students[highest_student]["Grade"])
