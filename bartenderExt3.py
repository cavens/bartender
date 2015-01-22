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

clientDrinks = {}

stock = "shake of bitters": 5,"lash of tonic": 5, "twist of lemon peel": 5,"glug of rum": 5, "slug of whisky": 5, "splash of gin": 5,"olive on a stick": 5, "salt-dusted rim": 5, "rasher of bacon": 5,"sugar cube": 5, "spoonful of honey": 5, "spash of cola": 5,"slice of orange": 5, "dash of cassis": 5, "cherry on top": 5}

stockInit = {"shake of bitters": 5, "splash of tonic": 5, "twist of lemon peel": 5,"glug of rum": 5, "slug of whisky": 5, "splash of gin": 5,"olive on a stick": 5, "salt-dusted rim": 5, "rasher of bacon": 5,"sugar cube": 5, "spoonful of honey": 5, "spash of cola": 5,"slice of orange": 5, "dash of cassis": 5, "cherry on top": 5}



def askStyle (questions):
  """Asks what style of drink"""
  style = {}
  for type, key in questions.iteritems():
    print key
    style[type] = raw_input().lower() in ["y", "yes"]
  return style


def constructDrink (clientname, style, ingredients, stock):
  """Constructs the drink"""
  if clientname in clients:
    
  drink = []
  for key in style:
    if style[key]:
      ingredient = random.choice(ingredients[key])
      drink.append (ingredient)
      stockManagement(ingredient)
  giveName() = cocktailname
  print "This is the: " + cocktailname
  clients [clientname] = cocktailname
  return drink



def giveName (adjectives, nouns):
  """Gives cocktail an original name"""
  cocktailname = random.choice(adjectives) + " " + random.choice(nouns)
  return cocktailname


def reStock ():
  """Checks whether bartender wants to restock"""
  restock = raw_input("Do you want to restock?").lower() in ("y","yes")
  if restock:
    stock = stockInit
  else:
    print "You shouldn't wait too long, dude..."

    
def stockManagement (ingredient):
  """Keeps track of the stock"""
      stock[ingredient] -=1
      if stock[ingredient] < 3:
        reStock()

    
def main ():
  """Main function, calls all other functions, manages clients"""
  #Gets client name
  while True:
    clientname = raw_input ("What's your name please?")
    if clientname.lower() == "stop": break
    if clientname in clients:
      constructDrink(clientName,"","","")
    else:
      #Gets style
      style = askStyle(questions)
      #Gets drink
      print constructDrink("",style, ingredients, stock)
      #Gets name
      cocktailname = giveName(adjectives, nouns)
      
if __name__ == "__main__":
    main()
    
