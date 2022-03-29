class Student:
    def __init__(self,Id,Name,Dob):
        self.Id = Id
        self.Name = Name
        self.Dob = Dob
        self.Mark = {}

    def displayStudent(self):
        print("***************************")
        print("Enter ID Student:    " + self.Id)
        print("Enter Student Name:  " + self.Name)
        print("Enter Student Date of Birth: " + self.Dob)
        print("***************************")

    def getInputId(self):
        return self.Id
    def setInputId(self, Id):
        self.Id = Id

    def getInputName(self):
        return self.Name
    def setInputName(self, Name):
        self.Name = Name

    def getInputDob(self):
        return self.Dob
    def setInputDob(self, Dob):
        self.Dob = Dob

    def getMark(self):
        return self.Mark
    def setMark(self, Course, Mark):
        self.Mark.update({Course: Mark})

    def displayStudentMark(self,course):
        print(self.Name + " : " + str(self.Mark.get(course)))

class Course:
    def __init__(self, Id, Name):
        self.Id = Id
        self.Name = Name

    def displayCourse(self):
        print("**********************************")
        print("Enter ID Course:    " + self.Id)
        print("Enter Student Course:  " + self.Name)
        print("**********************************")


    def getCoId(self):
        return self.Id
    def setCoId(self,Id):
        self.Id = Id

    def getCoName(self):
        return self.Name
    def setCoName(self,Name):
        self.Name = Name

def numStudent():
    while True:
        try:
            print("________________________________")
            numStudent = int(input("Enter Number of Student:    "))
            print("________________________________")
            return numStudent
        except ValueError:
            print("Invalid number.")
            print("________________________________")

def infoStudent():
    print("________________________________")
    stuId = input("Enter Student ID:    ")
    stuName = input("Enter Student Name:    ")
    stuDob = input("Enter Student Date of Birth:    ")
    print("________________________________")
    return stuId, stuName, stuDob

def numCourse():
    while True:
        try:
            print("________________________________")
            numcourse = int(input("Enter Number of Course:  "))
            print("________________________________")
            return numcourse
        except ValueError:
            print("That's wrong number. ")
            print("________________________________")

def infoCourse():
    print("________________________________")
    courseId = input("Enter Course ID:    ")
    courseName = input("Enter Course Name:    ")
    print("________________________________")
    return courseId, courseName

def findCoName(cos,courseId):
    for course in cos:
        if course.getCoId() == courseId:
            return course.getCoName()
    print("Error")
    print("________________________________")

if __name__ == "__main__":
    stus = []
    cos = []

    student_num = numStudent()
    print(student_num)
    for i in range (0,student_num):
        Id, Name, Dob = infoStudent()
        stus.append(Student(Id, Name, Dob))

    couse_num = numCourse()
    for i in range (0,couse_num):
        Id, Name = infoCourse()
        cos.append(Course(Id, Name))

    print("ListStudents")
    for student in stus:
        student.displayStudent()

    print("ListCourse")
    for course in cos:
        course.displayCourse()

    x ='y'
    while x== 'y':
        sel_courseId = input("Select Course ID:    ")
        sel_course = findCoName(cos, sel_courseId)
        print("Name Course:"+ sel_course )
        for student in stus:
            mark = input("Enter " + student.Name + "mark:")
            student.setMark(sel_course, mark)
        x = input("Wanna choose another? (y/n):")
        print("________________________________")

    sel_courseId = input("Select Id Course:    ")
    sel_course = findCoName(cos,sel_courseId)
    print(f"Mark of Student {sel_course} : \n")
    for student in stus:
        student.displayStudentMark(sel_course)



    
    