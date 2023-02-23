#!/usr/bin/env python3
import ipdb
def admin_login(username, password):
    # value_if_true if condition else value_if_false
    return 'Access granted' if (username.lower() == 'admin' and password == '12345') else "Access denied"
    # same as below:
    # if username.upper() == "ADMIN" and password == "12345":
    # return "Access granted"
    
    # return "Access denied"

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return  "It's brisk out there!"
    # elif temperature > 40 and temperature < 65: THIS WORKS BUT NEEDS TO INCLUDE 40 AND 65 TOO
    elif 40 <= temperature <= 65: 
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    # else:
    #     return  "It's perfect out there!" BUT MORE SIMPLE WAY BELOW:
    return  "It's perfect out there!"

def fizzbuzz(num):
    # your code here
    # ipdb.set_trace() 
    if num % 5 == 0 and num % 3 == 0:
    # if not num % 15: THIS IS SHORTER VERSION
        return 'FizzBuzz'
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return 'Buzz'
    return num
# fizzbuzz(45)

def calculator(operation, num1, num2):
    # your code here
    if operation == '+' :
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    # else:
    #     print('Invalid operation!')
    #     return None
    # short version below
    print("Invalid operation!")
    return None
