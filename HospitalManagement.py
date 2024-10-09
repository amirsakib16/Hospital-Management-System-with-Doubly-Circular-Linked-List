class Patient:
    def __init__(self,prev,info,next):
        self.prev = prev
        self.info = info
        self.next = next
class WRM:
    dummy = Patient(None,None,None)
    head = dummy
    tail = dummy
    def __init__(self, id=None, name=None, age=None, bloodgroup=None):
        self.id = id
        self.name = name
        self.age = age
        self.bloodgroup = bloodgroup
        if id and name and age and bloodgroup:
            studentInfo = f"ID: {self.id}\nName: {self.name}\nAge: {self.age}\nBlood Group: {self.bloodgroup}"
            newPatient = Patient(None,studentInfo,None)
            WRM.tail.next = newPatient
            newPatient.prev = WRM.tail
            WRM.tail = WRM.tail.next
            WRM.tail.next = WRM.head
            WRM.head.prev = WRM.tail

    def registerPatient(self,id, name, age, bloodgroup):
        wrm = WRM(id, name, age, bloodgroup)

    def servePatient(self):
        if WRM.tail.info==None:
            print("\033[91mNo patient in the waiting room!!")
            return
        elif WRM.dummy.next.next==None:
            current = WRM.dummy.next
            WRM.dummy.next = None
            WRM.dummy.prev = None
            current.next = None
            current.prev = None
            print("\033[93mPatient has been served successfully!!")
            asked = input("     See patient's info? Y/N  ")
            if asked=="Y" or asked=="y":
                print(current.info)
                current.info = None
            elif asked=="N" or asked=="n":
                current.info = None
            else:
                print("\033[92mInvalid user input")
                current.info = None
            return
        current = WRM.head.next
        WRM.dummy.next = WRM.dummy.next.next
        WRM.dummy.next.prev = WRM.dummy
        current.prev = None
        current.next = None
        print("\033[92mPatient has been served successfully!!")
        asked = input("     See patient's info? Y/N  ")
        if asked=="Y" or asked=="y":
            print(current.info)
            current.info = None
        elif asked=="N" or asked=="n":
            current.info = None
        else:
            print("\033[92mInvalid user input")
            current.info = None

    def showAllPatient(self):
        if WRM.tail.info==None:
            print("\033[91mNo patient in the waiting room!!")
            return
        temp = WRM.head.next
        count = 1
        while temp!=WRM.head:
            print(f"Patient {count} information: ")
            print(temp.info)
            temp = temp.next
            count+=1
            print()
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print()

    def canDoctorGoHome(self):
        if WRM.tail.info==None:
            print("\033[92mYes!! Doctor can go home now")
        else:
            count = 0
            current = WRM.head.next
            while current!=WRM.head:
                count+=1
                current = current.next
            print("\033[91mNo!! Doctor can not go home now")
            print(f"Total waiting patient: {count}")

    def cancelAll(self):
        if WRM.tail.info==None:
            print("\033[91mYou need to register first to cancel the patient")
            return
        current = WRM.head.next
        while current!=WRM.tail:
            WRM.head.prev = None
            WRM.head.next = None
            WRM.head.info = None
            WRM.head = current
            current = current.next
        WRM.tail.prev = None
        WRM.tail.next = None
        WRM.tail.info = None
        print("\033[92mAll the appointment has been canceled")

    def ReverseTheLine(self):
        if WRM.tail.info==None:
            print("\033[91mCan not reverse the line. Must register the patient first")
            return
        start = WRM.head.next
        end = WRM.tail
        while start!=end and end.next!=start:
            start.info,end.info = end.info,start.info
            start = start.next
            end = end.prev
        print("\033[92mThe line has successfully reversed!!")

wrm = WRM()
while True:
    print()
    print("         \033[93mTo register a patient press >>> 1")
    print("         To serve a patient press >>> 2")
    print("         To cancel all the appoinments preee >>> 3")
    print("         Check if the doctor can go home or not press >>> 4")
    print("         To see all the patient's info press >>> 5")
    print("         To reverse the line press >>> 6")
    print()
    userInput = int(input())
    if userInput==1:
        studentId = input("\033[96mEnter Student ID: ")
        studentName = input("Enter Student Name: ")
        studentAge = input("Enter Student Age: ")
        studentBloodGroup = input("Enter Student Blood Group: ")
        wrm.registerPatient(studentId, studentName, studentAge, studentBloodGroup)
    elif userInput==2:
        wrm.servePatient()
    elif userInput==3:
        wrm.cancelAll()
    elif userInput==4:
        wrm.canDoctorGoHome()
    elif userInput==5:
        wrm.showAllPatient()
    elif userInput==6:
        wrm.ReverseTheLine()


