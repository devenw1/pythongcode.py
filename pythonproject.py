#Import
import time
#typewriter function 
def typewrite(string):
  liststring= list(string)
  for char in liststring:
    print(char, end="", flush=True)
    time.sleep(0.05)
  return""



typewrite("Welcome to the Gambling Palace\n")
age = input(typewrite("How old are you? "))

if age >= str(18):
  typewrite("Come on in!\n")
  start = input(typewrite("Would you like to Gamble (1), go to the bar (2) or look  around (3)? "))
  if start == "1":
    typewrite("You walk over to a table.\n")

  if start == "2":
    typewrite("You walk over to the bar and look at the menu.\n")
    drink = input(typewrite("What would you like to order? "))
    typewrite("The bartender whips up your " + drink + " and hands it to you.\n")
    afterbar = input(typewrite("Would you like to Gamble (1) or look around (2)? "))
    if afterbar == "1":
      typewrite("you walk over to a table.\n")


    if afterbar == "2":
      typewrite("You take a look around the room and see everyone dressed formally and all the tables lined with people.\n")
      typewrite("You walk over to one of the tables.\n")

  if start == "3":
    typewrite ("You take a look around and see all the tables around you and people dressed in formal wear.\n")
    w_view = input(typewrite("Would you like to gamble (1), or go to the bar (2)? "))
    if w_view == "1":
      typewrite("You walk over to a table.\n")
    if w_view == "2":
      typewrite("You walk over to the bar and look at the menu.\n")
      drink = input(typewrite("What would you like to order? "))
      typewrite("The bartender whips up your " + drink + " and hands it to you.\n")
      typewrite("You walk over to a table.\n")
  typewrite("The first table you walk to is blackjack.")

else:
  typewrite("Get lost!")
