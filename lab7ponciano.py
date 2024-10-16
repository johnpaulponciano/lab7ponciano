name=input("What is your name? ")
section=(input("What is your section? "))
prelim= float(input("What is your grade in your prelim? "))
midterm= float(input("What is your grade in your midterm? "))
final=float(input("What is your grade in your Final? "))

if prelim <40 and prelim <100:
    print("Your grade in prelim is ", prelim)
elif prelim >100:
    print("Invalid grade in prelim")
    
if midterm <40 and midterm <100:
    print("Your grade in midterm is ", midterm)
elif midterm >100:
    print("Invalid grade in midterm")
    
if final <40 and final <100:
    print("Your grade in final is ", final)
elif final >100:
    print("Invalid grade in final")
    
finalgrade= prelim * 0.3333 +  midterm * 0.3333 + final * 0.3333
finalgrade=  round(finalgrade)
if  finalgrade >=40 and finalgrade<=100:
    print("Your Grade  is ", finalgrade)


if finalgrade >= 99 and finalgrade <=100:
        print("Your Grade points is 1.00, Excellent.",  name, "your grade is", finalgrade)
elif finalgrade >= 96 and finalgrade <=98:
        print("Your Grade points is 1.25, Outstanding.",  name, "your grade is", finalgrade)
elif finalgrade >= 93 and finalgrade <=95:
        print("Your Grade points is 1.50, Superior.",  name, "your grade is", finalgrade)
elif finalgrade >= 90 and finalgrade <=92:
        print("Your Grade points is 1.75, Very Good.",  name, "your grade is", finalgrade)
elif finalgrade >= 87 and finalgrade <=89:
        print("Your Grade points is 2.00, Good.",  name, "your grade is", finalgrade)
elif finalgrade >= 84 and finalgrade <=86:
        print("Your Grade points is 2.25, Satisfactory.",  name, "your grade is", finalgrade)
elif finalgrade >= 81 and finalgrade <=83:
        print("Your Grade points is 2.50, Fairly Satisfactory.",  name, "your grade is", finalgrade)
elif finalgrade >=78 and finalgrade <=80:
        print("Your Grade points is 2.75, Fair.",  name, "your grade is", finalgrade)
elif finalgrade >= 75 and finalgrade <=77:
        print("Your Grade points is 3.00, Passed.",  name, "your grade is", finalgrade)
elif finalgrade <=75:
        print("Your Grade points is 5.00, Failed.",  name, "your grade is", finalgrade )
else:
    print("Invalid grade")