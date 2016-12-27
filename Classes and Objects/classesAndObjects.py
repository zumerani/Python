lotteryPlayerDict = {
    'name': 'Ralph',
    'numbers': (5 , 9 , 12 , 3 , 1 , 21)
}

# Instead of using a dictionary, we can use a class to make the dictionary
# more generic.
class LotteryPlayer:

    def __init__(self , name , numbers): #'self' refers to the object being instantiated
        self.name = name
        self.numbers = numbers

    def total(self):
        return sum(self.numbers)



player = LotteryPlayer("Zain" , (1 , 2 , 3)) #instantiate a class. 'player' now has the properties defined in the __init__ method above^.
print(player.name)
print(player.numbers)
print("Total is: {}".format(player.total()))
player.numbers = (4 , 5 , 6) #Note: Tuples are immutable, so we can't change the contents, but you can change the entire tuple
print(player.numbers)
print("Now the total is: {}".format( player.total() ) )


#Another example
class Student:
    def __init__(self , name , school):
        self.name = name
        self.school = school
        self.marks = []

    def calculateAverage(self):
        return sum(self.marks) / len(self.marks)

    #Static methods have no implicit parameters
    @staticmethod
    def goToSchool():
        print("I am going to school")

    #Class Methods will have the 'cls' parameter passed in implicitly
    @classmethod
    def goingToSchool(cls):
        print("I am a {}".format(cls))

zain = Student("Zain" , "MIT")
zain.marks.append(50)
zain.marks.append(100)
print(zain.goingToSchool())
print( Student.goToSchool() )