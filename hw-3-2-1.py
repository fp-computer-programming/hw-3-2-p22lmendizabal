# author: LM 10/06/21
average_grade = float(input("Enter in the numerical average you had this quarter. "))

if average_grade < 60:
    print("You got an F")
else:
    if average_grade < 65:
        print("You have a D")
    else:
        if average_grade < 70:
            print("You have a D+")
        else:
            if average_grade < 73:
                print("You have a C-")
            else:
                if average_grade < 77:
                    print("You have a C")
                else:
                    if average_grade < 80:
                        print("You have a C+")
                    else:
                        if average_grade < 83:
                            print("you have a B-")
                        else:
                            if average_grade < 87:
                                print("You have a B")
                            else:
                                if average_grade < 90:
                                    print("You have a B+")
                                else:
                                    if average_grade < 93:
                                        print("You have a A-")
                                    else:
                                        if average_grade < 100:
                                            print("You have a A!!!!!")