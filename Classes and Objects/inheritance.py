class Student:
    def __init__(self , name , school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls , origin , friendName , salary):
        #return a new Student called 'friendName' in the same school as self
        return cls(friendName , origin.school , salary) #This now calls WorkingStudent's constructor



#This is bascially 'WorkingStudent' extends 'Student', all of Student's methods are now in WorkingStudent
class WorkingStudent(Student):
    def __init__(self , name , school , salary):
        #rather than copying the contents of the constructor, use 'super()'
        super().__init__(name , school) #executes the supper class constructor (Student's constructor)
        self.salary = salary #now set your 'WorkingStudent' characteristics


zain = WorkingStudent("Zain" , "UCSD" , 15.00)
print(zain.salary) #prints 15.0

friend = WorkingStudent.friend( zain , "Bob" , 20.00) #NOTE: This calls Student's 'friend' method NOT WorkingStudent, because WorkingStudent
                                              # doesn't have a friend method. But in order to call 'friend' as a WorkingStudent object,
                                              # you need to declare 'friend' in the super class (Student) as a classmethod. This is
                                              # because you are now passing 'cls' which is WorkingStudent and you return:
                                              # cls(friendName) but that calls WorkingStudent's constructor so it will store the salary
                                              # as well.

print(friend.name) #prints Bob
print(friend.school) #prints school
print(friend.salary) #prints salary (20.0)
