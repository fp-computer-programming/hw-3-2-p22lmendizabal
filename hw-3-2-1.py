# author: LM 10/06/21
average_grade = int(input("Enter in the numerical average you had this quarter. "))

if average_grade >= 93:
    print("You have an A")
else:
    if average_grade < 93:
        print("You have an A-")
    else: 
        print("You have an A.")
if average_grade <= 89:
    print("You have a B+")
else:
    if average_grade <= 86.999999999:
        print("You have a B.")