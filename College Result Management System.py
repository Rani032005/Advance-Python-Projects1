students = {}

def add_result():
    name = input("Student name: ")
    marks = int(input("Marks: "))
    gpa = marks / 10
    students[name] = gpa

def show_results():
    for name, gpa in students.items():
        print(name, "GPA:", gpa)

while True:
    print("\n1.Add Result\n2.Show Results\n3.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        add_result()
    elif ch == 2:
        show_results()
    else:
        break