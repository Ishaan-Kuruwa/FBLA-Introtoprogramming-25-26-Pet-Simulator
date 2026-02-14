# Empty "print" statements will be used to separate lines and make text more readable
# Importing random library for later use of randomized choices
import random

# Importing Matplotlib library to display images
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Importing os, time for a clear UI
import os
import time

# Define a lambda function to clear the screen
clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Importing os, Matplotlib and Pillow libraries to display images of pet
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

# Global "run" Boolean used to run or stop game
# global run
run = False

# Define "invalid" Global boolean for later use of invalid player inputs
# global invalid
invalid = True

# Define class 'Pet" to hold pet attributes, name, and type
class Pet():

  def __init__(self):
    self.name = None
    self.pet_type = None
    self.pet_hunger = 50/100
    self.pet_health = 75/100
    self.pet_hygiene = 90/100
    self.pet_energy = 90/100
    self.pet_rest = 80/100
    self.pet_happiness = 75/100
    self.rating = None

    # Define self.mood to determine if Pet is happy, sad, angry, or tired
    # Will later display images
    self.mood = None

  # "Display_Attributes" function to print f-string of pet's updated attributes after each care cycle rounded to 2 decimal points
  def Display_Attributes (self):
    print ("Here are your pet's attributes below:")
    print (f'Hunger: {self.pet_hunger:.2f}/1')
    print (f'Health: {self.pet_health:.2f}/1')
    print (f'Hygiene: {self.pet_hygiene:.2f}/1')
    print (f'Energy: {self.pet_energy:.2f}/1')
    print (f'Rest: {self.pet_rest:.2f}/1')
    print (f'Happiness: {self.pet_happiness:.2f}/1')
    print ()
    # Pet attributes rating using conditional statement

    rating_total = (self.pet_hunger +
    self.pet_health +
    self.pet_hygiene +
    self.pet_energy +
    self.pet_rest +
    self.pet_happiness)
    rating_total /= 6
    round (rating_total, 2)
    self.rating = rating_total

    if (self.rating > 85):
      # Pet is Happy
      self.mood = "Happy"

    elif (self.rating > 70):
      # Pet is Tired
      self.mood = "Tired"

    elif (self.rating > 50):
      # Pet is Sad
      self.mood = "Sad"

    elif (self.rating < 50):
      # Pet is Angry
      self.mood = "Mad"

    # Print pet rating with f-string
    print (f"Based on your pet's current attributes, we give you a pet rating of {round (self.rating * 100, 2)}/100")
    print ()

  # Define lower random attributes as function by randomly choosing 3 attributes to lower in the range of 10-20
  def Lower_Attributes (self):
    # Pet_attributes is now variable "list"
    pet_attributes = ['pet hunger', 'pet health', 'pet hygiene', 'pet energy', 'pet rest', 'pet happiness']

    # Shuffle options using random library
    random.shuffle (pet_attributes)

    # Choose pet attributes to lower by suing zero-based indexing in lists
    pet_attributes_1 = pet_attributes[0]
    pet_attributes_2 = pet_attributes[1]
    pet_attributes_3 = pet_attributes[2]

    # Conditional statements to lower attributes
    # Used global condition to change attribute variables outside of function
    if pet_attributes_1 == 'pet hunger' or pet_attributes_2 == 'pet hunger' or pet_attributes_3 == 'pet hunger':
      self.pet_hunger -= ((random.randint (10, 20))/100)
      print (f"Your pet's hunger has dropped, it is now: {self.pet_hunger:.2f}/1")

    if pet_attributes_1 == 'pet health' or pet_attributes_2 == 'pet health' or pet_attributes_3 == 'pet health':
      self.pet_health -= ((random.randint (10, 20))/100)
      print (f"Your pet's health has dropped, it is now: {self.pet_health:.2f}/1")

    if pet_attributes_1 == 'pet hygiene' or pet_attributes_2 == 'pet hygiene' or pet_attributes_3 == 'pet hygiene':
      self.pet_hygiene -= ((random.randint (10, 20))/100)
      print (f"Your pet's hygiene has dropped, it is now: {self.pet_hygiene:.2f}/1")

    if pet_attributes_1 == 'pet energy' or pet_attributes_2 == 'pet energy' or pet_attributes_3 == 'pet energy':
      self.pet_energy -= ((random.randint (10, 20))/100)
      print (f"Your pet's energy has dropped, it is now: {self.pet_energy:.2f}/1")

    if pet_attributes_1 == 'pet rest' or pet_attributes_2 == 'pet rest' or pet_attributes_3 == 'pet rest':
      self.pet_rest -= ((random.randint (10, 20))/100)
      print (f"Your pet's rest has dropped, it is now: {self.pet_rest:.2f}/1")

    if pet_attributes_1 == 'pet happiness' or pet_attributes_2 == 'pet happiness' or pet_attributes_3  == 'pet happiness':
      self.pet_happiness -= ((random.randint (10, 20))/100)
      print (f"Your pet's happiness has dropped, it is now: {self.pet_happiness:.2f}/1")

    print ()

  # "Pet_Type" function to decide pet type
  def Pet_Type(self):

    # Pet options are stored in list
    player_pet_options = ['Dog', 'Cat', 'Fish', 'Hamster', 'Bird', 'Snake']

    # "For" loop to create lower case pets
    pets = []
    for pet in player_pet_options:
      pets.append (pet.lower())

    # Display pet options for player through "print" statement
    print ("Let's choose a pet!")
    print ('Here are your possible pet options:', player_pet_options)
    print ()

    # Make invalid variable global so can be changed inside function
    global invalid
    while invalid == True:

      # Player pet choice input
      chosen_pet_type = input('Please choose a pet.') # Store the string choice

      # Player inputs valid pet
      if chosen_pet_type.lower() in pets:
        print ('You chose:', chosen_pet_type)
        invalid = False

      # If player inputs an invalid answer, call function "invalid_answer"
      else:
        game.Invalid_Answer()

    # Capitalize string to later use in displaying images
    self.pet_type = chosen_pet_type.capitalize()

    # Reset "invalid" variable
    invalid = True

    print ()

  # "Pet_Name" function to decide pet name
  def Pet_Name (self):
    # Choose pet name
    print ("Now lets choose your pet's name!")

    # Player chooses pet name through input
    name = input ("Please choose your pet's name.")
    print ("Your pet's new name is", name)
    self.name = name
    print ()

  def Display_Pet (self):
    try: 
      pet_image = mpimg.imread (f'IntrotoProgramming25-26Images/{pet.mood}_{pet.pet_type}.png')

    except: 
      print (pet.mood, pet.pet_type)
      print ("You haven't downloaded the image folder, please do that to display images. Thank You!")
      time.sleep (2)
      return
    
    plt.imshow (pet_image)
    plt.title (f"Your Pet is {pet.mood}. Please click 'X' to continue!")
    plt.show()

