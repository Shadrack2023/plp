# This is a basic calculator program that perfom basic arithmetic operation.

import time

print("To perform arithmetic operations, you'll need to enter two numbers on the prompts below.")

num1 = float(input("Enter number: "))
num2 = float(input("Enter another number here: "))

print("Operation in process... ")
time.sleep(3)

add_num = num1 + num2
diff_num = num1 - num2
mult_num = num1 * num2

print(f"Addition: {add_num}")
print(f"Subtraction: {diff_num}")
print(f"Multiplication: {mult_num}")

if num2 == 0:
    print(f"Division: Error! Can't divide by zero.")
else:
    div_num = num1 / num2
    print(f"Division: {div_num}")


