# # # print "Hello, World!"
# # # # Print two different things on the same line
# # # # print ("Hello, World", "Again")

# # # print """This will ignore the new lines
# # # until it sees another
# # # three quotes"""

# # # name = "Buncha Crunch"

# # # name = "Captain " + "Crunch"

# # # the_meaning_of_life = 40 + 2
# # # print the_meaning_of_life
# # # print the_meaning_of_life % 2

# # # print the_meaning_of_life / 5 #returns 8 because it's an integer but not a float
# # # print int(4.2 + 3.1) #returns 7 because integers aren't floats

# # # Datatypes
# # # -Strings (english and words and stuff)
# # # -Numbers which are either floats (numbers with a decimal) or integers
# # # -Booleans (True or False, 1 or 0, yes or no)
# # # -lists (lists of variables in one variable)
# # # -dictionary (variables of variables)
# # # -objects (dealing with this one later)

# # # Strings
# # first_name = "Captain"
# # last_name = "Crunch"
# #Formatted
# # print "Hello, {} {}".format(first_name, last_name)
# #Placeholder
# # print "Hello, %s %s for the %dth time!" % (first_name, last_name, 10)

# # # Floats
# # # pi_the_magic_float = 3.14
# # # print pi_the_magic_float
# #The Type Method
# # # print type(pi_the_magic_float)

# #Make string with str()
# #Make integer with int()


# # # Booleans (True and False)
# # the_truth = True
# # print type(the_truth)
# # the_lie = False
# # print type(the_lie)

# # Raw Input (just Input in newest Python)
# # first_name = raw_input("First Name: ")
# # last_name = raw_input("Last Name: ")

# # # Conditionals
# # # 1 = means you want to assign something
# # # 2 == means you want to compare the left to the right

# # if(first_name == last_name):
# #   print "Your first name is the same as your last name?"

# # age = raw_input("How old are you? ")
# # age_as_int = int(age)
# # if(age_as_int >= 21):
# #   print "You can buy beer."
# # else:
# #   print "Underage banned."

# # import random
# # random_number = random.randint(1,10)
# # number_of_tries_left = 5
# # try_or_tries = "tries"

# # not_guessed = True
# # while not_guessed:
# #   guess_a_number = raw_input("Guess a number between 1 and 10. ")
# #   if (int(guess_a_number) == random_number and number_of_tries_left > 0):
# #     print ("You guessed the number!")
# #     not_guessed = False
# #     answer = raw_input("Play again? Y or N ")
# #     if (answer == "Y"):
# #       print ("HE WON AND SAID YES")
# #       number_of_tries_left = 5
# #       not_guessed = True
# #     else:
# #       print ("Fine, be that way")
# #       not_guessed = False
# #   elif (int(guess_a_number) > random_number and number_of_tries_left > 0):
# #     number_of_tries_left -= 1
# #     print ("You guessed too high, you have %d %s left!") % (number_of_tries_left, try_or_tries)
# #   elif (int(guess_a_number) < random_number and number_of_tries_left > 0):
# #     number_of_tries_left -= 1
# #     print ("You guessed way way too low, you have %d %s left!") % (number_of_tries_left, try_or_tries)
# #   else:
# #     print ("YOU LOSE!")
# #     answer = raw_input("Play again? Y or N ")
# #     if (answer == "Y"):
# #       print ("HE SAID YES!")
# #       number_of_tries_left = 5
# #       not_guessed = True
# #     else:
# #       print ("Fine, be that way")
# #       not_guessed = False


# # ------Lists


# # student1 = "Marissa"
# # student2 = "Merilee"
# # student3 = "Daniel"
# # student4 = "Chris"

# # List is a single variable with a bunch of numbered parts
# # the number that an element is in is called the "Index"

students = [
  "Marissa",
  "Merilee",
  "Daniel",
  "Chris",
  "Chad",
  "Shane",
  "Stephen",
  "Drew"
  ]


# #   # print students
# # # print (students[1])
# # # print (students[-1])

# # atlantaTeams = [
# #   "Falcons",
# #   "Braves",
# #   "Hawks",
# #   "Thrashers"
# # ]

# # # print (atlantaTeams)
# # # # To add an element to the end of a list, you can use the append Method
# # atlantaTeams.append("Atlanta United")
# # # print (atlantaTeams)
#Pop removes the last element, append adds one to the end

# # # # To delete an index, you can use the remove Method
# # atlantaTeams.remove("Thrashers")
# # # print (atlantaTeams)
# # # # We can insert into any indicie with the insert Method
# # atlantaTeams.insert(0,"Tom Brady's team")
# # # print (atlantaTeams)

# # teams_as_a_string =   "Falcons, Braves, Hawks, Thrashers"
# # teams_as_a_list = teams_as_a_string.split(",")
# # # print (teams_as_a_list)
# # # Sort will change the list
# # atlantaTeams.sort()
# # print (atlantaTeams)
# # #Sorted will sort, but NOT CHANGE the list
# # copy_of_atlanta_teams = sorted(atlantaTeams)
# # print (copy_of_atlanta_teams)

# # copy_of_atlanta_teams.reverse()
# # print (copy_of_atlanta_teams)

# # length_of_atlanta_teams = len(copy_of_atlanta_teams)
# # print (length_of_atlanta_teams)
# # print (copy_of_atlanta_teams[-1])
# # print (copy_of_atlanta_teams[length_of_atlanta_teams-1])
# # print len(atlantaTeams[0])

