print ("Enter 2 number to perform calculation: ");
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
calc = input("Enter the operator: ")
if calc=="+":
  print("The sum of",num1,"&",num2,"is:",num1+num2 )
elif calc=="-":
  print("The subtraction of",num1,"&",num2,"is:",num1-num2)
elif calc=="*":
  print("The multiplication of",num1,"&",num2,"is:",num1*num2)
elif calc=="/":
  print("The division of",num1,"&",num2,"is:",num1/num2)
elif calc=="**":
  print("The exponention of",num1,"&",num2,"is:",num1**num2)
elif calc=="%":
  print("The modulus of",num1,"&",num2,"is:",num1%num2)
elif calc=="//":
  print("The floor division of",num1,"&",num2,"is:",num1//num2)
else:
  print("Invalid")
