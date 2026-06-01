# Student Record System using Dictionary
student = {}
student["Name"] = input("Enter student name: ")
student["Roll No"] = input("Enter roll number: ")
student["Marks"] = input("Enter marks: ")

print("\nStudent Record")

for key, value in student.items():
    print(key, ":", value)