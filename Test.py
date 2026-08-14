"""
Sample Python Program - Student Grade Management System
Demonstrates: functions, classes, data structures, and file operations
"""

class Student:
    """Class to represent a student"""
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades
    
    def calculate_average(self):
        """Calculate average grade"""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def get_grade_letter(self):
        """Convert average to letter grade"""
        avg = self.calculate_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
    
    def __str__(self):
        avg = self.calculate_average()
        letter = self.get_grade_letter()
        return f"Student: {self.name} (ID: {self.student_id}) | Avg: {avg:.2f} | Grade: {letter}"


def display_students(students):
    """Display all students information"""
    print("\n" + "="*60)
    print("STUDENT GRADE REPORT")
    print("="*60)
    for student in students:
        print(student)
    print("="*60 + "\n")


def main():
    # Create sample students
    students = [
        Student("Alice Johnson", "S001", [85, 90, 88, 92]),
        Student("Bob Smith", "S002", [78, 82, 79, 81]),
        Student("Charlie Brown", "S003", [95, 93, 97, 94]),
        Student("Diana Prince", "S004", [88, 85, 90, 87])
    ]
    
    # Display all students
    display_students(students)
    
    # Find top student
    top_student = max(students, key=lambda s: s.calculate_average())
    print(f"Top Student: {top_student.name} with average {top_student.calculate_average():.2f}\n")


if __name__ == "__main__":
    main()
    print("Program completed successfully!")
