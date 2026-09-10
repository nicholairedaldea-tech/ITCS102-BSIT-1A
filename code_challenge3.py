#Global Freight Calculator

SenderName= input('Enter Sender Name: ')
Type= input('Enter Type of Item: ')
is_Fragile= bool(input('Is It Fragile? True or False: '))
weight= float(input('Enter Item Weight in kg: '))
distance= float(input('Enter Distance in km: '))
is_Express= bool(input('Is it Rush? True or False: '))
is_International= bool(input('Is it International Delivery? True or False: '))

base_cost= (weight * 2.50) + (distance * 0.15)

if weight <= 2.0 and distance <=100.0 and is_Express == False and is_International == False:
	print('Free Shipping')
else:
	print('meron')