from input import *
from output import *
from domain import *

def Main():
    listStudent = list()
    listCourse = list()
    inputStudent(listStudent)
    inputCourse(listCourse)

    inputMark(listStudent, listCourse)

    for student in listStudent:
        student.display()

    averageMark(listStudent)

    for student in listStudent:
        student.display()

Main();

