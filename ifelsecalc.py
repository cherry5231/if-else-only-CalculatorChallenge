print("WELCOME TO BASIC CALCULATOR")

print("operators are + - * / % ")
print("Maximum 5 values accepted\n")
print("Make sure to use brackets depending on priority, ex-BODMAS")
print("minimum two values have to be entered\n")
print("While entering what type of calculation you want add the values below \n")
print("After that every value is considered a,b,.....\n Make sure to type how you want to calculate them like (a+b) using brackets after you enter the calculation you want\n")

NO_OF_VALUES = input("Enter number of values: ")

if NO_OF_VALUES == "2":

 a = float(input(""))
 b = float(input(""))

 print("Enter what type of calculation you want:\n")
 calculation = input("")
 if calculation ==  "+":
   addition = a+b
   print(addition)
 elif calculation ==  "-":
   subtraction = a-b
   print(subtraction)
 elif calculation == "%":
   percentage = a%b
   print(calculation)
 elif calculation == "*":
    multiplication = a*b
    print(multiplication)
 elif calculation == "/":
   division = a/b
   print(division)   
elif NO_OF_VALUES == "3":
 a = float(input(""))
 b = float(input(""))
 c = float(input(""))
 print("Enter what type of calculation you want:")
 calculation = input("")
 bracket = input("")
 if calculation ==  "+":

   addition = a+b+c
   print(addition)

 elif calculation ==  "-":
   if bracket == "(b-c)":
    subtraction = a-(b-c)
    print(subtraction)
   elif bracket == "(a-b)":
    subtraction = (a-b)-c
   print(subtraction)

 elif calculation == "%":
  if bracket == "(a%b)":
    percentage = (a%b)%c
    print(percentage)
  elif bracket == "(b%c)":
    percentage =  a%(b%c)
    print(percentage)
   
   
 elif calculation == "*":
   if bracket == "(a*b)":
    multiplication =(a*b)*c
    print(multiplication)
   elif bracket == "(b*c)":
    multiplication = a*(b*c)
    print(multiplication)

 elif calculation == "/":
  if bracket == "(a/b)":
    division = (a/b)/c
    print(division)
  elif bracket == "(b/c)":
    division = a/(b/c)
    print(division)
elif NO_OF_VALUES == "4":
 a = float(input(""))
 b = float(input(""))
 c = float(input(""))
 d = float(input(""))
 print("Enter what type of calculation you want:")
 calculation = input("")
 bracket = input("")
 if calculation ==  "+":

   addition = a+b+c+d
   print(addition)

 elif calculation ==  "-":
   if bracket == "(b-c)":
    subtraction = a-(b-c)-d
    print(subtraction)
   elif bracket == "(a-b)":
    subtraction = (a-b)-c-d
    print(subtraction)
   elif bracket == "(c-d)":
    subtraction =  a-b-(c-d)
    print(subtraction)
   elif bracket == "(a-b)-(c-d)":
    subtraction = (a-b)-(c-d)
    print(subtraction)
 elif calculation == "%":
  if bracket == "(a%b)":
    percentage = (a%b)%c%d
    print(percentage)
  elif bracket == "(b%c)":
    percentage =  a%(b%c)%d
    print(percentage)
  elif bracket == "(c%d)":
    percentage = a%b%(c%d)
    print(percentage)
  elif bracket == "(a%b)%(c%d)":
    percentage = (a%b)%(c%d)
    print(percentage)
   
   
 elif calculation == "*":
   if bracket == "(a*b)":
    multiplication =(a*b)*c*d
    print(multiplication)
   elif bracket == "(b*c)":
    multiplication = a*(b*c)*d
    print(multiplication)
   elif bracket == "(a*b)*(c*d)":
    multiplication = (a*b)*(c*d)
    print(multiplication)

 elif calculation == "/":
  if bracket == "(a/b)":
    division = (a/b)/c/d  
    print(division)
  elif bracket == "(b/c)":
    division = a/(b/c)/d
    print(division)
  elif bracket == "(a/b)/(c/d)":
    division = (a/b)/(c/d)
    print(division)

elif NO_OF_VALUES == "5":
 a = float(input(""))
 b = float(input(""))
 c = float(input(""))
 d = float(input(""))
 e = float(input(""))
 print("Enter what type of calculation you want:")
 calculation = input("")
 bracket = input("")
 if calculation ==  "+":

   addition = a+b+c+d+e
   print(addition)

 elif calculation ==  "-":
   if bracket == "(b-c)":
    subtraction = a-(b-c)-d-e
    print(subtraction)
   elif bracket == "(a-b)":
    subtraction = (a-b)-c-d-e
    print(subtraction)
   elif bracket == "(c-d)":
    subtraction =  a-b-(c-d)-e
    print(subtraction)
   elif bracket == "(a-b)-(c-d)-e":
    subtraction = (a-b)-(c-d)-e
    print(subtraction)
   elif bracket == "(d-e)":
    subtraction = a-b-c-(d-e)
    print(subtraction)
   elif bracket == "(a-b)-c-(d-e)":
    subtraction = (a-b)-c-(d-e)
    print(subtraction)
 
 elif calculation == "%":
  if bracket == "(a%b)":
    percentage = (a%b)%c%d%e
    print(percentage)
  elif bracket == "(b%c)":
    percentage =  a%(b%c)%d%e
    print(percentage)
  elif bracket == "(c%d)":
    percentage = a%b%(c%d)%e
    print(percentage)
  elif bracket == "(a%b)%(c%d)%e":
    percentage = (a%b)%(c%d)
    print(percentage)
  elif bracket == "(a%b)%c%(d%e)":
    percentage = (a%b)%c/(d%e)
    print(percentage)
  elif bracket == "a%(b%c)/d%e":
    percentage= a%(b%c)%d%e
    print(percentage)
  elif bracket == "a%b%(c%d)%e":
    percentage = a%b%(c%d)%e
    print(percentage)
   
   
 elif calculation == "*":
   if bracket == "(a*b)":
    multiplication =(a*b)*c*d*e
    print(multiplication)
   elif bracket == "(b*c)":
    multiplication = a*(b*c)*d*e
    print(multiplication)
   elif bracket == "(a*b)*(c*d)*e":
    multiplication = (a*b)*(c*d)
    print(multiplication)
   elif bracket == "(a*b*c*d*e)":
    multiplication = a*b*c*d*e
    print(multiplication)

 elif calculation == "/":
  if bracket == "(a/b)":
    division = (a/b)/c/d/e
    print(division)
  elif bracket == "(b/c)":
    division = a/(b/c)/d/e
    print(division)
  elif bracket == "(a/b)/(c/d)":
    division = (a/b)/(c/d)/e
    print(division)
  elif bracket == "a/b/c/(d/e)":
    division = a/b/c/(d/e)
    print(division)
  elif bracket == "(a/b)/c/(d/e)":
    division = (a/b)/c/(d/e)
    print(division)
  elif bracket == "a/(b/c)/d/e":
    division = a/(b/c)/d/e
    print(division)
  elif bracket == "a/b/(c/d)/e":
    division = a/b/(c/d)/e
    print(division)
  elif bracket == "a/(b/c)/(d/e)":
     division = a/(b/c)/(d/e)
     print(division)





