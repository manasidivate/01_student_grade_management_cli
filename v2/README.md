# 🎓 Student Grade Management System (CLI) — Version 2

This is an improved version of my command-line based Student Grade Management System built using Python.

In this version, I focused not just on making the system work, but on structuring the code properly, improving data handling, and making the program more robust and reusable.

---

## 🚀 What this project can do

The system allows you to:

- Add a new student  
- Search for a student using reusable logic  
- Add marks to a student with proper validation  
- Calculate average marks  
- Assign grades based on performance  
- Display a structured student report  
- Delete a student record  
- View all students  

The application runs through a menu-driven interface, making it easy to interact with step by step.

---

## 🧠 What’s improved in Version 2

Compared to the earlier version, this version focuses more on code quality and system design:

- Separated logic into helper functions (`calculate_average_logic`, `assign_grade_logic`)  
- Avoided repeating logic by reusing functions across features  
- Added input validation (empty input, invalid marks, range checks)  
- Used `.strip()` consistently to handle user input properly  
- Improved control flow using `continue` for cleaner menu handling  
- Cleaned and simplified code structure for better readability  

This version reflects a shift from just writing code to designing a structured system.

---

## 🛠️ Tech Used

- Python  
- Dictionaries (for storing student data)  
- JSON (for persistent storage)  
- Functions  
- Control flow (loops, conditionals, exception handling)  

---

## 📂 Project Structure

- `main.py` → contains the full CLI system and logic  
- `students.json` → stores student data persistently  

---

## ▶️ How to run

1. Clone the repository  

git clone https://github.com/manasidivate/student-grade-management-system-cli.git


2. Go to the project folder  

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
- Avoiding duplicate code through function reuse  
- Handling user input safely (validation + exception handling)  
- Structuring a program step-by-step like a real system  
- Improving code readability and maintainability  

---

## 🔄 What I plan next

- Further modularizing the code into multiple files  
- Improving output formatting and user experience  
- Exploring database integration instead of JSON  
- Building a GUI version for better interaction  

---

## 💭 Final note

This version helped me move from just writing working code to thinking in terms of structure, flow, and reusability.

It’s a small project, but it reflects how I’m approaching backend development s