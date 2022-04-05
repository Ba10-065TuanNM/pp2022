from ast import NameConstant
import math
import input
import output

class Student:
    def __init__(self,name,id,dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.listMark = list()

    def getName(self):
        return self.name

    def setCourseMark(self, course, mark):
        courseMark = {
            "course" : course,
            "mark" : mark
        }
        self.listMark.append(courseMark)

    def getAverage(self):
        sumMark = 0;
        for courseMark in self.listMark:
            sumMark += courseMark["mark"]

        average = sumMark/len(self.listMark)
        return math.floor(average*10)/10

    def display(self):
        print("id:", self.id)
        print("name:", self.name)
        print("dob:",self.dob)
        print("List Mark:", self.listMark)
        print("Average:",self.getAverage())
        print("****", len(self.listMark))

class Course:
    def __init__(self,id,name):
        self.id = id
        self.nameC = name

    def getName(self):
        return self.nameC

    def display(self):
        print("Name C:",self.nameC)
        print("Num C: ",self.numberCourse)