# # The other type of loop...For
# # for i in range(1,10):
# #   print i

# # -----For Loop Format
# # for (the thing you want to call the thing you're on) in (variable looping through)
# for student in students:
#   # print student
#   if(student == "Chris"):
#     print ("Welcome Chris!")
#   else:
#     print ("IMPOSTER")

# Set up a for loop but the range will be 0 to len-1
# students_length = len(students)
# for i in range(0,students_length):
#   print (students[i])

# # You can also add a step to determine how far you go each loop 
# for i in range(0,10,2):
#   print(i)

# If you want a portion of a list you can use the [x:y] format
# This will create a copy of the array, DOES NOT mutate or change the original
# it will start at the xth element and will stop at the yth
# print (students)
# second_and_third = students[1:3]
# print(second_and_third)
# all_but_the_first = students[1:]
# print (all_but_the_first)


# a function is a piece of code that can be called from the main bod of the program 
# the upshot is that if you have complicated code or code that is repeated often,
# a function is your answer.
# repeating yourself is BAD (except the first time through)

# A function in python is not a function, it is a definition.
# To declare a function in python you use "def"
# Functions ALWAYS have ()

# def say_hello():
#   print ("Hello")

# say_hello()

# def say_hello_with_name(name):
#   print ("Hello, "+ name)

# say_hello_with_name("Gary")
# print (name)


# def say_hello_with_default(name, in_class = "Yes"):
#   print ("Hello, "+ name)
#   print "Is student in class? " + in_class

# say_hello_with_default("Carla")
# say_hello_with_default("Max", "No")
# say_hello_with_default("Natalie", "No", "She's the best!")

#Functions always return something
# def return_user_name(name):
#   return name

# print return_user_name("YingRong")

# def make_uppercase(string):
#   return string.upper()

# normalize_string = make_uppercase("I'm a WIlD aNd cRAzy GuY")
# print normalize_string


# Lists are awesome! But it's changeable
# What if you wanted something that wasn't changeable?
# A tuple is the same in all ways as a list except:
# -1: its values cannot be changed
# -2: it uses () instead of []

# a_tuple_test = (1,5,8)
# print (a_tuple_test[1])

# a_tuple_test[1] = 6
# print (a_tuple_test)


# --DICTIONARIES
# Dictionaries are very simple objects ("associative arrays")
# They operate with a "key-value pair"
# name = "Gary"
# gender = "none"
# height = "Very short"

# person = {
#   "name" : "Gary",
#   "gender" : "none",
#   "height" : "very short"
# }

# print (person["name"])

# Can add key-value's as needed
# zombie = {}
# zombie["weapon"] = "axe"
# zombie["health"] = 100
# zombie["startX"] = 10
# zombie["startY"] = 20
# zombie["speed"] = 10

# print (zombie)

# for key,value in zombie.items():
#   print ("Zombie has a key of %s with a value of %s" % (key,value))
#   print (zombie[key])

# if (zombie["speed"] < 5):
#   zombie["position"] = zombie["startX"] + 5
# elif (zombie["speed"] < 10):
#   zombie["position"] = zombie["startX"] + 10
# else:
#   zombie["position"] = zombie["startX"] + 15

# zombie["pointless"] = "Why?"
# print (zombie)


# zombies = []
# zombies.append(
#   {
#   "speed" : 10,
#   "weapon" : "fist",
#   "name" : "Hank"
#   }
# )

# zombies.append(
#   {
#   "speed" : 5,
#   "weapon" : "baseball bat",
#   "name" : "Dean"
#   }
# )

# print (zombies[1]["speed"])

# zombies[1]["victims"] = [
#   "Jane",
#   "Mike",
#   "Jones Family" :{
#     "father" : "Jim"
#   }
# ]

# print (zombies[1]["victims"][1])


# Ways to program:
# 1. Waterfall (What we've been doing for our pygame so far)
# 2. Procedural:
  # -function
  # -Choose-your-own-adventure style
  # -Initial overhead is low
# 3. OOP (Object Oriented Programming):
  # -functions are put where they belong
  # -Initial overhead is higher, but then drops significantly
  # -Portable
  # -Reusable
  # -Makes organization much easier (if not you messed up or shouldn't use it)

# OOP is built around the idea of Class: the blueprint
# The blueprint doesn't do anything, it's not the house, 
# but it lets you build the house which you can then use

# class = the blueprint
# object = the thing
# attributes = data
# methods = actions

# class = Car()
  # public mpg=40
# myCar = Car()
# print myCar(object).mpg(attribute)

# Encapsulation: Encapsulate everything an object might need in itself (methods, etc as part of it)

# Public, Private, and Protected:
  # -We'll never use them because they aren't part of python or javascript really, 
  #   but they are in a lot of programming languages including PHP


class Person(object):
  def __init__(self, name, gender, cell, number_of_arms = 2):
    self.name = name
    self.gender = gender
    self.species = "Human"
    self.number_of_arms = number_of_arms
    self.phone = {
      "cell": cell,
      "home": "Who has a homephone anymore?"
    }

marissa = Person("Marissa", "female", "555-555-5505", 3)
# print (marissa.name, marissa.gender)
# print (marissa.species)
# print (marissa.number_of_arms)
# print (marissa.phone["cell"])

# merilee = Person("Merilee", "female")
# merilee.species = "Robot"
# print (merilee.species)