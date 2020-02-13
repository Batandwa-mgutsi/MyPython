
# Calculates the number of seconds spent at lectures ina semester, assuming
# there are 5 lectures a day, lectures on 4 days a week, and there are 12 weeks in a semester.
# Batandwa Mgutsi
# 12/02/2020

def formatNumber(number):
    "Adds a space after every third digit in the number"
    stringNumber = f"{number}"
    output = ''
    for i in range(len(stringNumber)):
        if(i%3 == 0):
            output += ' '
        output += stringNumber[i]
    return output

minutesPerLecture = 45
lecturesPerDay = 5
nrOfLectureDaysInOneWeek = 4
weeksInOneSemester = 12

secondsSpentOnLectures = (minutesPerLecture*60)*lecturesPerDay*nrOfLectureDaysInOneWeek*weeksInOneSemester

print(f"Well! You spend about {formatNumber(secondsSpentOnLectures)} seconds a semester just attending"
        " lectures. I mean, Is it really worth it?")
