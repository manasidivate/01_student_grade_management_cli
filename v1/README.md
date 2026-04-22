# 🎓 Student Grade Management System (CLI)

This is a simple command-line based application built using Python to manage student records and their marks.

I built this project as part of my backend learning journey to understand how real-world data can be structured, updated, and processed step by step — not just written as code, but designed logically.

---

## 🚀 What this project can do

The system allows you to:

- Add a new student  
- Search for a student (using reusable logic)  
- Add marks to a specific student  
- Calculate average marks  
- Assign grades based on performance  
- Display a complete student report  
- Delete a student record  
- View all students  

Everything runs through a menu-driven interface, so the flow feels structured and interactive.

---

## 🧠 How I approached this

Instead of writing everything in one place, I focused on:

- Breaking features into functions  
- Reusing logic wherever possible (like the `search_student` helper)  
- Avoiding repeated input handling  
- Keeping the flow simple but structured  

For example, searching a student is separated as a helper function so it can be reused in multiple features like adding marks, calculating average, etc.

---

## 🛠️ Tech Used

- Python  
- Lists (for storing records)  
- Functions  
- Basic control flow (loops, conditionals)

---

## 📂 Project Structure (simple and focused)

This project is intentionally kept minimal to focus on core logic and problem-solving:

- `main.py` → contains the entire CLI system and feature implementation  

---

## ▶️ How to run

1. Clone the repository
```
git clone https://github.com/manasidivate/student-grade-management-system-cli.git
```

2. Go to the project folder
```
cd student-grade-management-system-cli
```

3. Run the program
```
python main.py
```

---

## 🖥️ Sample Run

```
---Menu Options---

1. Add Student
2. Find Student
3. Add Marks
4. Calculate Average
5. Assign Grade
6. Display Report
7. Delete Student
8. View Students
9. Exit Program

Enter choice: 1
Enter student name: John
Student added successfully

Enter choice: 3
Enter student name: John
Enter marks: 85
Marks added successfully

Enter choice: 6
Enter student name: John
Student name: John
Student marks: [85]
Average marks: 85.0
Grade: B
```

This is a simple example to show how the system behaves when interacting through the CLI.

---

## 📌 What I learned from this project

- Structuring data (students + marks)
- Writing reusable functions
- Avoiding redundant code
- Handling edge cases (like no marks / student not found)
- Building a complete CLI workflow from scratch

---

## 🔄 Next Version

For the next version of this project, I plan to improve it further by:

- Improving the data structure to make the code more clear and scalable  
- Storing data using files or a database instead of runtime memory  
- Improving input validation and handling edge cases better  
- Structuring the code into multiple modules for better readability  
- Exploring a GUI-based version for better user interaction  

This version focuses on getting the logic right. The next version will focus more on structure and scalability.

---

## 💭 Final note

This project may look simple, but it helped me shift from just "writing Python code" to actually "building something with logic and structure".

And that’s the direction I’m continuing in.