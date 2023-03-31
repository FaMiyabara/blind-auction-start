from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

next = True
bidders={}

while next:
  name = input("What's your name? ")
  bid = int(input("Value of your bid: $"))
  bidders[name]=bid
  more_bids = input ("It's anyone else to bid? Y/N \n").lower()
  clear()
  if more_bids == "n":
    next = False

greatest  = (max(bidders, key=bidders.get)) 
print (f"The winner was {greatest} with a bid of  ${bidders[greatest]}")

    