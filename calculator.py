print("Enter first number")
num1 = input()
print("Enter second number")
num2 = input()
print("Enter operator")
operators = input()

if operators == "+":
    print(int(num1) + int(num2))
elif operators == "-":
    print(int(num1) - int(num2))
elif operators == "*":
    print(int(num1) * int(num2))
elif operators == "/":
    print(int(num1) / int(num2))
else:
    print("please enter proper operator")
