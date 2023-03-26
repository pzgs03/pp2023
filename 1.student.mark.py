
#Input number of students in a class
def number_of_students(number):
    number = int(input("The number of students in a class: "))
    return number

#Input student information: id, name, DoB
def students_information(n):
    students = []
    for i in range (n):
        id = str(input("Student's id: "))
        name = str(input("Student's name: "))
        DoB = str(input("Student's DoB: "))
        students.append({
            'id':id,
            'name':name,
            'DoB':DoB
        })

#Input number of courses
def number_of_courses(numberc):
    numberc = int(input("The number of courses: "))
    return numberc

#Input course information: id, name
def courses_information(n):
    courses = []
    for i in range (n):
        idc = str(input("Id of course: "))
        namec = str(input("Name of course: "))
        courses.append({
            'idc':idc,
            'namec':namec
        })

#Select a course, input marks for student in this course
def input_mark():
    students_information["marks"] = {}
    # TODO: check mark in student or not
    # If not, enter the mark for the course


#List courses
def list_courses(n):
    if n == 0:
        print("There aren't any courses yet")
    else:  
        print("Here is the course list: ")
        for course in courses_information(n): 
            print(f"{course['idc']} {course['namec']}")

#List students
def list_students(n):
    if n == 0:
        print("There aren't any students")
    else:
        print("Here is the student list: ")
    for students in students_information(n):
        print(f"{students['id']} - {students['name']} - {students['DoB']}")
    if "marks" in students_information(n):
        print("Marks (Course Id - Mark): ", end="")   
 
# Main function 
def main():
    courses = []
    students = []
    num_students = 0
    num_courses = 0

    while(True):
        print("""
        '0. Exit',       
        '1. Input number of students in a class',
        '2. Input student information: id, name, DoB',
        '3. Input number of courses',
        '4. Input course information: id, name',
        '5. List courses',
        '6. List students',
        '7. Select a course, input marks for student in this course'
    """)
        option = int(input("Your choice: "))                                                        
        if option == 0:
            break
        elif option == 1:                                                                           
            number_of_students(num_students)
        elif option == 2:
            students_information(number_of_students(num_students))
        elif option == 3: 
            number_of_courses(num_courses)                                                                            
        elif option == 4:                                                                                                                          
            courses_information(number_of_courses(num_courses))
        elif option == 5:                                                                                                                           
            list_courses(number_of_courses(num_courses))
        elif option == 6:                                                                                                                         
            list_students(number_of_students(num_students))
        elif option == 7:                                                                                                                              
            input_mark()
        else:
            print("Invalid")

# Call the main function
if __name__ == "__main__":
    main()
