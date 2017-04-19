# # print "Hello, World!"
# # # Print two different things on the same line
# # # print ("Hello, World", "Again")

# # print """This will ignore the new lines
# # until it sees another
# # three quotes"""

# # name = "Buncha Crunch"

# # name = "Captain " + "Crunch"

# # the_meaning_of_life = 40 + 2
# # print the_meaning_of_life
# # print the_meaning_of_life % 2

# # print the_meaning_of_life / 5 #returns 8 because it's an integer but not a float
# # print int(4.2 + 3.1) #returns 7 because integers aren't floats

# # Datatypes
# # -Strings (english and words and stuff)
# # -Numbers which are either floats (numbers with a decimal) or integers
# # -Booleans (True or False, 1 or 0, yes or no)
# # -lists (lists of variables in one variable)
# # -dictionary (variables of variables)
# # -objects (dealing with this one later)

# # Strings
# first_name = "Captain"
# last_name = "Crunch"
# print "Hello, {} {}".format(first_name, last_name)
# print "Hello, %s %s for the %dth time!" % (first_name, last_name, 10)

# # Floats
# # pi_the_magic_float = 3.14
# # print pi_the_magic_float
# # print type(pi_the_magic_float)


# # Booleans (True and False)
# the_truth = True
# print type(the_truth)
# the_lie = False
# print type(the_lie)

# Raw Input
# first_name = raw_input("First Name: ")
# last_name = raw_input("Last Name: ")

# # Conditionals
# # 1 = means you want to assign something
# # 2 == means you want to compare the left to the right

# if(first_name == last_name):
#   print "Your first name is the same as your last name?"

# age = raw_input("How old are you? ")
# age_as_int = int(age)
# if(age_as_int >= 21):
#   print "You can buy beer."
# else:
#   print "Underage banned."

import random
random_number = random.randint(1,10)
number_of_tries_left = 5
try_or_tries = "tries"

not_guessed = True
while not_guessed:
  guess_a_number = raw_input("Guess a number between 1 and 10. ")
  if (int(guess_a_number) == random_number and number_of_tries_left > 0):
    print ("You guessed the number!")
    not_guessed = False
    answer = raw_input("Play again? Y or N ")
    if (answer == "Y"):
      print ("HE WON AND SAID YES")
      number_of_tries_left = 5
      not_guessed = True
    else:
      print ("Fine, be that way")
      not_guessed = False
  elif (int(guess_a_number) > random_number and number_of_tries_left > 0):
    number_of_tries_left -= 1
    print ("You guessed too high, you have %d %s left!") % (number_of_tries_left, try_or_tries)
  elif (int(guess_a_number) < random_number and number_of_tries_left > 0):
    number_of_tries_left -= 1
    print ("You guessed way way too low, you have %d %s left!") % (number_of_tries_left, try_or_tries)
  else:
    print ("YOU LOSE!")
    answer = raw_input("Play again? Y or N ")
    if (answer == "Y"):
      print ("HE SAID YES!")
      number_of_tries_left = 5
      not_guessed = True
    else:
      print ("Fine, be that way")
      not_guessed = False
