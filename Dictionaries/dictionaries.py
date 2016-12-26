#Dictionaries -- key/value pairings
#Dictionaries are key/value sets

myDict = {'name' : 'Zain' , 'age': 20 , 'grades' : [13 , 14 , 99 , 100] }#We can store any data we want

lotteryPlayer = {
    'name': 'Ben' ,
    'numbers' : (13, 45 , 66 , 23 , 22) #tuple
}

universities = [ #List of dictionaries ... there are no restrictions here, you can put anything

    {
        'name': 'Oxford'
    },
    {
        'name': 'Stanford' ,
        'location': 'Bay Area'
    }

]

print("Sum of Ben's numbers are: {}".format( sum(lotteryPlayer['numbers']) ) ) #Note with sets, you cannot access but with dictoinaries you can access

