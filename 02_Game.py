# Empty "print" statements will be used to separate lines and make text more readable
# Importing random library for later use of randomized choices
import random

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

# Define class 'Pet" to hold player's pet and functions relating to it
class Pet():

  # Define function "__init__" with attributes of pet like name, type, etc.
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

    # Calculating rating of pet using mean calculation: sum of total / # of attributes
    rating_total = (self.pet_hunger +
    self.pet_health +
    self.pet_hygiene +
    self.pet_energy +
    self.pet_rest +
    self.pet_happiness)
    rating_total /= 6

    # Rounding rating total to 2nd decimal place for clean UI
    round (rating_total, 2)
    self.rating = rating_total

    # Pet attributes rating using conditional "if, elif" statement
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

    # "pet_attributes" is now a list
    pet_attributes = ['pet hunger', 'pet health', 'pet hygiene', 'pet energy', 'pet rest', 'pet happiness']

    # Shuffle options using random library to vary attributes chosen
    random.shuffle (pet_attributes)

    # Choose pet attributes to lower by using zero-based indexing in lists
    pet_attributes_1 = pet_attributes[0]
    pet_attributes_2 = pet_attributes[1]
    pet_attributes_3 = pet_attributes[2]
    
    # Lowering attributes after each day keeps game challenging and captivating for the player!
    # Conditional "if" statements to lower attributes
    # Used "random.randint()" to vary differences each time
    # Used "f-strings" to print readable updated attributes
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
    # Assign name to "self" attribute in class "Pet"
    self.name = name
    print ()

  # "Display_Pet" function to display images of user pet
  def Display_Pet (self):

    # "try and except" used to determines if user has image folder
    try: 
      pet_image = mpimg.imread (f'IntrotoProgramming25-26Images/{pet.mood}_{pet.pet_type}.png')

    except: 
      print (pet.mood, pet.pet_type)
      if pet.mood == None: print ("You haven't fed your pet yet. Come back later!")
      else: print ("You haven't downloaded the image folder, please do that to display images. Thank You!")
      time.sleep (2)
      return
    
    # Using "maplotlib" library to display images, set title to instructions to leave image
    plt.imshow (pet_image)
    plt.title (f"Your Pet is {pet.mood}. Please click 'X' to continue!")
    plt.show()
    clear_screen()

