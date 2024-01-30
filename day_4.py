# # import random

# # random_integer = random.randint(1,10)
# # print(random_integer)

# # random_float = random.random()*5
# # print(random_float)

# # love_score = random.randint(1,100)
# # print(f"Your love crore is {love_score}")

# # Import the random module here

# # Split string method
# # names_string = input("Give me everybody's names, separated by a comma. ")
# # names = names_string.split(", ")
# # # 🚨 Don't change the code above 👆

# # #Write your code below this line 👇
# # print (names)

# # import random
 
# # for i in range(len(names)):
# #     name_choice = random.choice(names)
    
# # print(name_choice)
# # fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# # vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
     
# # dirty_dozen = [fruits, vegetables]
     
# # print(dirty_dozen[1][1])


# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# horizontal = int(position[0])
# vertical = int(position[1])

# map[vertical - 1][horizontal - 1] = "X"



# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
# # 🚨 Don't change the code above 👆
# # Write your code below this row 👇
# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = "X"

# # Write your code above this row 👆
# # 🚨 Don't change the code below 👇
# print(f"{line1}\n{line2}\n{line3}")




# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissors]

choice = int(input("what you choose? rock - 0, paper - 1 or scissors - 2? "))

if choice >= 3 or choice < 0: 
  print("You typed an invalid number, you lose!") 
else:
  print (game[choice])
  
  computer_choice = random.randint(0,2)
  print("Computer chose:")
  print(game[computer_choice])
  
  
  if choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and choice == 2:
    print("You lose")
  elif computer_choice > choice:
    print("You lose")
  elif choice > computer_choice:
    print("You win!")
  elif computer_choice == choice:
    print("It's a draw")

# import random

# random_number = random.randint(0,1)

# if random_number == 1:
#   print ("Heads")
# else:
#   print("Tails")

# names = names_string.split(", ")
# # The code above converts the input into an array seperating
# #each name in the input by a comma and space.
# # 🚨 Don't change the code above 👆
# import random

# num_items = len(names)
# random_choice = random.randint(0, num_items - 1)
# person_who_pay = names[random_choice]
# print(person_who_pay + " is going to buy the meal today!")
