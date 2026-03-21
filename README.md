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

## 📌 What I learned from this project

- Structuring data (students + marks)
- Writing reusable functions
- Avoiding redundant code
- Handling edge cases (like no marks / student not found)
- Building a complete CLI workflow from scratch

---

## ✨ Future improvements

- Store data using files or database (instead of runtime list)
- Add validation for inputs
- Build a GUI version of this system
- Improve error handling and user experience

---

## 💭 Final note

This project may look simple, but it helped me shift from just "writing Python code" to actually "building something with logic and structure".

And that’s the direction I’m continuing in.