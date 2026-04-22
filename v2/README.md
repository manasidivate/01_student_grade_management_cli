# 🎓 Student Grade Management System (CLI) — Version 2

This is an improved and refactored version of the Student Grade Management System built using Python.

In this version, the focus was not just on implementing features, but on improving how the system is structured, how logic is organized, and how reliably it handles user input and data.

---

## 🚀 What this project does

The system allows you to:

- Add a new student  
- Search for a student using reusable logic  
- Add marks with proper validation  
- Calculate average marks  
- Assign grades based on performance  
- Display a structured student report  
- Delete a student record  
- View all students  

The application runs through a menu-driven interface for step-by-step interaction.

---

## 🧠 What’s improved in Version 2

Compared to Version 1, this version focuses more on structure, reusability, and reliability.

Key improvements include:

- Separation of core logic from user interaction  
- Reusable helper functions (`calculate_average_logic`, `assign_grade_logic`)  
- Reduced duplication by reusing functions across features  
- Input validation (empty input, invalid values, range checks)  
- Cleaner control flow using `continue` for menu handling  
- JSON-based persistent storage  
- Improved readability and overall code organization  

This version reflects a shift from writing feature-based code to designing a more structured and maintainable system.

---

## 🛠️ Tech Used

- Python  
- Dictionaries (for structured data storage)  
- JSON (for persistent storage)  
- Functions  
- Control flow (loops, conditionals, exception handling)  

---

## 📂 Project Structure

- `main.py` → contains the CLI system and feature logic  
- `students.json` → stores student data persistently  

---

## ▶️ How to run

1. Clone the repository  

git clone https://github.com/manasidivate/student-grade-management-system-cli.git


2. Navigate to the project folder  

cd student-grade-management-system-cli


3. Run the program  

python main.py


---

## 🖥️ Sample Run


---Menu Options---

Add Student
Find Student
Add Marks
Calculate Average
Assign Grade
Display Report
Delete Student
View Students
Exit Program

Enter choice: 1
Enter student name: John
Student added successfully

Enter choice: 3
Enter student name: John
Enter marks: 85
Marks added successfully

Enter choice: 4
Enter student name: John
Average: 85.0

Enter choice: 5
Enter student name: John
Grade: B

Enter choice: 6
Enter student name: John

--- Student Report ---
Name: John
Marks: [85]
Average: 85.0
Grade: B


---

## 📌 What I learned from this version

- Separating logic from user interaction  
- Writing reusable helper functions  
- Reducing duplication through better design  
- Handling user input safely (validation + exception handling)  
- Structuring programs more systematically  
- Improving readability and maintainability  


## 💭 Final Note

While the problem itself is straightforward, this version reflects an improvement in how I approach building software.

The focus has shifted from making the program work to designing it in a way that is cleaner, more structured, and easier to maintain.