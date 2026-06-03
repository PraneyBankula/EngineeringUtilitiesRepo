subjectAmount = int(input("How many subjects do you take?: "))
i = 0
subjects = []
while (i < subjectAmount):
    enterSubject = input("Enter your subject: ")
    subjects.append(enterSubject)
    i+=1

total = 0

for subject in subjects:
    grade = int(input("Enter your grade for {subject}: (grade 0-100)"))
    total += grade    
   
averageSum = total / subjectAmount
if (averageSum >= 93):
    print("Congrats you have a 4.0!")
elif (averageSum < 93 and averageSum >= 90):
    print("You have a 3.7, solid!")
elif (averageSum < 90 and averageSum >= 87):
    print("You have a 3.3, not bad!")
elif(averageSum < 87 and averageSum >= 83):
    print("You have a 3.0, decent")
elif (averageSum < 83 and averageSum >= 80):
    print("Your gpa is a 2.7, try to boost it up")
elif(averageSum < 80 and averageSum >= 77):
    print("You have a 2.3, terrible")
elif(averageSum < 77 and averageSum >=73):
    print("You have a 2.0, just disappointing")
elif(averageSum < 73 and averageSum >= 70):
    print("You have a 1.7 GPA, do you even try")
elif(averageSum < 70 and  averageSum >= 67):
    print("You have a 1.3 GPA, just how")
elif(averageSum < 67 and averageSum >= 65):
    print("You have a 1.0 GPA, impressive")
elif(averageSum < 65 ):
    print("You have a 0.0 GPA")