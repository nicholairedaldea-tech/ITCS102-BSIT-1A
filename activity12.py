import getpass

password= getpass.getpass('Create Password: ')
Password= password

Password= getpass.getpass('Type Password: ')
if Password == password:
	print('Password Matched')
else:
	print('Password Does Not Match')