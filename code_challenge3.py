#Global Freight Calculator

SenderName= input('Enter Sender Name: ')
Type= input('Enter Type of Item: ')
is_Fragile= input('Is It Fragile? True or False: ')
weight= float(input('Enter Item Weight in kg: '))
distance= float(input('Enter Distance in km: '))
is_Express= input('Is it Rush? True or False: ')
is_International= input('Is it International Delivery? True or False: ')

base_cost= (weight * 2.50) + (distance * 0.15)

if weight <= 2.0 and distance <=100.0 and is_Express == 'False' and is_International == 'False':
	print('Free Shipping')
elif is_International == 'True' and is_Express == 'True':
	print('Total=', (base_cost * 1.40) + 50)
elif is_Express == 'True' or is_International == 'True' and weight > 20:
	print('Total=', (base_cost * 1.20) + 25)
elif weight > 30 or distance > 1000:
	print('Total=', base_cost + 30)
else:
	print('Total=', base_cost)