#Program requires the use of dictionaries to store student grades and compute the average

#student dictionary:
student = {
    'name': 'Jose',
    'school' : 'Cupertino',
    'grades' : (66, 77, 78)
}

def averageGrade(data):
    grades = data['grades']
    return sum(grades) / len(grades)

def averageOfAllStudents(studentList): #studentList is a list of dictionaries
    total = 0
    count = 0
    for person in studentList:
        total += sum( person['grades'] )
        count += len( person['grades'] )

    return total/count
