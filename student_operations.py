students = []  # stores all student records


# add student
def add_student():
    student_name = input("Enter student name: ")

    # student structure: [name, marks_list]
    student = [student_name, marks := []]

    students.append(student)
    print("Student added successfully")

# Helper function: reusable search logic (no user input here)
def search_student(search):      
    for student in students:
        if student[0] == search:  # access name field (index 0)
            print("Student Found:", student)
            return student       # important: return found record for reuse
    else:  # runs only if no match was found in the loop
        print("Student Not Found")

# find Student (handles user input + uses helper)
def find_student():
    search = input("Enter student name: ")
    student = search_student(search)   # pass input as argument
    return student    # return so other features can reuse this if needed

# Add Marks
def add_marks():
    student_name = input("Enter student name: ") 

    # directly using helper instead of find_student() to avoid duplicate input
    student = search_student(student_name)
    if student:     # checks if a valid record was returned (not None)
        marks = int(input("Enter marks: "))
        student[1].append(marks)     # index 1 stores marks list
        print("Marks added successfully")
    else:
        print("Student not found")

# Calculate and display average marks of a student
def calculate_average():
    student_name = input("Enter student name: ")
    student = search_student(student_name)

    if student:
        marks = student[1]      # Extract marks list

        # Check if marks list is empty
        if not marks:
            print("No marks available")
        else:
            average = sum(marks) / len(marks)
            print("Average marks:", average)
            return average
    else:
        print("Student not found")

# Assign grade based on student's average marks
def assign_grade():
    # Get average marks from calculate_average function
    average = calculate_average()
    
    # Safety check: if average couldn't be calculated (None), exit function
    if average is None:
        return
    
    # Assign grade based on average marks range
    if (average >= 90):
        print("Grade = A")
    elif (average >= 75):
        print("Grade = B")
    elif (average >= 60):
        print("Grade = C")
    else:
        print("Grade = D")

# Display report
def display_report():
    student = find_student()   # get student record (or None if not found)

    if student:
        print("Student name:", student[0])  # index 0 -> name
        print("Student marks:", student[1]) # index 1 -> marks list

        marks = student[1]     # calculate_average function repeated

        if not marks:
            print("No marks available")
        else:
            average = sum(marks) / len(marks)
            print("Average marks:", average)

            if (average >= 90):    # assign_grade function repeated
                grade = "A"
            elif (average >= 75):
                grade = "B"
            elif (average >= 60):
                grade = "C"
            else:
                grade = "D"

            print("Grade:", grade)

# Delete student
def delete_student():
    student = find_student()  # get student record (or None if not found)

    if student:
        students.remove(student)   # remove matched student object from list
        print("Student deleted successfully")
    else:
        print("Student not found")

# View students
def view_students():
    if not students:   # checks if the list is empty
        print("No students available")
    else:      
        print("List of students: ")
        for student in students:   # loop through each student in the list
            print("Student name:", student[0])
            print("Marks:", student[1])


# Menu System: runs continuously until user chooses to exit
print("---Menu Options---")

while True:   # infinite loop to keep CLI program running
    # display available operations
    print("1. Add Student")
    print("2. Find Student")
    print("3. Add Marks")
    print("4. Calculate Average")
    print("5. Assign Grade")
    print("6. Display Report")
    print("7. Delete Student")
    print("8. View Students")
    print("9. Exit Program")

    choice = input("Enter choice: ")   # take user input

    # route user choice to corresponding feature
    if choice == "1":
        add_student()

    elif choice == "2":
        find_student()

    elif choice == "3":
        add_marks()

    elif choice == "4":
        calculate_average()

    elif choice == "5":
        assign_grade()

    elif choice == "6":
        display_report()

    elif choice == "7":
        delete_student()

    elif choice == "8":
        view_students()

    elif choice == "9":
        print("-Exiting program-")
        break       # terminate loop and end program

    else:
        print("Invalid choice")   # handle incorrect input