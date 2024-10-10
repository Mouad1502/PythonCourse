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
# No challenge just some debugging exercises
#####################################################################
# Day 14 Challenge
# logo = """
#     __  ___       __
#    / / / (_)___ _/ /_  ___  _____
#   / /_/ / / __ `/ __ \/ _ \/ ___/
#  / __  / / /_/ / / / /  __/ /
# /_/ ///_/\__, /_/ /_/\___/_/
#    / /  /____/_      _____  _____
#   / /   / __ \ | /| / / _ \/ ___/
#  / /___/ /_/ / |/ |/ /  __/ /
# /_____/\____/|__/|__/\___/_/
# """
#
# vs = """
#  _    __
# | |  / /____
# | | / / ___/
# | |/ (__  )
# |___/____(_)
# """
# from game_data import data
# import random
# print(logo)
# reps=0
# def chosenData():
#     firstChoice = random.choice(data)
#     secondChoice = random.choice(data)
#     while firstChoice == secondChoice:
#         secondChoice = random.choice(data)
#     userChoice = input(f"Who has more followers :\n A : {firstChoice['name']}\n {vs}\n B: {secondChoice['name']} \n").upper()
#     if userChoice == 'A':
#         return firstChoice, max(firstChoice['follower_count'], secondChoice['follower_count'])
#     elif userChoice == 'B':
#         return secondChoice, max(firstChoice['follower_count'], secondChoice['follower_count'])
#     else:
#         print("Invalid choice! Please select 'A' or 'B'.")
#         return chosenData()  # Re-prompt if invalid input
# def higherOrLower():
#     global reps
#     [userChoice,rightChoice] = chosenData()
#     if userChoice['follower_count'] == rightChoice :
#         reps += 1
#         print('You are right keep going \n')
#         higherOrLower()
#     else:
#         if reps == 0:
#             print("You couldn't even guess the first one right what a bummer you are :/")
#         else:
#             print(f"You failed after {reps} time(s) !!")
#         again = input("if you want to play again press 'y'.")
#         if again == 'y':
#             print(logo)
#             reps = 0
#             higherOrLower()
#         else:
#             print("Thanks for playing :D")
# higherOrLower()
#########################################################################################
# Day 15 Challenge
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# resources = {
#     "water": 300,
#     "milk": 20,
#     "coffee": 100,
# }
#
# listOfDrinks=["espresso","latte","cappuccino"]
# def pick_the_drink():
#     drinkChoice = input("What would you like? (espresso/latte/cappuccino):")
#     return drinkChoice
# def possible_drinks():
#     possibleDrinks =[]
#     for drink in listOfDrinks:
#         ingredients = MENU[drink]["ingredients"]
#         can_make = True
#         for ingredient in ingredients:
#             if resources[ingredient] < ingredients[ingredient]:
#                 can_make = False
#                 # print(f"Sorry, we don't have enough {ingredient} for a {drink}!!")
#                 break
#         if can_make == True:
#             possibleDrinks.append(drink)
#     return possibleDrinks
# def calculate_cost():
#     pennys = int(input("How many pennys are you inputing in the machine?: "))
#     dimes = int(input("How many dimes are you inputing in the machine?: "))
#     nickels = int(input("How many nickels are you inputing in the machine?: "))
#     quarters = int(input("How many quarters are you inputing in the machine?: "))
#     userCost = (pennys + dimes * 10 + nickels * 5 + quarters * 25) / 100
#     return userCost
# def check_cost(userCost,drinkChoice):
#     drinkCost = MENU[drinkChoice]["cost"]
#     if userCost >= drinkCost:
#         print("You have put enough money for the drink.")
#         print("Your change is :", userCost - drinkCost)
#     lack = drinkCost - userCost
#     while userCost < drinkCost:
#         print(f"The money you put is not enough to get you the drink of choice please add {lack}.")
#         addedCoins = calculate_cost()
#         userCost += addedCoins
# def coffee_machine():
#     userCost = calculate_cost()
#     drinkChoice = pick_the_drink()
#     while drinkChoice not in listOfDrinks:
#         print("You didn't type the right drink!!")
#         drinkChoice = pick_the_drink()
#
#     if drinkChoice in listOfDrinks:
#         if drinkChoice in possible_drinks():
#             ingredients = MENU[drinkChoice]["ingredients"]
#             for ingredient in ingredients:
#                 resources[ingredient] -= ingredients[ingredient]
#             check_cost(userCost, drinkChoice)
#         else:
#             possibleDrinks = possible_drinks()
#             print(f"The drink you ordered is not available, please choose among these drinks: {possibleDrinks}")
#             coffee_machine()
#
# coffee_machine()
#################################################################
# Day 16 Challenge ##############
# class CoffeeMaker:
#     """Models the machine that makes the coffee"""
#     def __init__(self):
#         self.resources = {
#             "water": 300,
#             "milk": 200,
#             "coffee": 100,
#         }
#
#     def report(self):
#         """Prints a report of all resources."""
#         print(f"Water: {self.resources['water']}ml")
#         print(f"Milk: {self.resources['milk']}ml")
#         print(f"Coffee: {self.resources['coffee']}g")
#
#     def is_resource_sufficient(self, drink):
#         """Returns True when order can be made, False if ingredients are insufficient."""
#         can_make = True
#         for item in drink.ingredients:
#             if drink.ingredients[item] > self.resources[item]:
#                 print(f"Sorry there is not enough {item}.")
#                 can_make = False
#         return can_make
#
#     def make_coffee(self, order):
#         """Deducts the required ingredients from the resources."""
#         for item in order.ingredients:
#             self.resources[item] -= order.ingredients[item]
#         print(f"Here is your {order.name} ☕️. Enjoy!")
# class MenuItem:
#     """Models each Menu Item."""
#     def __init__(self, name, water, milk, coffee, cost):
#         self.name = name
#         self.cost = cost
#         self.ingredients = {
#             "water": water,
#             "milk": milk,
#             "coffee": coffee
#         }
#
#
# class Menu:
#     """Models the Menu with drinks."""
#     def __init__(self):
#         self.menu = [
#             MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
#             MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
#             MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
#         ]
#
#     def get_items(self):
#         """Returns all the names of the available menu items"""
#         options = ""
#         for item in self.menu:
#             options += f"{item.name}/"
#         return options
#
#     def find_drink(self, order_name):
#         """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
#         for item in self.menu:
#             if item.name == order_name:
#                 return item
#         print("Sorry that item is not available.")
# class MoneyMachine:
#
#     CURRENCY = "$"
#
#     COIN_VALUES = {
#         "quarters": 0.25,
#         "dimes": 0.10,
#         "nickles": 0.05,
#         "pennies": 0.01
#     }
#
#     def __init__(self):
#         self.profit = 0
#         self.money_received = 0
#
#     def report(self):
#         """Prints the current profit"""
#         print(f"Money: {self.CURRENCY}{self.profit}")
#
#     def process_coins(self):
#         """Returns the total calculated from coins inserted."""
#         print("Please insert coins.")
#         for coin in self.COIN_VALUES:
#             self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
#         return self.money_received
#
#     def make_payment(self, cost):
#         """Returns True when payment is accepted, or False if insufficient."""
#         self.process_coins()
#         if self.money_received >= cost:
#             change = round(self.money_received - cost, 2)
#             print(f"Here is {self.CURRENCY}{change} in change.")
#             self.profit += cost
#             self.money_received = 0
#             return True
#         else:
#             print("Sorry that's not enough money. Money refunded.")
#             self.money_received = 0
#             return False
# from menu import Menu, MenuItem
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine
#
#
# money_machine = MoneyMachine()
# coffee_maker = CoffeeMaker()
# menu = Menu()
# is_on = True
#
#
# while is_on:
#     options = menu.get_items()
#     choice = input(f"What would you like ? ({options}): ")
#     if choice == "off":
#         is_on = False
#     elif choice == 'report':
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink = menu.find_drink(choice)
#         if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
#             coffee_maker.make_coffee(drink)
########################################################################
# Day 17 Challenge #################################
# class Question:
#     def __init__(self, text, answer):
#         self.text = text
#         self.answer = answer
# from question_model import Question
# from data import question_data
#
# question_bank = [Question(item['text'], item['answer']) for item in question_data]
#
# class QuizBrain:
#     def __init__(self):
#         self.question_number = 0
#         self.question_list = question_bank
#
#     def play(self):
#         score = 0
#         self.question_number = 0
#         for question in question_bank:
#             self.question_number += 1
#             print(f"Q.{self.question_number}: {question.text}")
#             answer = input("True or False ?")
#             if answer.lower() == question.answer.lower():
#                 score += 1
#                 print(f"Good answer !!")
#             else:
#                 print("Wrong answer :(")
#             print(f"your score is {score}/{self.question_number}")
#         print(f"You got {score}/{self.question_number} in the quiz, thanks for playing!")
#         again = input("do you want to play again? y or n ?")
#         if again == 'y':
#             self.play()
#         else:
#             print("Come back for more questions :D")
# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#     {"text": "In West Virginia, USA, if you accidentally hit an animal with your car,"
#              " you are free to take it home to eat.", "answer": "True"},
#     {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]
# from quiz_brain import QuizBrain
#
#
# quiz = QuizBrain()
# quiz.play()
##############################################################################3
# Day 18 Challenge ####################################3
# from turtle import *
# import random
# abibiz_the_turtle = Turtle()
# abibiz_the_turtle.shape("turtle")
# abibiz_the_turtle.color("blue")
# abibiz_the_turtle.pensize(3)
#
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         # Generate a random color
#         abibiz_the_turtle.pencolor(random.random(), random.random(), random.random())
#
#         abibiz_the_turtle.circle(100)  # Draw a circle with a radius of 100 units
#         abibiz_the_turtle.setheading(abibiz_the_turtle.heading() + size_of_gap)
# draw_spirograph(5)
# screen = Screen()
# screen.exitonclick()
##################################################################
# DAy 19 Challenge ############################33


