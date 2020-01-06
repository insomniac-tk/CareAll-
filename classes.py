'''
	Author - Tejas Khanna
	This module handles defines all the classes for the
	CareAll System
'''

# Superclass for defining a generic User(can be a caretaker or oldie) of the system 

class User:

	def __init__(self,user_id,name,password,email,contact,emergency_contact):

		self.user_id = user_id
		self.name = name
		self.password = password
		self.email = email
		self.contact = contact
		self.emergency_contact = emergency_contact
		self.rating = {} 
		# storage format - rating['User_object'] = 2 means , User_object gave this user(self) a rating
		# of 2.
	
	# Helpful method to fetch details of a user at any point!
	def GetDetails(self):
		if not self.rating == None or self.rating == {}:
			print("Name - {} | Rating - {}/5".format(self.name,self.rating))
		else:
			print("Name - {}".format(self.name))

class Caretaker(User):

	# Blueprint for Student object 

	def __init__(self,user_id,name,password,email,contact,emergency_contact,monthly_charge):
		super().__init__(user_id,name,password,email,contact,emergency_contact) # inherited attributes
		# attrs unique to Caretaker object
		self.category = 'caretaker'
		self.monthly_charge = monthly_charge
		self.TakingCareOf = [] # List of oldies Caretaker is taking care of, a list of oldie objects

class Oldie(User):

	# Blueprint for an Oldie object 

	def __init__(self,user_id,name,password,email,contact,emergency_contact):
		super().__init__(user_id,name,password,email,contact,emergency_contact) # inherited attributes
		self.category = 'oldie'
		self.MyCaretaker = None
		self.Requests = [] # Holding the caretaker objects that want to help

	def ShowCareTaker(self):
		print("Details of caretaker for {} are :".format(self.name))
		for k,v in vars(self.MyCaretaker):
			print("{} : {}".format(k,v))


class Wallet:
	# Every user owns a wallet 

	def __init__(self,user_obj,init_balance):
		self.user_id = user_obj.user_id
		self.init_balance = init_balance
		self.curr_balance = self.init_balance
		print("New Wallet created for {},\nOpening balance = Rs. {}".format(user_obj.name,init_balance))

	# methods to add / deduct money from wallet
	def deposit(self,amount):
		self.curr_balance += amount 

	def withdraw(self,amount):
		'''
			A boolean function which returns False if amount to withdraw exceeds current balance
			Otherwise ,updates curr_balance to reflect changes and returns the current balance
		'''
		if amount > self.curr_balance:
			print("You cannot withdraw Rs.{} as you do not have sufficient funds in your account.".format(amount))
			print("Your Balance: Rs. {}".format(self.curr_balance))
			return False

		else:
			self.curr_balance -= amount # curr_bal - amt
			return self.curr_balance

class Review():
	# instances of this class will hold information about 3 things - a review(string),who posted it(poster_id)
	# and who it is for 
	# Say we already have a Caretaker and Oldie object and the former writes a review about the latter.
	# Example - newReview = Review(text,caretaker,oldie) # id will be extracted from the caretaker and 
	# oldie objects themeselves. 

	# Reviewer - Person posting the review, Revieweee - Whom the review is about

	def __init__(self,text,reviewer,reviewee):
		self.review = text
		self.reviewer = reviewer
		self.reviewee = reviewee


