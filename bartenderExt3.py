import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

adjectives = ["Bored","Hardworking","Mysterious","Verbose","Laconic","Curious","Silly","Contrary","Shocking","Wild","Rambunctious","Courageous","Cowardly","Infamous"]

nouns = ["rainbows","laser beams","senor","bunny","captain fantastic","nibblets","bipolar cupcake","carrot people","sock gnomes"
]

clients = {}

stock = {"shake of bitters", "splash of tonic", "twist of lemon peel","glug of rum", "slug of whisky", "splash of gin","olive on a stick", "salt-dusted rim", "rasher of bacon","sugar cube", "spoonful of honey", "spash of cola","slice of orange", "dash of cassis", "cherry on top"}


def askStyle (questions):
  """Asks what style of drink"""
  style = {}
  for type, key in questions.iteritems():
    print key
    style[type] = raw_input().lower() in ["y", "yes"]
  return style


def constructDrink (style, ingredients, stock):
  """Constructs the drink"""
  drink = []
  for key in style:
    if style[key] == True:
      ingredient = random.choice(ingredients[key])
      drink.append (ingredient)
      stock[ingredient] -=1
      if stock[ingredient] < -7:
        stockManagement (stock)
  return drink


def giveName (adjectives, nouns):
  """Gives cocktail an original name"""
  cocktailname = random.choice(adjectives) + " " + random.choice(nouns)
  return cocktailname


def stockManagement (stock):
  """Checks whether bartender wants to restock"""
  restock = raw_input("Do you want to restock?").lower() in ("y","yes")
  if restock == True:
    stock.clear()
  else:
    print "You shouldn't wait too long, dude..."
    

def main (clients):
  """Main function, calls all other functions, manages clients"""
  #Gets client name
  clientname = raw_input ("What's your name please?")
  while clientname.lower() != "stop":
    if clientname in clients:
      print "Let's make you a nice " + clients[clientname]
      clientname = raw_input ("What's your name please?")
    else :
      #Gets style
      style = askStyle(questions)
      #Gets drink
      print constructDrink(style, ingredients, stock)
      #Gets name
      cocktailname = giveName(adjectives, nouns)
      print "This is the: " + cocktailname
      clients [clientname] = cocktailname
      clientname = raw_input ("What's your name please?")

      
if __name__ == "__main__":
    main(clients)
    
    
