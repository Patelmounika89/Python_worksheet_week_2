students=["Mounik","kavya","Shirisha","Sneha","Snigdha"]
with open("students.txt","w")as file:
    for student in students:
        file.write(student +"\n")
    
with open("students.txt","r")as file:
    names=file.read()
    name=names.split()
    total_names=len(name)
    print("Students Names")
    print(names)
    print("Toatal Names:",total_names)