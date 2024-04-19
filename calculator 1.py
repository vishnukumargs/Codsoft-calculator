print("Calculator")
num1=int(input("Enter value A:"))
num2=int(input("Enter value B:"))
operator=input("Enter the operator(+ - * /):")
if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    print("Operator is invalid")
