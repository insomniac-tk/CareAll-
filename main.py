'''
    Application Name  - CareAll
	Author - Tejas Khanna
	This module is the main entry point for the careall application 
'''

import pickle # pickling users dictionary to save it on disk
from classes import *
from os import system,name

FILE_NAME = 'DummyUsers'
sys_users = {'Caretakers':[],'Oldies':[]}





def CreateNewUser(category):
	'''
		This function adds a new Caretaker or Oldie object to sys_users depending on paramter category
	'''
	global id
	name = input("Enter your Full Name: ")
	password= input("Choose a safe password: ")
	email = input("Enter email: ")
	contact = input("Enter your contact number: ")
	em_contact = input("Enter an emergency contact number: ")
	
	if not category == None:

		if category == 'Caretaker':
			monthly_charge = int(input("Please mention your monthly charge - Rs. "))
			obj = Caretaker(id,name,password,email,contact,em_contact,monthly_charge)
			sys_users['Caretakers'].append(obj)
		else:
			obj = Oldie(id,name,password,email,contact,em_contact)
			sys_users['Oldies'].append(obj)

	# increment global id by 1 
	id += 1

def SignUp():
	'''
			This function handles creation of new users
	'''
	print("#############################")
	print("1. A student who wants to earn money as a caretaker\n2. An elder who is looking for youngsters to help him.")
	choice = 0
	while True:
		choice = int(input("You are(Enter 1 or 2) - "))

		if choice not in (1,2):
			print("Oops. That's not valid. Try again.")
			continue
		
		break

	# now calling CreateNewUser based on Category
	category = 'Caretaker' if choice==1 else 'Oldie'
	CreateNewUser(category)


def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
  

def RateUser(the_user_that_is_rating,the_one_being_rated):
	'''
			This function takes as a user object as a  paramater
			It updates the rating attribute of the user_object
			Returns the rating 
	'''
	rating = -1
	while True:

		rating = int(input("Your Rating out of 5: "))

		if not input>=0 and input<=5:
			print("Invalid rating, it should be between 0 and 5. Try again please!")
			continue
		else:
			the_one_being_rated.rating['the_user_that_is_rating'] =  rating
			break


BANNER =  '''#############################
\t#### CareAll ####
#############################
# Are you living alone and need a caretaker to assist you 
# with your daily needs?
# Are you a student who wants to make some money and has 
# a zeal for hospitality and caretaking? 
# Well we've got good news for both of you! 
# Welcome to CareAll where you can earn money by taking care of the elderly!
# SignUp or Login now!
#############################
'''

SIGNUP_LOGIN_BAR  = """1.SignUp
2.Login
"""

def DummyUsers():
	SignUp()
	#pickle
	f = open('DummyUsers','ab')
	pickle.dump(sys_users,f)
	f.close()


def LogIn():
	clear()
	flag = False
	f = open(FILE_NAME,'rb')
	db = pickle.load(f) # The dict sys_users is returned here
	f.close()
	'''
		This function checks the email and password of the User(caretaker or oldie)
		against the data retreived from the pickled sys_users object in the file called
		FILE_NAME defined at the beginning of this module.
		If the email/password combo matches, it takes the user to their home screen.
	'''
	while not flag == True:
		print("########## LOG IN #############")
		email = input("Enter your email: ")
		pwd = input("Enter password: ")
		category = int(input("Caretaker(1) or Elder(2) ? - "))
		c = "Caretaker" if category == 1 else "Oldie"
		
		if c == "Caretaker":
			caretakers = db['Caretakers']
			for ct in caretakers:
				if ct.email == email and ct.password==pwd:
					flag = True 

		else:
			oldies = db['Oldies']
			for ol in oldies:
				if ol.email == email and ol.password==pwd:
					flag =  True

		if flag == False:
			print("Email or Password incorrect , please try again.")
	
	# Redirect to UserHome upon success
	UserHome(email,pwd,category)

	

def UserHome(email,password,category):
	clear()
	f = open(FILE_NAME,'rb')
	db = pickle.load(f) # The dict sys_users is returned here
	f.close()
	c = 'Caretakers' if category == 1 else 'Oldies'
	curr_user = None
	for u in db[c]:
		if u.email == email and u.password == password:
			curr_user = u
			break

	print("##############")
	print("Welcome {}".format(curr_user.name))

	if c=='Caretakers':
		print("The followed elders want help: ")
		for elder in db['Oldies']:
			print("Id - {}".format(elder.user_id))
			print("Name - {}".format(elder.name))
			print('________________________________________')

		n = int(input("Write the id of the elder  that you want to help - "))
		chosen_elder = None
		for elder in db['Oldies']:
			if n == elder.user_id:
				chosen_elder = elder
				break



def main():
	print(BANNER)
	print(SIGNUP_LOGIN_BAR)
	choice = 0
	while True:
		choice = int(input("Enter 1 for SignUp , 2 for Login - "))

		if choice not in (1,2):
			print("Enter 1 or 2. Try again.")
			continue
		break

	# SignUp
	if choice == 1:
		SignUp()
	else:
		LogIn()


if __name__=='__main__':
	main()