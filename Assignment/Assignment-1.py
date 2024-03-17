def GPA_Calculator(avg):
    if avg >= 0 and avg <= 100:
        if avg >= 0 and avg <= 40:
            print("Your Grade F")
        elif avg > 40 and avg <= 60:
            print("Your Grade: D")
        elif avg > 60 and avg <= 70:
            print("Your Grade: C")
        elif avg > 70 and avg <= 80:
            print("Your Grade: B")
        elif avg > 80 and avg <= 90:
            print("Your Grade: A")
        elif avg > 90 and avg <= 100:
            print("Your Grade: A+")
        else:
            print("somthing Wrong")

Bangla = int(input("Enter Your Bangla Subject marks: "))
English = int(input("Enter your English Subject marks: "))
Math = int(input("Enter your Mathematics Subject Marks: "))
Science = int(input("Enter your Science Subject marks: "))

if (Bangla>=0 and Bangla<=100 and English>=0 and English<=100 and Math>=0 and Math<=100 and Science>=0 and Science<=100):
    avg = int((Bangla + English + Math + Science) / 4)
    print("*************************")
    GPA_Calculator(avg)
else:
    print("You have Entered wrong marks")