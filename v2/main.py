import json


def load_data():
    try:
        with open("students.json") as data:
            students_data = json.load(data)
            return students_data
    except FileNotFoundError:
        return {}


students = load_data()  # stores all student records


def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file)


def add_student():
    student_name = input("Enter student name: ").strip()

    if not student_name:
        print("Student name cannot be empty")
        return

    if student_name in students:
        print("Student already exists. Try a different name.")
    else:
        students[student_name] = {"marks": []}  # Store student with an empty marks list
        save_data()
        print("Student added successfully")


# Reusable search helper (no I/O)
def search_student(search):      
    if search in students:  
        return students[search]  # important: return found record for reuse 
    return None


def find_student():
    search = input("Enter student name: ").strip()

    student = search_student(search)  # pass input as argument

    if student is None:
        print("Student not found")
    
    return student  # return so other features can reuse this if needed


def add_marks():
    student_name = input("Enter student name: ").strip() 

    # Use search helper to avoid duplicate input handling
    student = search_student(student_name)

    if student is not None:  # checks if a valid record was returned (not None)
        try:
            marks = int(input("Enter marks: ")) 
        except ValueError:
            print("Invalid input")
            return

        if marks < 0 or marks > 100:
            print("Marks should be between 0 and 100")
            return
        
        student["marks"].append(marks)  # add new marks to the student's marks list
        save_data()
        print("Marks added successfully")
    else:
        print("Student not found")


# Reusable calculate average helper (no I/O)
def calculate_average_logic(student):
    marks = student["marks"]

    if not marks:
        return None
    
    return sum(marks) / len(marks)
   

def calculate_average():
    student_name = input("Enter student name: ").strip()

    student = search_student(student_name)

    if student is None:
        print("Student not found")
        return
    
    avg = calculate_average_logic(student)

    if avg is None:
        print("No marks available")
        return   
        
    print("Average:", avg)


# Reusable assign grade helper (no I/O)
def assign_grade_logic(average):

    if average is None:  # Handle case where no marks exist
        return None
    
    # Assign grade based on average marks range
    if (average >= 90):
        return "A"
    elif (average >= 75):
        return "B"
    elif (average >= 60):
        return "C"
    else:
        return "D"


def assign_grade():
    student_name = input("Enter student name: ").strip()

    student = search_student(student_name)

    if student is None:
        print("Student not found")
        return
    
    average = calculate_average_logic(student)
    grade = assign_grade_logic(average)

    if grade is None:
        print("No marks available")
        return
            
    print("Grade:", grade)


def display_report():
    student_name = input("Enter student name: ").strip()

    student = search_student(student_name)
    
    if student is None:
        print("Student not found")
        return
    
    print("\n--- Student Report ---")
    print("Name:", student_name)
    print("Marks:", student["marks"])

    average = calculate_average_logic(student)
    grade = assign_grade_logic(average)

    if average is None:
        print("No marks available")
        return
        
    print("Average:", average)
    print("Grade:", grade)


def delete_student():
    student_name = input("Enter Student name to delete: ").strip()

    student = search_student(student_name)  # get student record (or None if not found)

    if student is not None:
        del students[student_name]  # remove entire student record from dictionary using student_name as key
        save_data()
        print("Student deleted successfully")
    else:
        print("Student not found")


def view_students():
    if not students:  # checks if the dct is empty
        print("No students available")
    else:      
        print("All Students Data: ")  
        for student_name in students: 
            print("Name:", student_name, ", Marks:", students[student_name]["marks"])


# Menu System: runs continuously until user chooses to exit
print("---Menu Options---")

while True:  # infinite loop to keep CLI program running
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

    choice = input("Enter choice: ").strip()  # take user input

    if not choice:
        print("Choice cannot be empty")
        continue  # skip rest of loop and ask for input again

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
        print("Exiting program...")
        break  # terminate loop and end program

    else:
        print("Invalid choice")  # handle incorrect input