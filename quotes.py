import random 

love_relationships_quotes = [ "What do you value most in relationships (trust, respect, sense of humor, etc.)", "What three important things have you learned from previous relationships?", "What are three things working well in your current relationship? What are three things that could be better?"
]

self_reflection_quotes = [ "What values do you consider most important in life (honesty, justice, altruism, loyalty, etc.)? How do your actions align with those values?", "Describe one or two significant life events that helped shape you into who you are today.?", "When do you trust yourself most? When do you find it harder to have faith in your instincts?"
]

uncomfortable_emotions_quotes = [ "What difficult thoughts or emotions come up most frequently for you?", "What do you fear most? Have your fears changed throughout life?", "What parts of daily life cause stress, frustration, or sadness? What can you do to change those experiences? "
]

newquote = input("Welcome to the journaling life. There are several subject for journal prompts, please select from the following: Love, Self or Emotions. Type your response to get started! \n")
if newquote == "Love":
  value = random.choice(love_relationships_quotes)
  print("This is your quote for today: " + value)
elif newquote == "Self":
  value = random.choice(self_reflection_quotes)
  print("This is your quote for today: " + value)
elif newquote == "Emotions":
  value = random.choice(uncomfortable_emotions_quotes)
  print("This is your quote for today: " + value)
else:
  print("Invalid Input")

response = input("Would you like another quote? Y/N ] \n")
if response == "Yes" or response == "Y":
  print("Select from the following prompts: Love, Self or Emotions.")
elif response == "No" or response == "N": 
  print("We hope to see you soon!")
else:
  print("Invalid Input")
