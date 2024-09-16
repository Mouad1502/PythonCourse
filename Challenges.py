## Day 1 Challenge
# print("Click Run to run the final project you will build")
# print("Welcome to the Band Name Generator.")
# CityName = input("What's the name of the city you grew up in?\n")
# PetName = input("What's the name of your pet's name ?\n")
# print("Your band name is : ", CityName, PetName)
##################################################################
## Day 2 Challenge
# print("Welcome to the tip calculator:")
# print("====================")
# totalBill = float(input("What was the total bill?"))
# tip = float(input("How much tip would you like to give? 10, 12 or 15?"))
# numberPeople = int(input("How many people to split the bill?"))
# if(tip == 10):
#     print("Each person should pay:", round(totalBill*1.1/numberPeople,2))
# elif(tip == 12):
#     print("Each person should pay:", round(totalBill * 1.12 / numberPeople,2))
# elif(tip == 15):
#     print("Each person should pay:", round(totalBill * 1.15 / numberPeople,2))
# else:
#     print("the tip chosen is not taken by consideration.")
#################################################################################
## Day3 Challenge
# print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
# choice = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' .")
# if choice == 'left':
#     print("You made the right choice, proceed to the next step!")
# else:
#     print("You fell into a hole, Game Over :(")
# choice = input("Now you re in front of a swamp and something is going on inside the water make your choice : 'swim' or 'wait' .")
# if choice == 'wait':
#     print("You made the right choice, proceed to the next step!")
# else:
#     print("You got attacked by trout, Game Over :(")
# choice = input("A path is gettting carved in the middle of the swamp, now you have 3 doors in front of you each one has its distinctive colour, choose which door you re going to go through: 'blue', 'red' or 'yellow' .")
# if choice == 'blue':
#     print("You got eaten by beasts, Game Over :(")
# elif choice == 'red':
#     print("You got burned by fire, Game Over :(")
# elif choice == 'yellow':
#     print("Congratulations you survived the game of fate!!")
# else:
#     print("Game over you can't even choose the right color :/ !")
##############################################################################
## Day 4 Challenge
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# import random
# compChoice = random.randint(0,2)
# userChoice = int(input("Choose between 0 for paper, 1 for rock and 2 for scissors :"))
# if(userChoice == 0):
#     print(paper)
#     if compChoice == 1:
#         print(rock)
#         print("You won :D")
#     elif compChoice == 0:
#         print(paper)
#         print("it's a tie :|")
#     elif compChoice == 2:
#         print(scissors)
#         print("You lost :/")
# if(userChoice == 1):
#     print(rock)
#     if compChoice == 1:
#         print(rock)
#         print("it's a tie :|")
#     elif compChoice == 0:
#         print(paper)
#         print("You lost :/")
#     elif compChoice == 2:
#         print(scissors)
#         print("You won :D")
# if(userChoice == 2):
#     print(scissors)
#     if compChoice == 1:
#         print(rock)
#         print("You lost :/")
#     elif compChoice == 0:
#         print(paper)
#         print("You won :D")
#     elif compChoice == 2:
#         print(scissors)
#         print("it's a tie :|")
################################################
# Day 5 Challenge
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# initialPwd=""
# for i in range(0,nr_letters):
#     initialPwd += letters[random.randint(0,len(letters)-1)]
# for i in range(0,nr_symbols):
#     initialPwd += symbols[random.randint(0, len(symbols) - 1)]
# for i in range(0,nr_numbers):
#     initialPwd += numbers[random.randint(0,len(numbers)-1)]
# l = list(initialPwd)
# random.shuffle(l)
# pwd = ''.join(l)
# print(pwd)
###########################################################################################
# Day 6 Challenge
