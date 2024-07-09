#intialize dictionary
student_grades= { }

#add a new student
def add_student(name, grade):
    student_grades[name] = grade
    #[prinsu] = 100
    print(f"Added {name} with a {grade}")
    #added prinsu with 100
    
#update a student
def update_student(name,grade):
    if name in student_grades:
        student_grades[name]=grade
        #prinsu = 200
        print(f"{name} grade is updated to {grade}")
    else:
        print(f"{name} does not exist")
        
#delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} is deleted")
    else:
        print(f"{name} does not exist")
        
#view a student
def display_all_student():
    if student_grades:
        for name,grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("No student found/added")
        
def main ():
    while True:
        print("\n Student Grade Management System")
        print("1. Add a student")                                                                                                  
        print("2. Update a student")                                                                                                  
        print("3. Delete a student")                                                                                                  
        print("4. View a student")                                                                                                  
        print("5. Exit")       
        
        choice=int(input("Enter your choice:"))
        
        if choice == 1:
            name=input("Enter student name:")
            grade=int(input("Enter student grade:"))
            add_student(name, grade)
        
        elif choice == 2:
            name=input("Enter student name:")
            grade=int(input("Enter student grade:"))
            update_student(name, grade)
        
        elif choice == 3:
            name=input("Enter student name:")
            delete_student(name)
            
        elif choice == 4:
            display_all_student()
            
        elif choice == 5:
            print("Closing the program")
            break
            
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()