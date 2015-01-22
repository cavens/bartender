import pdb
import random
from data import *

def askName() return raw_input("What's your name? "):

def nameExists(clientname):
  """What do I do?....."""
  returning = clientname in clientdrink
  return returning


def stockManagement(clientname,ingredient,statusnew):
  """What do I do?....."""
  global stock
  if statusnew:
    stock [ingredient] -= 1
    if stock [ingredient] < 3:
      reStock()
  else:
    ingredients = clientingredients[clientname]
    for ingredient in ingredients:
      stock [ingredient] -=1
      if stock [ingredient] <3:
        reStock()

  
def reStock():
  """Checks whether bartender wants to restock"""
  restock = raw_input("Do you want to restock?").lower() in ("y","yes")
  global stock
  if restock:
    for key in stock:
      stock[key]=5
    print "Reserves back at 100%"
  else:
    print "You shouldn't wait too long, dude..."
    
  
def constructDrink(clientname,style):
  """Constructs the drink"""
  drink = []
  for key in style:
    if style[key]:
      ingredient = random.choice(ingredients[key])
      drink.append (ingredient)
      stockManagement(clientname, ingredient, True)
  return drink


def drinkName():
  """Looks up existing name OR creates new name. Returns name of drink"""
  drinkname = random.choice(adjectives) + " " + random.choice(nouns)
  return drinkname


def newClient(clientname):
  """Asks for style, adds ingredients, gives drink name, adds data in DB"""
  style = askStyle()
  drink = constructDrink(clientname,style)
  drinkname = drinkName()
  clientdrink [clientname] = drinkname
  clientingredients [clientname] = drink
  return drinkname

  
def askStyle():
  """Asks what style of drink"""
  style = {}
  for type, key in questions.iteritems():
    print key
    style[type] = raw_input().lower() in ["y", "yes"]
  return style
    

def main():
  """What do I do?....."""
  while True:
    clientname = askName()
    if clientname.lower() in "stop": break
    returning = nameExists(clientname)
    if returning:
      stockManagement(clientname,"",False)
      drinkname = clientdrink[clientname]
    else:
      drinkname = newClient(clientname)
    print stock
    print "Here's a nice" + " " + drinkname
  
  
if __name__ == "__main__":
    main()
  
  