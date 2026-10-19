"""
Operations to be done:
    add
    update
    delete
    view
    exit
"""
#! Initialising dictionary
student_marks = {}

#! Add a new student
def add_student(name, marks):
    student_marks[name] = marks
    print(f"Added {name} with {marks}")

#! Update a student
def update_student(name, marks):
    if name in student_marks:
        student_marks[name] = marks
        print(f"{name} with marks are updated {marks}")
    else:
        print(f"{name} not found!")

#! Delete student
def delete_student(name):
    if name in student_marks:
        del student_marks[name]
        print(f"{name} deleted succesfully")
    else:
        print(f"{name} not found!")

#! View all students marks
def display_all_students():
    if student_marks:
        for name, marks in student_marks.items():
            print(f"{name} : {marks}")
    else:
        print("No students data found")

def main():
    while True:
        print("\n Student Marks Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")

        choice = int(input("Enter your choice = "))
        if choice == 1:
            name = input("Enter student name: ")
            marks = float(input("Enter student marks: "))
            add_student(name, marks)

        elif choice == 2:
            name = input("Enter student name: ")
            marks = float(input("Enter student marks: "))
            update_student(name, marks)

        elif choice == 3:
            name = input("Enter student name: ")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Closing the program")
            break

        else:
            print("Invalid input")

if __name__ == "__main__":
    main()