# Define class "Game" to hold all functions containing user's game
class Game():

  # Define init of self to contain main variables
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

  # Define "Instructions" function to teach user how to play game
  def Instructions():
    clear_screen()
    print ("Welcome to Virtupet!")
    time.sleep (1)
    print()
    print ("Virtupet - Instructions")
    print()
    print ("In this game, you are reponsible for caring for your virtual pet. \nYour goal is to keep your pet healthy, happy, and financially supported.")
    print()
    time.sleep (2)
    print ("HOW TO PLAY")
    print ("------------------------------------")
    print ("Each day, you can choose to:")
    print ("1. Take care of your pet")
    print ("2. Check your financials")
    print ("3. Buy from the shop")
    print ("4. Create a savings goal")
    print ("5. Check the Help Menu")
    print ("6. Move onto the next day")
    print ("7. Quit the Game")
    print ("------------------------------------")
    print()
    print ("IMPORTANT RULES")
    print ("------------------------------------")
    print ("Keep your pet's health up. Make sure to check on your pet's attributes.")
    print ("Spend Wisely.")
    print ("Keep your pet in the best mood possible!")
    print ("------------------------------------")
    print()
    print ("OBJECTIVE")
    print ("------------------------------------")
    print ("Stay alive for as long as you can!")
    print ("Let's become amazing pet owners together!")
    move_on = input ("Are you ready to move on? (Click any key to move on)")
    clear_screen()
    if move_on == str: 
      return

  # Define "Next_Day" function to move onto next day for player
  def Next_Day (self):
    # global run variable, if false leave game
    global run
    if run == False: return

    print ("Let's move on to the next day!")
    print ()

    # Use "for" loop along with time to create active UI and suspense for user
    for i in range (3):
      print (f"Next day in {3 - i}.")
      time.sleep (1)
    
    # Function "clear_screen" used
    print()
    clear_screen()
    

  # Function "Invalid_answer" used whenever Player input is incorrect
  def Invalid_Answer(self):
    print ('Your answer is invalid. Please try again.')

  # 'Game_Start' function to decide to play
  def Game_Start(self):

    # Make "run" variable global so can be changed inside function
    global run
    # "While" loop to validate user input
    while run == False:
      player_start = input ('Would you like to start?')

      # Player chose to start game
      # leave loop if player says yes
      if player_start.lower() == 'yes':
        run = True
        return True

      # Player chose to not start game
      # Run becomes false, return False to exit game
      elif player_start.lower() == 'no':
        run = False
        print ('Have a good day player!')
        print ('Please find time to play later!')
        return False

      # Invalid player input (call function "Invalid_Answer")
      else:
        self.Invalid_Answer()
      
      print()

  # Define "Add_Day" function to add day
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


    print ()

    # "While loop" to let player make choices until wants to quit
    while run == True:

      # Print each option in options with for loop
      for option in options: print (option)

      # Player input to decide option
      player_option = input ("Please choose an option! Please input the number of your preferred option (ex: 1, 2, etc.)")

      # Try and Except to check valid user input
      try: player_option = int (player_option)

      except:
        self.Invalid_Answer()
        continue

      # Conditionals "if, else" to make sure input was a valid number
      if 1 <= player_option <= 7:
        pass

      else:
        self.Invalid_Answer()
        continue

      # Conditionals "if, elif" to call function for each possible option 1-6
      print()
      if player_option == 1: game.Pet_Care()
      elif player_option == 2: game.Cost_Of_Care()
      elif player_option == 3: game.Shop()
      elif player_option == 4: game.Savings_Goal()
      elif player_option == 5: Game.Help_Menu()
      elif player_option == 6: return
      elif player_option == 7: Game.Quit_Game()

      # Clear screen for clear UI
      clear_screen()
      continue

  # Define "Feed" function so pet is fed, update pet coins, expenses, and finances
  def Feed(self, actions):
    pet.pet_hunger += 20/100
    pet.pet_health += 10/100
    pet.pet_happiness += 5/100
    self.pet_coins -= actions['1. Feed']
    self.expenses += actions['1. Feed']
    self.Finances[0].append (['Feed', actions['1. Feed'], self.day])
    print ("Your pet is fed.")

  # Define "Play" function so pet can play, update pet coins, expenses, and finances
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

  # Define "Rest" function so pet can rest, update pet coins, expenses, and finances
  def Rest (self, actions):
    pet.pet_energy += 15/100
    pet.pet_rest += 15/100
    pet.pet_health += 5/100
    self.pet_coins -= actions['3. Rest']
    self.expenses += actions['3. Rest']
    self.Finances[0].append (['Rest', actions['3. Rest'], self.day])
    print ("Your pet rested.")

  # Define "Clean" function so pet is Clean, update pet coins, expenses, and finances
  def Clean (self, actions):
    pet.pet_hygiene += 20/100
    pet.pet_happiness += 10/100
    self.pet_coins -= actions['4. Clean']
    self.expenses += actions['4. Clean']
    self.Finances[0].append (['Clean', actions['4. Clean'], self.day])
    print ("Your pet was cleaned.")

  # Define "Check_Health" function so pet's health is increased, update pet coins, expenses, and finances
  def Check_Health (self, actions):
    pet.pet_health += 20/100
    pet.pet_hygiene += 10/100
    self.pet_coins -= actions['5. Check Health']
    self.expenses += actions['5. Check Health']
    self.Finances[0].append (['Check Health', actions['5. Check Health'], self.day])
    print ("Your pet's health was checked.")

  # "Player_Care" function to make a move for current day
  def Pet_Care(self):
    
    # Welcome player to pet care
    print ("Welcome to Pet Care! Here you can choose which actions you would like to take to increase your pet's attributes!")
    print ()

    # Define "actions" list
    actions = {"1. Feed" : 15,
               "2. Play" : 7.5,
               "3. Rest" : 12.5,
               "4. Clean" : 10,
               "5. Check Health" : 10}

    # Call function "Display_Attributes"
    pet.Display_Attributes()

    # Print actions
    print ("Here are your actions!")
    print (actions)
    print ()

    # Get user input choice for option
    while True:
      player_action_choice = input ("Please choose the move you want to make today! Please input 'none' to return to the menu or the number of your preferred action (Ex: 1, 2, etc.)")

      # "if" conditional used to return if player doesn't want to make a choice
      if player_action_choice == 'none':
        print ("Be careful, taking care of your pet is very important. See you next time!")
        return

      # "try, except, finally" conditionals used to check valid user input
      try:
        player_action_choice = int (player_action_choice)

        # Conditionals "if, else" to make sure input was a valid number
        if 1 <= player_action_choice <= 10:
          pass

        else:
          continue

      except:
        self.Invalid_Answer()
        continue

      finally:
        # Conditionals "if, elif" to call function for each possible option 1-10
        if player_action_choice == 1: game.Feed(actions)
        elif player_action_choice == 2: game.Play(actions)
        elif player_action_choice == 3: game.Rest(actions)
        elif player_action_choice == 4: game.Clean(actions)
        elif player_action_choice == 5: game.Check_Health(actions)

        print (f"Your current Pet Coins amount is {self.pet_coins}. Spend Wisely!")
        continue

  # Define "Cost_Of_Care" function
  def Cost_Of_Care(self):
    print ("Welcome to Cost of Care! Here you can check your finances.")

    # List of finance types
    finance_types = ["1. Food and Supply", "2. Toys or Activities", "3. Health Care or Vet Visits"]
    # Print each section
    for section in finance_types: print (section)
    
    # "While" loop to let user input multiple times
    while True:
      type_action = input ("Let's customize your financial report! What type of finances would you like to check? (Please input 1, 2, 3 or none)")

      print (f"Your expenses are: {self.expenses}.")
      print (f"Your pet coins amount is {self.pet_coins}.")

      # "if" conditional used to return to main menu
      if type_action.lower() == 'none':
        print ("Let's Continue!")
        break
      
      # "try and except" conditionals used to validate input
      try:
        type_action = int (type_action)
        print ("Here are your finances: ")
        # print each action
        for action in self.Finances[type_action-1]: print (action)

      except:
        self.Invalid_Answer()
        continue
    
    # "filters" list defined
    filters = ["1. Today", "2. Below __ (price)", "3. Above __ (price)", "4. Savings Progress"]
    print ("Let's filter your finances!")
    print (filters)
    print (self.Finances)

    # "While" loop used to let user input multiple times
    while True:
      player_filter = input ("Choose a filter! (input 'none' for no filter or the number (1, 2, 3, 4) of the filter you would like.)")

      # "if" conditional for user to return to menu
      if player_filter.lower() == 'none': break

      # "try and except" conditionals used to check valid input
      try: player_filter = int (player_filter)

      except:
        self.Invalid_Answer()
        continue
      
      # "if, elif" conditionals used to 
      if player_filter == 1:
        print ("Here are your daily items: ")
        print ()
        print ("Action", "Cost", "Day")
        print ()
        # nested for loops to print each item in section
        for section in self.Finances:
          for item in section:
            if item[2] == self.day: print (item)

        print ()

      elif player_filter == 2:
        
        # "While" loop used to validate user input
        while True:
          below_price = input ("Please input a price so you can see all items less than/equal to that price that are yours!")
          # "try and except" used to validate input
          try: below_price = int (below_price)
          except:
            self.Invalid_Answer()
            continue

          print ("Here are your selected items: ")
          print ()
          print ("Action", "Cost", "Day")
          print ()
          # Nested for loop used to print each item in section
          for section in self.Finances:
            for item in section:
              if item[1] <= below_price: print (item)
          print ()
          break

      elif player_filter == 3:

        # "While" loop used to validate user input
        while True:
          above_price = input ("Please input a price so you can see all items greater than/equal to that price that are yours!")
          # "try and except" used to validate input
          try: above_price = int (above_price)
          except:
            self.Invalid_Answer()
            continue

          print ("Here are your selected items: ")
          print ()
          print ("Action", "Cost", "Day")
          print ()
          # Nested for loop used to print each item in section
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
        # "for" loop used to print each item
        for item in self.savings_history:
          print (item)

        print ()

  # Define "Shop" function
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

    # "for" loop used to print each item
    for item in shop: print (item)

    # "While" loop used to validate user input
    while True:
      player_item_choice = input ("What type of item would you like to buy from the shop? (Input either 'none' to return to the menu, '1' for Supplies/Food, '2' for Toys/Activities, or '3' for a Vet Visit.)")

      # "if" conditional used to return to menu
      if player_item_choice.lower() == 'none':
        print ("See you next time!")
        return

      # "try and except" conditional used to validate input
      try: player_item_choice = int (player_item_choice)

      except:
        self.Invalid_Answer()
        continue

      print (shop[player_item_choice - 1])

      item_choice = input ("Which item would you like?")

      # "if" conditionals used to check each user item choice
      # In each "if" condition, add "if" conditionals for each possible item
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

  # Define "Savings_Goal" function
  def Savings_Goal(self):

    # "While" loop used to validate user input
    while True:
      player_savings_goal = input (f"What would you like your savings goal to be? (Your amount must be greater than {self.pet_coins + 25}.)")

      # "try and except" conditionals to validate user input
      try: player_savings_goal = int (player_savings_goal)

      except:
        self.Invalid_Answer()
        continue
      
      # "if, else" conditionals to make sure savings goal is valid
      if player_savings_goal >= self.pet_coins + 25:
          self.savings_goal = player_savings_goal
          print (f"Your savings goal is now {player_savings_goal} Pet Coins! You have 7 days to complete your goal! Spend Wisely.")
          self.savings_history.append ([self.pet_coins, player_savings_goal, self.day])
          time.sleep (2)
          return

      else:
        print ("That's too Easy! I know you can do better!")
        continue
  
  # Function "Pet_Coins_Game" to let user win pet coins after each day
  def Pet_Coins_Game (self):
    print ("Let's take a shot at winning some pet coins!")

    # "for" loop used to play game 3 times for player
    for i in range (3):
      
      # Winning number and pet coin amounts using "randint"
      winning_number = random.randint (1, 3)
      winning_pet_coins = random.randint (10, 30)

      # While loop for user validation
      while True:

        # User input of chosen number
        player_number = input ("Please choose a number from 1-3 to win pet coins from 10-30!")

        # Try and Except to determine if valid input
        try:
          player_number = int (player_number)

          # "if, else" conditionals to see if user won or not
          if player_number == winning_number:
            print (f"You won {winning_pet_coins} Pet Coins!")
            self.pet_coins += winning_pet_coins

          else:
            print ("You lost...")

          break

        except:
          game.Invalid_Answer()
          continue

      print (f"Your new Pet Coin balance is {self.pet_coins}!")

    print ()

  # Define "Check_Pet_Coins" function to make sure player doesn't go bankrupt or encourage/alert player's spending habits
  def Check_Pet_Coins(self):

    # "If, elif" conditionals to use print statements or exit game if player is bankrupt
    if self.pet_coins <= 0: 
      print ("You are bankrupt... Be careful with your spending next time. Play a new game to start over!")
      # global run to access variable
      global run
      run = False
      return False
    
    elif self.pet_coins >= 0: print ("Nice Job! You have a lot of coins! Let's continue!")
    elif self.pet_coins <= 50: print ("Your pet coins are low! You might want to calm down on spending...")

  # Define "Help_Menu" function
  def Help_Menu():
    clear_screen()
    print ("Welcome to the Help Menu! Below there will be 5 FAQ's about our game that will hopefully aid you:")
    print()
    print ("NOTE: If you would like to add to this game or have any problems, please check out the GitHub Repository at the top of this notebook, thank you!")
    print()
    # List "questions" to store questions
    questions = ["1. How do I exit after I am done with an option?",
                 "2. What requirements do I need to play this game?",
                 "3. What is the point/motivation of creating this game?",
                 "4. Can I contribute to this Game?",
                 "5. How can I make the game more fun?"]

    # List "answer" to store answers to questions
    answers = ["Input 'none' and then press enter on your keyboard, you should return to the main menu of the game",
              "All you need is the ability to run the cell of this notebook, and to download the images folder into your google drive!",
              "We hope to aid students in learning to take care of a pet, and teach students about the challenges of having a pet in a fun and interactive way!",
              "Yes, we would love for you to contribute to this game and are working on making it open source! Check out our GitHub.",
              "We would recommend challenging your friends, adding more to the game to make it more fun yourself, or even doing your own research on pet care!"]

    # "for" loop for 5 iterations to print each question and answer
    for i in range (5):
      print (questions[i])
      print (answers[i])

    print ()
    print ("I hope this was helpful!")
    print ()
    continue_game = input ("Would you like to continue? (Press any key to continue.)")
    if continue_game == str: return

  # Define "Quit_Game" function
  def Quit_Game():
    # global run to access variable
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
  Game.Instructions()
  pet.Pet_Type()
  pet.Pet_Name()

# "While" loop to keep game going and exit whenever needed
# Call all functions in run loop
while run:
  game.Add_Day()
  game.Main_Menu()
  if run == False: break
  pet.Lower_Attributes()
  game.Check_Pet_Coins()
  pet.Display_Pet()
  game.Pet_Coins_Game()
  game.Next_Day()

# Ending of game
print (f"Your pet finished: {pet.mood}!")
print ("Thank you for Playing!")
print ("Please come back later!")
