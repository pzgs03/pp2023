class Student_Infor:
    def __init__(self):
        self.__Name = str
        self.__ID = str
        self.__DoB = str

    def get_Name(self):
        self.__Name = input("Enter name of the student: ")
        return self.__Name
    
    def get_ID(self):
        self.__ID = input("Enter ID of the student: ")
        return self.__ID
    
    def get_DoB(self):
        self.__DoB = input("Enter DoB of the student: ")
        return self.__DoB

class Course_Infor:
    def __init__(self):
        self.__Name = str
        self.__ID = str

    def get_Name(self):
        self.__Name = input("Enter name of the course: ")
        return self.__Name
    
    def get_ID(self):
        self.__ID = input("Enter ID of the course: ")
        return self.__ID   
    
class U:
    def input_st(args):
        return int(input(f"Enter the number of {args}: "))

    def show(list):
        for i in enumerate(list):
            return i

class Management:
    def __init__(self):
        self.__num_stds = 0
        self.__num_crs = 0
        self.__stds = []
        self.__crs = []


    def get_num_stds(self):
        return self.__num_stds
    
    def get_num_crs(self):
        return self.__num_crs
    
    def get_stds(self):
        self.Name = Student_Infor.get_Name(self)
        self.ID = Student_Infor.get_ID(self)
        self.DoB = Student_Infor.get_DoB(self)      
        return self.__stds

    def get_crs(self):
        self.Name = Course_Infor.get_Name(self)
        self.ID = Course_Infor.get_ID(self)
        return self.__crs

    def set_num_stds(self):
        self.num_stds = self.get_num_stds()
        self.__num_stds = U.input_st("students")           

    def set_num_crs(self):
        self.num_crs = self.get_num_crs()
        self.__num_crs = U.input_st("courses")

    def set_stds(self):
        self.stds = self.get_stds()
        self.__stds = U.input_st(self.get_stds())

    def set_crs(self):
        self.crs = self.get_crs()
        self.__crs = U.input_st(self.get_crs())   

    # Display a list of students
    def list_stds(self):
        print("Student list: ")
        U.show(self.get_stds())

    # Display a list of courses
    def list_crs(self):
        print("Course list: ")
        U.show(self.get_crs())


# Main function 
def main():

    mana = Management()

    while(True):
        print("""
        '0. Exit',       
        '1. Input number of students in a class',
        '2. Input student information: id, name, DoB',
        '3. Input number of courses',
        '4. Input course information: id, name',
        '5. List courses',
        '6. List students',
    """)
        option = int(input("Your choice: "))                                                        
        if option == 0:
            break
        elif option == 1:                                                                           
            mana.set_num_stds()
        elif option == 2:
            mana.set_stds()
        elif option == 3: 
            mana.set_num_crs()                                                                       
        elif option == 4:                                                                                                                          
            mana.set_crs()
        elif option == 5:                                                                                                                           
            mana.list_crs()
        elif option == 6:                                                                                                                         
            mana.list_stds()
        else:
            print("Invalid")

# Call the main function
if __name__ == "__main__":
    main()

 
