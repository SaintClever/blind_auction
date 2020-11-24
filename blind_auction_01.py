from art import logo
import os

print(logo)
name_and_bid = {}

''' clear method '''
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

''' auction method '''
def auction():
	username = input('Name: ')
	user_bid = int(input('Bid: '))
	name_and_bid.update({username: user_bid})

	other_bidders = input('Are there other users who want to bid: Y/N ').lower()
	clear()
	
	if other_bidders == 'n':
		# print(name_and_bid)	
		print(f'{max(name_and_bid, key=name_and_bid.get)} has the highest bid: ${name_and_bid[max(name_and_bid, key=name_and_bid.get)]}')
		return name_and_bid
	elif other_bidders == 'y':
		auction() # recursive function

auction()