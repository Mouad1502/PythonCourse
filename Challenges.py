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