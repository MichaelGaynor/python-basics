# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }

# print (phonebook_dict["Elizabeth"])

# phonebook_dict["Kareem"] = "968-345-2345"
# print (phonebook_dict)

# del phonebook_dict["Alice"]
# print (phonebook_dict)

# phonebook_dict["Bob"] = "968-345-2345"
# print (phonebook_dict)

# print (phonebook_dict)
# print (phonebook_dict.values())
# for key, value in phonebook_dict:
#   print (key, value)

# Fixed set (probably)

# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }

# ramit_email = ramit["email"]
# print (ramit_email)

# ramit_interest1 = ramit["interests"][0]
# print (ramit_interest1)

# Jasmine_email = ramit["friends"][0]["email"]
# print (Jasmine_email)

# jasmine_interest2 = ramit["friends"][1]["interests"][1]
# print (jasmine_interest2)

# Fixed


# def letter_histogram(paragraph):
#   tally_of_letters = {}
#   for letter in paragraph:
#     if (letter in tally_of_letters):
#       tally_of_letters[letter] += 1
#     else:
#       tally_of_letters[letter] = 1
#   return tally_of_letters

# print (letter_histogram("Hello there bEEeojdnbwvbadfvpiasbvpeivbpibepisbqepivbavipqerbpiob"))


# def word_histogram(paragraph):
#   tally_of_words = {}
#   split_paragraph = paragraph.split(" ")
#   for word in split_paragraph:
#     if (word in tally_of_words):
#       tally_of_words[word] += 1
#     else:
#       tally_of_words[word] = 1
#   return tally_of_words

# # print (word_histogram("to be or not to be to to to not not to to to to, lol"))


# from collections import Counter

# def histogram_top_winners(histogram):
#   result = Counter(histogram)
#   result.most_common()
#   for key, value in result.most_common(3):
#     print ("%s: %i" % (key, value))

# print (histogram_top_winners(word_histogram("to be or not to be or to or to")))



# -------Super Bonus
listFellah = [1,45,65,4,45,"Jim",1,"Jim",3,4,1,1,True,3,45,4,1,"The Beetles",9]
def make_final_dictionary(list):
  final_dictionary = {
    "one": [],
    "two": [],
    "three": [],
    "four": [],
    "five": [],
    "six": []
  }
  items_dictionary = {}
  for item in list:
    item = str(item)
    if item in items_dictionary:
      items_dictionary[item] += 1
    else:
      items_dictionary[item] = 1
  for organized_item in items_dictionary:
    if (items_dictionary[organized_item] == 1):
      final_dictionary["one"].append(organized_item)
    elif (items_dictionary[organized_item] == 2):
      final_dictionary["two"].append(organized_item)
    elif (items_dictionary[organized_item] == 3):
      final_dictionary["three"].append(organized_item)
    elif (items_dictionary[organized_item] == 4):
      final_dictionary["four"].append(organized_item)
    elif (items_dictionary[organized_item] == 5):
      final_dictionary["five"].append(organized_item)
    elif (items_dictionary[organized_item] == 6):
      final_dictionary["six"].append(organized_item)
  print final_dictionary

make_final_dictionary(listFellah)












