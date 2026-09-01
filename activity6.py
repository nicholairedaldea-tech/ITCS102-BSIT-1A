money= int(input("Enter amount of money: "))

print('1000-', money//1000)
money= money%1000
print('500-', money//500)
money=money%500
print('100-', money//100)
money= money%100
print('50-', money//50)
money= money%50
print('20-', money//20)
money= money%20
print('10-', money//10)
money= money%10
print('5-', money//5)
money= money%5
print('1-', money)