print('SIMPLE CALCULATOR')  
print('+- Addition')
print('-- Subtration')
print('*- Multiplication')
print('/- Division')

num1= float(input('Enter First Number: '))
operation= input('Choose Operation: ')
num2= float(input('Enter Second Number: '))

if operation == '+':
    print(num1 + num2)

elif operation == '-':
    print(num1 - num2)

elif operation == '*':
    print(num1 * num2)

elif operation == '/':
    if num2 == 0:
        print('Invalid')
    else:
        print(num1 / num2)
