# fruits = ["apple", "peach", "pear"]
# for fruit in fruits:
#   print(fruit)
#   print(fruit + " Pie")
# print(fruits)

# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆


# #Write your code below this row 👇

# all_height = 0
# for height in student_heights:
#   all_height += height

# all_students = 0
# for student in student_heights:
#   all_students += 1
  
# average_height = round(all_height / all_students)
# print(average_height)

##other solution
## all_height = sum(student_heights)
## all_students = len (student_heights)
## average_height = round(all_height/all_students)

# 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# highest_score = 0
# for score in student_scores:
#   if score > highest_score:
#     highest_score = score

    
# print(f"The highest score in the class is: {highest_score}")

##another solution
##highest_score = max(student_scores)

# even_numbers = 0
# for i in range(2,101,2):
#     even_numbers += i
# print( even_numbers)


# for i in range (1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         i = "FizzBuzz"
#     elif i % 3 == 0:
#         i = "Fizz"
#     elif i % 5 == 0:
#         i = "Buzz"
#     print (i)
