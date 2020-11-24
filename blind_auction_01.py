from art import logo
import os

print(logo)
name_and_bid = {}

''' Clear terminal '''
def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

''' Get bidder name and bid '''
def auction():
  username = input('Name: ').capitalize()
  user_bid = int(input('Bid: '))
  name_and_bid.update({username: user_bid})
  other_bidders = input('Are there other users who want to bid: Y/N ').lower()
  clear()

  max_bid = max(name_and_bid, key=name_and_bid.get)
  if other_bidders == 'n':
    # print(name_and_bid)
    print(f'{max_bid} has the highest bid of ${name_and_bid[max_bid]}')
    return name_and_bid
  elif other_bidders == 'y':
    auction() # recursive function

auction()