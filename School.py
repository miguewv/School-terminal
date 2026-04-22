import os
import time

print("Welcome to the school terminal!")
time.sleep(2)

classroom = {"Victor": [0, 2], "Samuel": [2, 3]}


def main():
    def register_student(student):
        classroom[student] = []
        main()

    def view_classroom_students():
        for student in classroom.keys():
            print(student)
        time.sleep(5)
        main()

    def add_grade(student, grade: int):
        for current_student in classroom.keys():
            if current_student == student:
                classroom[current_student].append(grade)
                print("Grade added to the student.")
                time.sleep(3)
                main()
        else:
            print("Student not found.")
            time.sleep(3)
            main()

    def view_student_grades(student):
        for current_student in classroom.keys():
            if current_student == student:
                print(classroom[current_student])
                time.sleep(3)
                main()
        else:
            print("Student not found.")
            time.sleep(3)
            main()

    def number_of_students():
        print(len(classroom))
        time.sleep(3)
        main()

    os.system("cls")
    print("Choose an option:")
    print("1: Register a student in the classroom")
    print("2: View students registered in the classroom")
    print("3: Add a grade to a student")
    print("4: View a student's grades")
    print("5: Number of students in the classroom")
    choice = input("Choose a number: ")

    if choice == "1":
        print("What is the name of the student you want to register?")
        student_name = input()

        register_student(student_name)

    elif choice == "2":
        view_classroom_students()

    elif choice == "3":
        print("Which student do you want to add a grade to?")
        student = input()

        print("What grade do you want to add to this student?")
        grade = input()

        add_grade(student, int(grade))

    elif choice == "4":
        print("Which student's grades do you want to see?")
        student_grades = input()

        view_student_grades(student_grades)

    elif choice == "5":
        number_of_students()

    else:
        print("Choose a number from the list!")
        time.sleep(1)
        os.system("cls")
        main()


main()
