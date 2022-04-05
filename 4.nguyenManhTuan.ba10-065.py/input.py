import math
from unicodedata import name
import domain

def inputStudent(listStudent):
    numberStudent = int(input("Number of students:      "))

    for index in range(0, numberStudent):
        id = int(input("id"+str(index+1)+":"))
        name = str(input("name"+str(index+1)+":"))
        dob = str(input("dateofbirth"+str(index+1)+":"))

def inputCourse(listCourse):
    numberCourse = int(input("Number of course:     "))

    for index in range(0, numberCourse):
        id = int(input("id:     "))
        name = str(input("Name :        "))

def inputMark(listStudent, listCourse):
    for course in listCourse:
        for student in listStudent:
            mark = float(input("Mark:       "+ student.getName()+"for   "+course.getName()+":   "))
            student.setMark(course.getName(),math.floor(mark*10)/10)

def averageMark(listStudent):
    listStudent.sort(key=lambda student: student.getaverageMark(), reverse = False)