class Game():
  def __init__(self):

    # Define current day to access in class
    self.day = 0

    # Define savings goal to access in class
    self.savings_goal = None
    self.savings_history = []

    # Set pet items, coins, expenses, and finances as self to access in class
    self.pet_items = []
    self.pet_coins = 100
    self.expenses = 0

    # For 3 loop outside for: different types of payments: toys/activities, food/supplies, and health care
    # Later add for 3 loop inside for: action, cost, and day #
    self.Finances = [[]for _ in range (3)]

    # Define boolean "health_care" to check if player has health care to access in class
    self.health_care = False

  def Next_Day (self):
    print ("Let's move on to the next day!")
    print ()
    for i in range (3):
      print (f"Next day in {3 - i}.")
      time.sleep (1)
    
    print()
    clear_screen()
    

  # Function "Invalid_answer" used whenever Player input is incorrect
  def Invalid_Answer(self):
    print ('Your answer is invalid. Please try again.')

  # 'Game_Start' function to decide to play
  def Game_Start(self):

    # Make "run" variable global so can be changed inside function
    global run
    while run == False:
      player_start = input ('Would you like to start?')

      # Player chose to start game
      if player_start.lower() == 'yes':
        run = True
        return True

      # Player chose to not start game
      elif player_start.lower() == 'no':
        run = False
        print ('Have a good day player!')
        print ('Please find time to play later!')
        return False

      # Invalid player input (call function "invalid_answer")
      else:
        self.Invalid_Answer()
      
      print()

  def Add_Day (self):
    self.day += 1

  # Define "Main_Menu" function for user to choose move they want to make on current day
  def Main_Menu(self):

    # Introduction to new day for player using f-string
    print (f"Hello Player, today is day {self.day}.")
    print (f"Your pet coins amount is {self.pet_coins}.")
    print (f"Your total expenses are {self.expenses}.")
    print()

    # Define options list of possible actions on given day for player
    options = ["1. Care for Pet - Upgrade your pet's attributes", "2. Check Finances - Check your financial statements",
               "3. Buy from Shop - Buy items for your pet", "4. Create a Savings Goal - Choose a savings goal",
               "5. Open Help Menu - Get Help", "6. Move to next Day - Continue your adventure", "7. Quit Game - Quit"]

    # Print each option in options with for loop
    for option in options: print (option)

    print ()
    while True:
      # Player input to decide option
      player_option = input ("Please choose an option! Please input the number of your preferred option (ex: 1, 2, etc.)")

      # Try and Except to check valid user input
      try: player_option = int (player_option)

      except:
        self.Invalid_Answer()
        continue

      # Conditionals to make sure input was a valid number
      if 1 <= player_option <= 7:
        pass

      else:
        self.Invalid_Answer()
        continue

      # Conditionals to call function for each possible option 1-6
      print()
      if player_option == 1: game.Pet_Care()
      elif player_option == 2: game.Cost_Of_Care()
      elif player_option == 3: game.Shop()
      elif player_option == 4: game.Savings_Goal()
      elif player_option == 5: Game.Help_Menu()
      elif player_option == 6: return
      elif player_option == 7: Game.Quit_Game()
      #clear_output(wait=True)
      break


  def Feed(self, actions):
    pet.pet_hunger += 20/100
    pet.pet_health += 10/100
    pet.pet_happiness += 5/100
    self.pet_coins -= actions['1. Feed']
    self.expenses += actions['1. Feed']
    self.Finances[0].append (['Feed', actions['1. Feed'], self.day])
    print ("Your pet is fed.")

  def Play (self, actions):
    pet.pet_hunger -= 10/100
    pet.pet_hygiene -= 10/100
    pet.pet_energy -= 10/100
    pet.pet_health += 20/100
    pet.pet_happiness += 20/100
    self.pet_coins -= actions['2. Play']
    self.expenses += actions['2. Play']
    self.Finances[0].append (['Play', actions['2. Play'], self.day])
    print ("Your pet played.")

  def Rest (self, actions):
    pet.pet_energy += 15/100
    pet.pet_rest += 15/100
    pet.pet_health += 5/100
    self.pet_coins -= actions['3. Rest']
    self.expenses += actions['3. Rest']
    self.Finances[0].append (['Rest', actions['3. Rest'], self.day])
    print ("Your pet rested.")

  def Clean (self, actions):
    pet.pet_hygiene += 20/100
    pet.pet_happiness += 10/100
    self.pet_coins -= actions['4. Clean']
    self.expenses += actions['4. Clean']
    self.Finances[0].append (['Clean', actions['4. Clean'], self.day])
    print ("Your pet was cleaned.")

  def Check_Health (self, actions):
    pet.pet_health += 20/100
    pet.pet_hygiene += 10/100
    self.pet_coins -= actions['5. Check Health']
    self.expenses += actions['5. Check Health']
    self.Finances[0].append (['Check Health', actions['5. Check Health'], self.day])
    print ("Your pet's health was checked.")

  # "Player_Care" function to make a move for current day
  def Pet_Care(self):

    print ("Welcome to Pet Care! Here you can choose which actions you would like to take to increase your pet's attributes!")
    print ()

    # Define "actions" list
    actions = {"1. Feed" : 15,
               "2. Play" : 7.5,
               "3. Rest" : 12.5,
               "4. Clean" : 10,
               "5. Check Health" : 10}

    pet.Display_Attributes()

    print ("Here are your actions!")
    print (actions)
    print ()

    # Get user input choice for option
    while True:
      player_action_choice = input ("Please choose the move you want to make today! Please input 'none' to do nothing or the number of your preferred action (Ex: 1, 2, etc.)")

      if player_action_choice == 'none':
        print ("Be careful, taking care of your pet is very important. See you next time!")
        return

      # Try and Except to check valid user input
      try:
        player_action_choice = int (player_action_choice)

        # Conditionals to make sure input was a valid number
        if 1 <= player_action_choice <= 10:
          pass

        else:
          continue

      except:
        self.Invalid_Answer()
        continue

      finally:
        # Conditionals to call function for each possible option 1-10
        if player_action_choice == 1: game.Feed(actions)
        elif player_action_choice == 2: game.Play(actions)
        elif player_action_choice == 3: game.Rest(actions)
        elif player_action_choice == 4: game.Clean(actions)
        elif player_action_choice == 5: game.Check_Health(actions)

        print (f"Your current Pet Coins amount is {self.pet_coins}. Spend Wisely!")
        continue

  def Cost_Of_Care(self):
    print ("Welcome to Cost of Care! Here you can check your finances.")

    finance_types = ["1. Food and Supply", "2. Toys or Activities", "3. Health Care or Vet Visits"]
    for section in finance_types: print (section)

    while True:
      type_action = input ("Let's customize your financial report! What type of finances would you like to check? (Please input 1, 2, 3 or none)")

      print (f"Your expenses are: {self.expenses}.")
      print (f"Your pet coins amount is {self.pet_coins}.")

      if type_action.lower() == 'none':
        print ("Let's Continue!")
        break

      try:
        type_action = int (type_action)
        print ("Here are your finances: ")
        for action in self.Finances[type_action-1]: print (action)

      except:
        self.Invalid_Answer()
        continue

    filters = ["1. Today", "2. Below __ (price)", "3. Above __ (price)", "4. Savings Progress"]
    print ("Let's filter your finances!")
    print (filters)
    print (self.Finances)

    while True:
      player_filter = input ("Choose a filter! (input 'none' for no filter or the number (1, 2, 3, 4) of the filter you would like.)")

      if player_filter.lower() == 'none': break

      try: player_filter = int (player_filter)

      except:
        self.Invalid_Answer()
        continue

      if player_filter == 1:
        print ("Here are your daily items: ")
        print ()
        print ("Action", "Cost", "Day")
        print ()
        for section in self.Finances:
          for item in section:
            if item[2] == self.day: print (item)

        print ()

      elif player_filter == 2:

        while True:
          below_price = input ("Please input a price so you can see all items less than/equal to that price that are yours!")
          try: below_price = int (below_price)
          except:
            self.Invalid_Answer()
            continue

          print ("Here are your selected items: ")
          print ()
          print ("Action", "Cost", "Day")
          print ()
          for section in self.Finances:
            for item in section:
              if item[1] <= below_price: print (item)
          print ()
          break

      elif player_filter == 3:

        while True:
          above_price = input ("Please input a price so you can see all items greater than/equal to that price that are yours!")
          try: above_price = int (above_price)
          except:
            self.Invalid_Answer()
            continue

          print ("Here are your selected items: ")
          print ()
          print ("Action", "Cost", "Day")
          print ()
          for section in self.Finances:
            for item in section:
              if item[1] >= above_price: print (item)

          print ()
          break

      elif player_filter == 4:

        print ("Here is your savings history: ")
        print ()
        print ("Goal", "Cost", "Day")
        print ()
        for item in self.savings_history:
          print (item)

        print ()

  def Shop(self):
    print ("Welcome to the Shop!")
    print ("Here are the items")

    # Parts of shop: Toys/Activities, Vet Visit, Supplies/Food
    shop = [{'Bed': 20,
        'Clothing': 20,
         "Treats" : 10,
           "Meat" : 20},
        {"Hiking" : 10,
"Obstacle Course" : 20,
        "Frisbee" : 5,
       "Chew Toy" : 10},
   {"Urgent Care" : 20,
         "Vaccine": 10}]

    for item in shop: print (item)

    while True:
      player_item_choice = input ("What type of item would you like to buy from the shop? (Input either 'none' for nothing, '1' for Supplies/Food, '2' for Toys/Activities, or '3' for a Vet Visit.)")

      if player_item_choice.lower() == 'none':
        print ("See you next time!")
        return

      try: player_item_choice = int (player_item_choice)

      except:
        self.Invalid_Answer()
        continue

      print (shop[player_item_choice - 1])

      item_choice = input ("Which item would you like?")

      if player_item_choice == 1:
        if item_choice.lower() == 'bed':
          print ("Your pet now has a bed!")
          self.Finances[0].append (['Bed', shop[0]['Bed'], self.day])
          self.pet_coins -= shop[0]['Bed']
          self.expenses += shop[0]['Bed']
          pet.pet_happiness += 20/100
          pet.pet_hygiene += 10/100

        elif item_choice.lower() == 'clothing':
          print ("Your pet now has clothing!")
          self.Finances[0].append (['Clothing', shop[0]['Clothing'], self.day])
          self.pet_coins -= shop[0]['Clothing']
          self.expenses += shop[0]['Clothing']
          pet.pet_happiness += 20/100
          pet.pet_energy += 10/100

        elif item_choice.lower() == 'treats':
          print ("Your pet now has treats!")
          self.Finances[0].append (['Treats', shop[0]['Treats'], self.day])
          self.pet_coins -= shop[0]['Treats']
          self.expenses += shop[0]['Treats']
          pet.pet_hunger += 10/100
          pet.pet_energy += 10/100

        elif item_choice.lower() == 'meat':
          print ("Your pet now has meat!")
          self.Finances[0].append (['Meat', shop[0]['Meat'], self.day])
          self.pet_coins -= shop[0]['Meat']
          self.expenses += shop[0]['Meat']
          pet.pet_hunger += 20/100
          pet.pet_energy += 10/100

        else:
          self.Invalid_Answer()
          continue

      elif player_item_choice == 2:

        if item_choice.lower() == "hiking":
          print ("Your pet went on a hike!")
          self.Finances[1].append (['Hiking', shop[1]['Hiking'], self.day])
          self.pet_coins -= shop[1]["Hiking"]
          self.expenses += shop[1]["Hiking"]
          pet.pet_energy += (random.randint (10, 15)/100)
          pet.pet_happiness += (random.randint (10, 15)/100)

        elif item_choice.lower() == "obstacle course":
          print ("Your pet went on an obstacle course!")
          self.Finances[1].append (['Obstacle Course', shop[1]['Obstacle Course'], self.day])
          self.pet_coins -= shop[1]["Obstacle Course"]
          self.expenses += shop[1]["Obstacle Course"]
          pet.pet_energy += (random.randint (20, 25)/100)
          pet.pet_happiness += (random.randint (15, 20)/100)

        elif item_choice.lower() == "frisbee":
          print ("Your pet now has a frisbee!")
          self.Finances[1].append (['Frisbee', shop[1]['Frisbee'], self.day])
          self.pet_coins -= shop[1]["Frisbee"]
          self.expenses += shop[1]["Frisbee"]
          pet.pet_energy += (random.randint (5, 10)/100)
          pet.pet_happiness += (random.randint (5, 10)/100)

        elif item_choice.lower() == "chew toy":
          print ("Your pet now has a chew toy!")
          self.Finances[1].append (['Chew Toy', shop[1]['Chew Toy'], self.day])
          self.pet_coins -= shop[1]["Chew Toy"]
          self.expenses += shop[1]["Chew Toy"]
          pet.pet_energy += (random.randint (10, 15)/100)
          pet.pet_happiness += (random.randint (10, 15)/100)

        else:
          self.Invalid_Answer()
          continue

      elif player_item_choice == 3:

        if item_choice.lower() == "urgent care":
          print ("Your pet went to urgent care!")
          self.Finances[2].append (['Urgent Care', shop[2]['Urgent Care'], self.day])
          self.pet_coins -= shop[2]["Urgent Care"]
          self.expenses += shop[2]["Urgent Care"]
          pet.pet_hygiene += (random.randint (10, 15)/100)
          pet.pet_health += (random.randint (15, 20)/100)

        elif item_choice.lower() == "vaccine":
          print ("Your pet got a vaccine!")
          self.Finances[2].append (['Vaccine', shop[2]['Vaccine'], self.day])
          self.pet_coins -= shop[2]["Vaccine"]
          self.expenses += shop[2]["Vaccine"]
          pet.pet_energy += (random.randint (5, 10)/100)
          pet.pet_happiness += (random.randint (10, 15)/100)

        else:
          self.Invalid_Answer()
          continue

  def Savings_Goal(self):

    while True:
      player_choice = input ("Would you like to add a savings goal?")

      if player_choice.lower() == 'yes':
        break

      elif player_choice.lower() == 'no':
        print ("No problem! Maybe next time!")
        return

      else:
        self.Invalid_Answer()
        continue

    while True:
      player_savings_goal = input ("What would you like your savings goal to be? (Choose a range at least 25 pet coins higher than your current pet coin amount)")

      try: player_savings_goal = int (player_savings_goal)

      except:
        self.Invalid_Answer()
        continue

      if player_savings_goal >= self.pet_coins + 25:
          self.savings_goal = player_savings_goal
          print (f"Your savings goal is now {player_savings_goal} Pet Coins! You have 7 days to complete your goal! Spend Wisely.")
          self.savings_history.append ([self.pet_coins, player_savings_goal, self.day])
          return

      else:
        print ("That's too Easy! I know you can do better!")
        continue

  def Help_Menu():
    print ("Welcome to the Help Menu! Below there will be 5 FAQ's about our game that will hopefully aid you:")
    print ("NOTE: If you would like to add to this game or have any problems, please check out the GitHub Repository at the top of this notebook, thank you!")
    questions = ["1. How do I exit after I am done with an option?",
                 "2. What requirements do I need to play this game?",
                 "3. What is the point/motivation of creating this game?",
                 "4. Can I contribute to this Game?",
                 "5. How can I make the game more fun?"]

    answers = ["Input 'none' and then press enter on your keyboard, you should return to the main menu of the game",
              "All you need is the ability to run the cell of this notebook, and to download the images folder into your google drive!",
              "We hope to aid students in learning to take care of a pet, and teach students about the challenges of having a pet in a fun and interactive way!",
              "Yes, we would love for you to contribute to this game and are working on making it open source! Check out our GitHub.",
              "We would recommend challenging your friends, adding more to the game to make it more fun yourself, or even doing your own research on pet care!"]

    for i in range (5):
      print (questions[i])
      print (answers[i])

    print ()
    print ("I hope this was helpful!")
    print ()

  def Quit_Game():
    global run
    run = False
    return

# Player start "print" statement
print ('Hello Player. Welcome to Build Your Virtual Pet!')
print ()

# Create instance of class "Game" and "Pet"
game = Game ()
pet = Pet()

# Check if player wants to play and Call functions to start Game
if game.Game_Start() == True:
  pet.Pet_Type()
  pet.Pet_Name()

# "While" loop to keep game going and exit whenever needed
while run:
  game.Add_Day()
  game.Main_Menu()
  pet.Lower_Attributes()
  pet.Display_Pet()
  game.Next_Day()

print (f"Your pet finished: {pet.mood}!")
print ("Thank you for Playing!")
print ("Please come back later!")