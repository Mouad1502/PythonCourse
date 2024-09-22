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
#Get in reeborg.ca and play the mini games using python function this is an example for the maze game:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# while not at_goal():
#     if front_is_clear():
#         move()
#         turn_right()
#     else:
#         while wall_in_front():
#             turn_left()
#         move()
#         turn_right()
#####################################################################################
# Day 7 Challenge
# import random
# word_list = [
#     'abruptly',
#     'absurd',
#     'abyss',
#     'affix',
#     'askew',
#     'avenue',
#     'awkward',
#     'axiom',
#     'azure',
#     'bagpipes',
#     'bandwagon',
#     'banjo',
#     'bayou',
#     'beekeeper',
#     'bikini',
#     'blitz',
#     'blizzard',
#     'boggle',
#     'bookworm',
#     'boxcar',
#     'boxful',
#     'buckaroo',
#     'buffalo',
#     'buffoon',
#     'buxom',
#     'buzzard',
#     'buzzing',
#     'buzzwords',
#     'caliph',
#     'cobweb',
#     'cockiness',
#     'croquet',
#     'crypt',
#     'curacao',
#     'cycle',
#     'daiquiri',
#     'dirndl',
#     'disavow',
#     'dizzying',
#     'duplex',
#     'dwarves',
#     'embezzle',
#     'equip',
#     'espionage',
#     'euouae',
#     'exodus',
#     'faking',
#     'fishhook',
#     'fixable',
#     'fjord',
#     'flapjack',
#     'flopping',
#     'fluffiness',
#     'flyby',
#     'foxglove',
#     'frazzled',
#     'frizzled',
#     'fuchsia',
#     'funny',
#     'gabby',
#     'galaxy',
#     'galvanize',
#     'gazebo',
#     'giaour',
#     'gizmo',
#     'glowworm',
#     'glyph',
#     'gnarly',
#     'gnostic',
#     'gossip',
#     'grogginess',
#     'haiku',
#     'haphazard',
#     'hyphen',
#     'iatrogenic',
#     'icebox',
#     'injury',
#     'ivory',
#     'ivy',
#     'jackpot',
#     'jaundice',
#     'jawbreaker',
#     'jaywalk',
#     'jazziest',
#     'jazzy',
#     'jelly',
#     'jigsaw',
#     'jinx',
#     'jiujitsu',
#     'jockey',
#     'jogging',
#     'joking',
#     'jovial',
#     'joyful',
#     'juicy',
#     'jukebox',
#     'jumbo',
#     'kayak',
#     'kazoo',
#     'keyhole',
#     'khaki',
#     'kilobyte',
#     'kiosk',
#     'kitsch',
#     'kiwifruit',
#     'klutz',
#     'knapsack',
#     'larynx',
#     'lengths',
#     'lucky',
#     'luxury',
#     'lymph',
#     'marquis',
#     'matrix',
#     'megahertz',
#     'microwave',
#     'mnemonic',
#     'mystify',
#     'naphtha',
#     'nightclub',
#     'nowadays',
#     'numbskull',
#     'nymph',
#     'onyx',
#     'ovary',
#     'oxidize',
#     'oxygen',
#     'pajama',
#     'peekaboo',
#     'phlegm',
#     'pixel',
#     'pizazz',
#     'pneumonia',
#     'polka',
#     'pshaw',
#     'psyche',
#     'puppy',
#     'puzzling',
#     'quartz',
#     'queue',
#     'quips',
#     'quixotic',
#     'quiz',
#     'quizzes',
#     'quorum',
#     'razzmatazz',
#     'rhubarb',
#     'rhythm',
#     'rickshaw',
#     'schnapps',
#     'scratch',
#     'shiv',
#     'snazzy',
#     'sphinx',
#     'spritz',
#     'squawk',
#     'staff',
#     'strength',
#     'strengths',
#     'stretch',
#     'stronghold',
#     'stymied',
#     'subway',
#     'swivel',
#     'syndrome',
#     'thriftless',
#     'thumbscrew',
#     'topaz',
#     'transcript',
#     'transgress',
#     'transplant',
#     'triphthong',
#     'twelfth',
#     'twelfths',
#     'unknown',
#     'unworthy',
#     'unzip',
#     'uptown',
#     'vaporize',
#     'vixen',
#     'vodka',
#     'voodoo',
#     'vortex',
#     'voyeurism',
#     'walkway',
#     'waltz',
#     'wave',
#     'wavy',
#     'waxy',
#     'wellspring',
#     'wheezy',
#     'whiskey',
#     'whizzing',
#     'whomever',
#     'wimpy',
#     'witchcraft',
#     'wizard',
#     'woozy',
#     'wristwatch',
#     'wyvern',
#     'xylophone',
#     'yachtsman',
#     'yippee',
#     'yoked',
#     'youthful',
#     'yummy',
#     'zephyr',
#     'zigzag',
#     'zigzagging',
#     'zilch',
#     'zipper',
#     'zodiac',
#     'zombie',
# ]
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
#
# logo = '''
#  _
# | |
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |
#                    |___/    '''
# lives = 6
#
# print(logo)
#
# chosen_word = random.choice(word_list)
# print(chosen_word)
#
# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print("Word to guess: " + placeholder)
#
# game_over = False
# correct_letters = []
#
# while not game_over:
#
#     print(f"****************************{lives}/6 LIVES LEFT****************************")
#     guess = input("Guess a letter: ").lower()
#
#     if guess in correct_letters:
#         print(f"You've already guessed {guess}")
#
#     display = ""
#
#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(guess)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"
#
#     print("Word to guess: " + display)
#
#     if guess not in chosen_word:
#         lives -= 1
#         print(f"You guessed {guess}, that's not in the word. You lose a life.")
#
#         if lives == 0:
#             game_over = True
#
#             print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")
#
#     if "_" not in display:
#         game_over = True
#         print("****************************YOU WIN****************************")
#
#     print(stages[lives])
################################################################################
# Day 8 Challenge ################
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         if letter.lower() in alphabet:
#             # Preserve case
#             is_upper = letter.isupper()
#             # Find the new position in the alphabet
#             position = alphabet.index(letter.lower())
#             new_position = (position + shift_amount) % len(alphabet)
#             # Convert back to uppercase if necessary
#             new_letter = alphabet[new_position].upper() if is_upper else alphabet[new_position]
#             cipher_text += new_letter
#         else:
#             # Keep non-alphabet characters unchanged
#             cipher_text += letter
#
#     print(f"Here is the encoded result: {cipher_text}")
#
# def decrypt(encrypted_text, shift_amount):
#     deciphered_text = ""
#     for letter in encrypted_text:
#         if letter.lower() in alphabet:
#             # Preserve case
#             is_upper = letter.isupper()
#             # Find the new position in the alphabet
#             position = alphabet.index(letter.lower())
#             new_position = (position - shift_amount) % len(alphabet)
#             # Convert back to uppercase if necessary
#             new_letter = alphabet[new_position].upper() if is_upper else alphabet[new_position]
#             deciphered_text += new_letter
#         else:
#             # Keep non-alphabet characters unchanged
#             deciphered_text += letter
#
#     print(f"Here is the decoded result: {deciphered_text}")
#
# def caesar():
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text = input("Type your message:\n")
#     shift = int(input("Type the shift number:\n"))
#
#     if direction == 'encode':
#         encrypt(text, shift)
#     elif direction == 'decode':
#         decrypt(text, shift)
#     else:
#         print('Invalid input. Please enter "encode" or "decode".')
#         # Rerun the `caesar` function to prompt the user again
#         caesar()
#
# caesar()
###############################################################
# Day 9 Challenge ##################################
# # TODO-1: Ask the user for input
# # TODO-2: Save data into dictionary {name: price}
# # TODO-3: Whether if new bids need to be added
# # TODO-4: Compare bids in dictionary
#
#
# print("Welcome to the auction for the land of Antartica, the starting price is going to be 100k of Bitcoin (yes we only accept crypto bcuz it is untraceable) if you are willing to join fill in some basic information about you and other bidders.")
# biddingDictionary = {}
#
# def addBidder():
#     name = input("Hello, what is your name ?")
#     bid = int(input("How much are you willing to bid? (the number should be bigger than 100 and the unit is going to be on hundreds)"))
#     biddingDictionary[name] = bid
#     askBid = input("is there any other bidder ? if YES type 'y' if NO type 'n'")
#     if askBid == 'y' :
#         addBidder()
#     elif askBid == 'n' :
#         max = biddingDictionary[next(iter(biddingDictionary))]
#         highestBid = next(iter(biddingDictionary))
#         for bidder in biddingDictionary:
#             if biddingDictionary[bidder] > max:
#                 max = biddingDictionary[bidder]
#                 highestBid = bidder
#         print(f'The bidder with the highest price is: {highestBid} with a bidding price of {max}')
# addBidder()
####################################################################
# Day 10 challenge ###########
# def add(n1, n2):
#     return n1 + n2
# def subtract(n1, n2):
#     return n1 - n2
# def multiply(n1, n2):
#     return n1 * n2
# def divide(n1, n2):
#     return n1 / n2
# calc = {
#     "+":add,
#     "-":subtract,
#     "*":multiply,
#     "/":divide
# }
# logo = """
#  _____________________
# |  _________________  |
# | | Pythonista  0.1 | |  .----------------.  .----------------.  .----------------.  .----------------.
# | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
# |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
# | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
# | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
# | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
# | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
# | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
# | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
# | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
# | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
# |_____________________|
# """
# print(logo)
# n1 = float(input("type the first number:\n"))
# n2 = float(input("type the second number:\n"))
# operation = input("""
#     Choose the operation you want to do:
#     + for addition
#     - for substraction
#     * for multiplication
#     / for division
# """)
# result=0
# if operation == '+':
#     result = calc["+"](n1,n2)
# elif operation == '-':
#     result = calc["-"](n1,n2)
# elif operation == '*':
#     result = calc['*'](n1,n2)
# elif operation == '/':
#     result = calc['/'](n1,n2)
# print(f"The result is {result}")
# again = input(f"do you still want to work with {result}? if YES type 'y' if NO type 'n'")
# while again == 'y':
#     operation = input("""
#         Choose the operation you want to do:
#         + for addition
#         - for subtraction
#         * for multiplication
#         / for division
#     """)
#     n2 = float(input("type the second number:\n"))
#     result = calc[operation](result,n2)
#     print(result)
#     again = input(f"do you still want to work with {result}? if YES type 'y' if NO type 'n'")
#     if again == 'n':
#         print("Thank you for using Pythonista :D")
####################################################################################
# Day 11 Challenge ##################################################
# logo = """
# .------.            _     _            _    _            _
# |A_  _ |.          | |   | |          | |  (_)          | |
# |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
# | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
# |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
# `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
#       |  \/ K|                            _/ |
#       `------'                           |__/
# """
# import random
# print(logo)
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# playAgain = "y"
# def drawCards(user):
#     user.append(random.choice(cards))
#     user.append(random.choice(cards))
#
# def adjustForAces(hand):
#     while sum(hand) > 21 and 11 in hand:
#         hand[hand.index(11)] = 1
#     return hand
# def blackJack():
#     computerCards = []
#     userCards = []
#     drawCards(userCards)
#     drawCards(computerCards)
#     userCards = adjustForAces(userCards)
#     print("Your cards for now are: ", userCards)
#     userScore = sum(userCards)
#     computerScore = sum(computerCards)
#     print(f"You have a total of: {userScore}")
#     print(f"The first card of the dealer is: {computerCards[0]}")
#     while userScore < 21:
#         continueGame = input(
#             "If you want to continue drawing type: 'hit' if you are satisfied with your hand type: 'stand'?")
#         if continueGame == 'hit':
#             userCards.append(random.choice(cards))
#             userCards = adjustForAces(userCards)
#             userScore = sum(userCards)
#             print(f"You have a total of: {userScore}")
#
#         if continueGame == 'stand':
#             while computerScore < 16:
#                 computerCards.append(random.choice(cards))
#                 computerCards = adjustForAces(computerCards)
#                 computerScore = sum(computerCards)
#             print(f'The dealer has: {computerScore}')
#             if userScore > computerScore or computerScore >= 21:
#                 print("You won!!")
#                 return
#         if userScore == computerScore:
#             print("The game is a draw!!")
#             return
#         if computerScore == 20:
#             print("The Dealer wins and you lose this one!")
#             return
#         if userScore == 20 and computerScore != 20:
#             print(f"You have a total of: {userScore}")
#             print(f"The dealer has a total of: {computerScore}")
#             print("You won!! Congratulations.")
#             return
#         if userScore >= 21:
#             print("You have exceeded the number needed your hand is a bust!! You lost :(")
#             return
# startGame = input("press 's' to start playing: \n")
# if startGame == 's':
#     while playAgain == 'y':
#         blackJack()
#         playAgain = input("Do you want to play again ? 'y' to say yes.")
###############################################################################
# Day 12 Challenge #################################
# logo = """
#   / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __
#  / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
# / /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |
# \____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|
# """
# import random
#
# def guess_the_number(level):
#     if level == 1:
#         number = random.randint(0,10)
#         tries = 3
#         interval = [0,10]
#         return tries, number, interval
#     if level == 2:
#         number = random.randint(0, 100)
#         tries = 5
#         interval = [0,100]
#         return tries, number, interval
#     if level == 3:
#         number = random.randint(0,1000)
#         tries = 10
#         interval = [0,1000]
#         return tries, number, interval
#
#
# def check_number(guess,number):
#     if guess < number:
#         print("The number you guessed is lower than the winning number, try again")
#     elif guess > number:
#         print("The number you guessed is higher than the winning number, try again")
#     if guess == number:
#         print(f"Congratulations, you got the winning number :{number}")
#
#
# def play_game():
#     print(logo)
#     print("Welcome to the game of Guess The Number.")
#     print("""
#     There are 3 levels to this game:
#     level 1 for easy.
#     level 2 for normal.
#     level 3 for hard.
#     """)
#     guess = 0
#     level = int(input("type '1' for easy, '2' for normal, '3' for hard: \t"))
#     [tries, number, interval] = guess_the_number(level)
#     while tries > 0 and guess != number:
#         guess = int(input(f"You have {tries} tries left, guess the number in the range of {interval}:"))
#         check_number(guess, number)
#         tries -= 1
#     if tries == 0:
#         print(f"You have used all the tries granted for your level :(, the winning number is {number} .")
#
#
# while True:
#     play_game()
#     playAgain = input("if you want to play again, press 'a'.")
#     if playAgain != 'a':
#         print("Thanks for playing.")
#         exit()
#########################################################################################
# Day 13 Challenge ###########################################



