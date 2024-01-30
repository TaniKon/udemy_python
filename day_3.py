# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi = round(weight / height ** 2)
# if bmi <= 18.5:
#     print(f"Your BMI is {bmi}, you are ", '\033[96m' + 'underweight' + '\033[0m')
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a ", '\033[92m' + 'normal weight' + '\033[0m')
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are ", '\033[93m' + 'slightly overweight' + '\033[0m')
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are ", '\033[93m' + 'obese' + '\033[0m')
# else:
#     print(f"Your BMI is {bmi}, you are ", '\033[91m' + 'clinically obese' + '\033[0m')

# 🚨 Don't change the code below 👇
#year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#if year % 4 == 0 and year % 100 != 0:
#     print("Leap year.")
# elif year % 400 == 0:
#     print("Leap year.")
# else:
#     print("Not leap year.")

  # if year % 4 == 0:
  #   if year % 100 == 0:
  #     if year % 400 == 0:
  #       print("Leap year")
  #     else:
  #       print("Not leap year")
  #   else:
  #     print("Leap year")
  # else:
  #   print("Not leap year")

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#   print ("you can drive")
#   age = int(input("what is your age?"))
#   if age <12:
#     print ("pay $5")
#   elif age <= 18:
#     print ("pay $7")
#   elif age >= 45 and age <= 55:
#     print ("pay $0")
#   else:
#     print ("pay $12")

# else:
#   print ("no ride")

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
final_bill = 0

if size == "S":
  # bill += 15
  final_bill = 15
  if add_pepperoni ==  "Y":
    final_bill += 2
elif size == "M":
  final_bill = 20
  if add_pepperoni ==  "Y":
    final_bill += 3
else:
  final_bill = 25
  if add_pepperoni ==  "Y":
    final_bill += 3
if extra_cheese == "Y":
  final_bill += 1
print (f"Your final bill is: ${final_bill}.")

#instruktor
# print("Thank you for choosing Python Pizza Deliveries!")
# size = input()  # What size pizza do you want? "S", "M", or "L"
# add_pepperoni = input()  # Do you want pepperoni? "Y" or "N"
# extra_cheese = input()  # Do you want extra cheese? "Y" or "N"

# # Your code below this line 👇
# bill = 0
# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# else:
#   bill += 25

# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3

# if extra_cheese == "Y":
#   bill += 1

# print(f"Your final bill is: ${bill}.")


#love calculator
# print("The Love Calculator is calculating your score...")
# name1 = input()  # What is your name?
# name2 = input()  # What is their name?
# # Your code below this line 
# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e

# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e

# score = int(str(first_digit) + str(second_digit))
# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")
