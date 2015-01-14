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
     

def askStyle (questions):
  """Asks what style of drink"""
  style = {}
  for type, key in questions.iteritems():
    print key
    style[type] = raw_input().lower() in ["y", "yes"]
  return style


def constructDrink (style, ingredients):
  """Constructs the drink"""
  drink = []
  for key in style:
    if style[key] == True:
      drink.append (random.choice(ingredients[key]))
  return drink


def giveName (adjectives, nouns):
  """Gives cocktail an original name"""
  #cocktailname = str
  cocktailname = random.choice(adjectives) + " " + random.choice(nouns)
  return cocktailname


if __name__ == "__main__":
    print constructDrink(askStyle(questions), ingredients)
    print "This is the: " + giveName(adjectives, nouns)

    
    
