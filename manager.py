# manager.py

import json
import os
from student import Student

FILE_PATH = "students.json"

class StudentManager:
    def __init__(self):
        self.students = {}  # key: student_id, value: Student object
        self.load_from_file()

    # ---------- File I/O ----------

    def load_from_file(self):
        """Load students from JSON file on startup."""
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, "r") as f:
                data = json.load(f)
                for record in data:
                    s = Student.from_dict(record)
                    self.students[s.student_id] = s
        else:
            self.students = {}

    def save_to_file(self):
        """Save all students to JSON file."""
        with open(FILE_PATH, "w") as f:
            json.dump([s.to_dict() for s in self.students.values()], f, indent=4)

    # ---------- CRUD Operations ----------

    def add_student(self, student_id, name, grade):
        """Add a new student with unique ID validation."""
        if student_id in self.students:
            print(f"\n❌ Error: Student ID '{student_id}' already exists!")
            return False
        if not student_id or not name or not grade:
            print("\n❌ Error: All fields (ID, name, grade) are required!")
            return False

        self.students[student_id] = Student(student_id, name, grade)
        self.save_to_file()
        print(f"\n✅ Student '{name}' added successfully!")
        return True

    def update_student(self, student_id, name=None, grade=None):
        """Update name and/or grade of an existing student."""
        if student_id not in self.students:
            print(f"\n❌ Error: Student ID '{student_id}' not found!")
            return False

        student = self.students[student_id]
        if name:
            student.name = name
        if grade:
            student.grade = grade

        self.save_to_file()
        print(f"\n✅ Student '{student_id}' updated successfully!")
        return True

    def delete_student(self, student_id):
        """Delete a student by ID."""
        if student_id not in self.students:
            print(f"\n❌ Error: Student ID '{student_id}' not found!")
            return False

        name = self.students[student_id].name
        del self.students[student_id]
        self.save_to_file()
        print(f"\n✅ Student '{name}' deleted successfully!")
        return True

    def list_students(self):
        """Print all students in a formatted table."""
        if not self.students:
            print("\n⚠️  No students found.")
            return

        print("\n" + "=" * 45)
        print(f"| {'ID':<10} | {'Name':<20} | {'Grade':<5} |")
        print("=" * 45)
        for student in self.students.values():
            print(student)
        print("=" * 45)
        print(f"  Total students: {len(self.students)}")

    def search_student(self, student_id):
        """Search for a student by ID."""
        if student_id in self.students:
            print("\n" + "=" * 45)
            print(f"| {'ID':<10} | {'Name':<20} | {'Grade':<5} |")
            print("=" * 45)
            print(self.students[student_id])
            print("=" * 45)
        else:
            print(f"\n❌ Student ID '{student_id}' not found!")