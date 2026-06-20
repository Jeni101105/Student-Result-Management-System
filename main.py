import csv


# Add Student
def add_student():

    name = input("Enter Student Name: ")

    try:
        mark1 = int(input("Enter Mark 1: "))
        mark2 = int(input("Enter Mark 2: "))
        mark3 = int(input("Enter Mark 3: "))

    except ValueError:
        print("Please enter valid marks")
        return

    total = mark1 + mark2 + mark3

    percentage = total / 3

    if percentage >= 90:
        grade = "A"

    elif percentage >= 75:
        grade = "B"

    elif percentage >= 50:
        grade = "C"

    else:
        grade = "Fail"

    with open("students.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            name,
            mark1,
            mark2,
            mark3,
            total,
            percentage,
            grade
        ])

    print("Student Added Successfully")


# View Students
def view_students():

    try:

        with open("students.csv", "r") as file:

            reader = csv.reader(file)

            print("\nName\tTotal\tPercentage\tGrade")
            print("-" * 50)

            found = False

            for row in reader:

                found = True

                print(
                    f"{row[0]}\t{row[4]}\t{float(row[5]):.2f}\t\t{row[6]}"
                )

            if not found:
                print("No student records found")

    except FileNotFoundError:

        print("No student records found")


# Search Student
def search_student():

    name_to_search = input("Enter Student Name: ")

    found = False

    try:

        with open("students.csv", "r") as file:

            reader = csv.reader(file)

            for row in reader:

                if row[0].lower() == name_to_search.lower():

                    print("\nStudent Found")
                    print("Name:", row[0])
                    print("Mark 1:", row[1])
                    print("Mark 2:", row[2])
                    print("Mark 3:", row[3])
                    print("Total:", row[4])
                    print("Percentage:", row[5])
                    print("Grade:", row[6])

                    found = True

                    break

        if not found:

            print("Student Not Found")

    except FileNotFoundError:

        print("No student records found")


# Main Menu
while True:

    print("\n===== STUDENT RESULT MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")