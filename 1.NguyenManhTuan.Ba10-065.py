print("         Mark management         ")
 
def addStudent():
    print("Add a student")
    # List of student
    global listStudents
    infor = {
        'id' : '',
        'name' : '',
        'dob' : '',
    }  
    # Input id
    print("Student ID:")
    id = input()
    while True:
        student = findStudent(id)
        if student != False:
            print("ID already exist:")
            id = input()
        else:
            break
    infor['id'] = id
    # Input name
    print("Student name:")
    infor['name'] = input()
    #Input Dob
    print("Student Date of birth:")
    infor['dob'] = input()
    print('----------------------------------')
    # Save to list
    listStudents.append(infor)
def addCourse():
    print("Add a course")
    # List of course
    global listCourse
    infor = {
        'id' : '',
        'name' : ''
    }
    # Input id
    print("Course ID:")
    id = input()
    while True:
        course = findCourse(id)
        if course != False:
            print("ID already exist:")
            id = input()
        else:
            break
    infor['id'] = id
    # Input name
    print("Course name:")
    infor['name'] = input()
    print('----------------------------------')
    # Save to list
    listCourse.append(infor)

def findStudent(id):
    global listStudents
    for i in range(0, len(listStudents)):
        if listStudents[i]['id'] == id:
            return [i, listStudents[i]]
    return False

def findCourse(id):
    global listCourse
    for i in range(0, len(listCourse)):
        if listCourse[i]['id'] == id:
            return [i, listCourse[i]]
    return False
 
def showStudents():
    print("List of Student")
    global listStudents
    for i in range(0, len(listStudents)):
        print("[",listStudents[i]['id'],"]", "[",listStudents[i]['name'],"]","[",listStudents[i]['dob'],"]",)

def showCourse():
    print("List of Course")
    global listCourse
    for i in range(0, len(listCourse)):
        print("[",listCourse[i]['id'],"]", "[",listCourse[i]['name'],"]",) 

def addMark():
    info = {
        'id' : '',
        'name' : '',
        'course' : '',
        'mark' : '',
    }
    info['id'] = listStudents[i]['id']
    info['name'] = listStudents[i]['name']
    info['course'] = nameco
    print("Enter Mark: ")
    info['mark'] = input()
    listMarks.append(info)
    print("[",listMarks[i]['id'],"]", "[",listMarks[i]['name'],"]", "[",listMarks[i]['course'],"]", "[",listMarks[i]['mark'],"]")

def showMark():
    print("Mark")
    global listMarks
    for i in range(0, len(listMarks)):        
        if i%len(listStudents)==0:
            print("--------------------------------")
            print(listMarks[i]['course'])
        print("[",listMarks[i]['id'],"]", "[",listMarks[i]['name'],"]", "[",listMarks[i]['course'],"]", "[",listMarks[i]['mark'],"]")

# Main
listStudents = []
listCourse = []
listMarks = []
action = 0
while action >= 0:
    if action == 1:
        print("Number of students in class: ")
        numstu= int(input())
        i = 1
        while i <= numstu:
            print('Information of student ', i)
            i += 1
            addStudent()
    elif action == 2:
        print("Number of course: ")
        numco= int(input())
        i = 1
        while i <= numco:
            print('Information course ', i)
            i += 1
            addCourse()
    elif action == 3:
        print("Select an id course:")
        for i in range(0, len(listCourse)):
            print("[",listCourse[i]['id'],"]", "[",listCourse[i]['name'],"]",)     
        id = input()
        course = findCourse(id)
        for i in range(0, len(listCourse)):
            if listCourse[i]['id'] == id:    
                nameco = listCourse[i]['name']  
        if course == False:
            print("Can't find the course ", id)
        else :
            i = 1
            for i in range(0, len(listStudents)):
                addMark()
    elif action == 4:
        showStudents()
    elif action == 5:
        showCourse()
    elif action == 6:
        showMark()
 
    print("     Functions:Press to choose")
    print("1: Add Stu")
    print("2: Add Course")
    print("3: Add Mark")
    print("4: List student")
    print("5: List course")
    print('6: Mark list')
    print("0: Out process")
    action = int(input())
    if action == 0:
        break