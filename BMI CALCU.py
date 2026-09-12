print('BMI Calculator')

Weight= float(input('Enter Your Weight in Kg: '))
Height= float(input('Enter Your Height in m: '))

Height2= Height ** 2

BMI= Weight / Height2
print(f'BMI:, {BMI:.3f}')

if BMI <= 18.5:
    print('Underweight')
elif BMI > 18.5 >= 24.9
    print('Normal')
elif BMI >= 25 >= 29.9:
    print('Overweight')
else:
    print('Obese')