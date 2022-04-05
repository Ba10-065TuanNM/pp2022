import math
from audioop import reverse
from unicodedata import name
from itertools import count
from numpy import average, double
from numpy import number

class Student:
    def __init__(self,id,name,dob):
        self.id = id
        self.name = name
        self.dob = dob 
        self.listMark = list()

    def getStudentName(self):
        return self.name

    def setcourseMark(self,course,mark):
        courseMark = {
            "course" : course,
            "mark" : mark
        }
        self.listMark.append(courseMark)

    def getAverage(self):
        sumMark = 0;
        for courseMark in self.listMark:
            sumMark += courseMark["Markk"]
        average = sumMark/len(self.listMark)
        return math.floor(average*10)/10
    
    def display(self):
        print("Id:    ", self.id)
        print("Name:    ", self.name)
        print("Date of birth:   ", self.dob)
        print("Mark:    ", self.listMark)
        print("Average:     ",self.getAverage())
        print("****: ",len(self.listMark))
        print("----------------------------")

class Course:
    def __init__(self,id,name):
        self.id = id
        self.nameC = name

    def getName(self):
        return self.nameC

    def display(self):
        print("Id Course:   ", self.id)
        print("Name Course:     ",self.nameC)
        print("----------------------------")


def inputStudent(listStudent):
    numStudent = int(input("Number of student:     "))
    for index in range (0, numStudent):
        id = int(input("Id student" + str(index+1) + ": "))
        name = str(input("Name of student   " + str(index+1) + ":   "))
        date = str(input("Date of " + str(index+1) + ": "))
        listStudent.append(Student(id, name, date))

def inputCourse(listCourse):
    numCourse = int(input("Number of course:     "))
    for index in range (0, numCourse):
        id = int(input("Id Course" ))
        name = str(input("Name of Course   " ))
        listCourse.append(Course(id,name))

def listMark(mark):
    mark.list()

def inputMark(listStudent,listCourse):
    for course in listCourse:
        for student in listStudent:
            mark = float(input("Mark:   "+ student.getName()+ "for   "+course.getName()+":   "))

def sortaverageMark(listStudent,mark):
    return listStudent.sortaverageMark(mark)

def sortaverage(listStudent):
    listStudent.sort(key=lambda student: student.getaverage(),reverse = False)

def Main():
    listStudent = list()
    listCourse = list()
    inputStudent(listStudent)
    inputCourse(listCourse)
    inputMark(listStudent, listCourse)
    for student in listStudent:
        student.display()
Main();