# author:LM (AMDG) 10/07/21
#BMI = kilograms / meters ** 2

height = float(input("Enter your height in meters. "))
weight = float(input("Enter your weight in kilgormas. "))

total_bmi = weight / height ** 2

if total_bmi < 19:
    print("You are underweight.")
else:
    if total_bmi < 25:
        print(" You are healthy")
    else:
        if total_bmi < 30:
            print("You are overweight.")
        else:
            if total_bmi < 40:
                print("You are obese")
            else:
                if total_bmi > 40:
                    print("You are very obese.")

