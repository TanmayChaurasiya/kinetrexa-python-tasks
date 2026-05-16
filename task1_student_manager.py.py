# task1_student_manager.py

# A global list to store our student records (each student will be a dictionary)
students = []

def display_menu():
    """Displays the main menu options."""
    print("\n" + "="*30)
    print("🎓 STUDENT MANAGEMENT SYSTEM")
    print("="*30)
    print("1. Add a New Student")
    print("2. View All Students")
    print("3. Delete a Student")
    print("4. Exit")
    print("="*30)

def add_student():
    """Takes user input to add a new student to the list."""
    print("\n--- Add Student ---")
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    
    # Create a dictionary for the student and add it to our list
    student_data = {"roll_no": roll_no, "name": name, "course": course}
    students.append(student_data)
    
    print(f"✅ Success: Student '{name}' added successfully!")

def view_students():
    """Loops through the student list and prints them clearly."""
    print("\n--- Student Records ---")
    if len(students) == 0:
        print("⚠️ No students found. Please add some first.")
    else:
        # Increased spacing: 15 for Roll No, 25 for Name, 20 for Course
        print(f"{'Roll No':<15} | {'Name':<25} | {'Course':<20}")
        print("-" * 65)
        for student in students:
            print(f"{student['roll_no']:<15} | {student['name']:<25} | {student['course']:<20}")
def delete_student():
    """Deletes a student based on their Roll Number."""
    print("\n--- Delete Student ---")
    if len(students) == 0:
        print("⚠️ No students available to delete.")
        return

    roll_to_delete = input("Enter the Roll Number of the student to delete: ")
    
    # Loop through the list to find the student
    for i in range(len(students)):
        if students[i]["roll_no"] == roll_to_delete:
            deleted_name = students[i]["name"]
            del students[i]  # Remove the student from the list
            print(f"✅ Success: Student '{deleted_name}' has been deleted.")
            return # Exit the function after deleting
            
    print(f"❌ Error: Student with Roll Number '{roll_to_delete}' not found.")

def main():
    """Main loop that drives the CLI program."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            print("\nExiting the Student Management System. Goodbye! 👋")
            break  # Breaks the loop and ends the program
        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 4.")

# This ensures the program runs automatically when the file is executed
if __name__ == "__main__":
    main()
