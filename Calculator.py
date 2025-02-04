first = float(input("First: "))
operation = input("Operation: ")
second = float(input("Second: "))

if operation == "+":
    result = first + second
elif operation == "-":
    result = first - second
elif operation == "*":
    result = first * second
elif operation == "/":
    if second != 0:
        result = first / second
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operation"

print("Result:", result)



