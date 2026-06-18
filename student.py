# student.py

class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def to_dict(self):
        """Convert student object to dictionary for JSON saving."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "grade": self.grade
        }

    @staticmethod
    def from_dict(data):
        """Create a Student object from a dictionary (for loading from JSON)."""
        return Student(data["student_id"], data["name"], data["grade"])

    def __str__(self):
        return f"| {self.student_id:<10} | {self.name:<20} | {self.grade:<5} |"