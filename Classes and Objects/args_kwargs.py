#If you want to pass multiple arguments into a function, use *args:


#Args (It's a tuple -- immutable)
def simplifiedAddition(*args):
    return sum(args)

#Now we can call the above function like so (without passing in a list):
print( simplifiedAddition(5 , 5 , 5) ) #prints 15. Note we don't need to pass in a list, just the arguments.


#Kwargs (Kwargs would be a set) -- stands for keyword arguments

def kwargsExample(name , location):
    print("name is: {}".format(name))
    print("location is: {}".format(location))

kwargsExample(name="zain" , location="houston")
#Even switching the order is fine:
kwargsExample(location="houston" , name="zain")


#Now, looking back at our inheritance classes from inheritance.py, we can simplify some of the code, using args:
#Changes made: In Student, we pass in *args which would just be whatever is passed after friendName (in this case, salary)

#The cool thing is, we can add whatever we want to args (we can add title like it is below) without changing the Student's
#constructor. All we need to do is change the constructor of WorkingStudent, and that's it.

class Student:
    def __init__(self , name , school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls , origin , friendName , *args):
        #return a new Student called 'friendName' in the same school as self
        return cls(friendName , origin.school , *args) #This now calls WorkingStudent's constructor



#This is bascially 'WorkingStudent' extends 'Student', all of Student's methods are now in WorkingStudent
class WorkingStudent(Student):
    def __init__(self , name , school , salary , title):
        #rather than copying the contents of the constructor, use 'super()'
        super().__init__(name , school) #executes the supper class constructor (Student's constructor)
        self.salary = salary #now set your 'WorkingStudent' characteristics
        self.title = "Software Developer"

Zain = WorkingStudent("Zain" , "MIT" , 15.00 , "Software Developer")
print(Zain.name)
print(Zain.salary)
print(Zain.title)

#We can also using kwargs, just say salary=15.00 and title="Software Developer" and replace *args with **kwargs