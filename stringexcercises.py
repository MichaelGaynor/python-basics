# ----------STRING EXCERCISES
# string_as_a_string = "This is a string"

# # --Uppercase a String
# print (string_as_a_string.upper())

# # --Capitalize a String
# print (string_as_a_string.capitalize())

# # --Reverse a String
# characters_from_string = []
# for character in string_as_a_string:
#   characters_from_string.append(character)
# characters_from_string.reverse()
# print (''.join(characters_from_string))

# --Leetspeak
# characters_to_be_replaced = ["A","E","G","I","O","S","T"]
# Characters_to_replace_with = ["4","3","6","1","0","5","7"]
# character_replacement_list = []

# character_replacement_list = ""

# for character in string_as_a_string:


# for character in string_as_a_string:
#   if (character.upper() == "A"):
#     character_replacement_list += "4"
#   elif (character.upper() == "E"):
#     character_replacement_list += "3"
#   elif (character.upper() == "G"):
#     character_replacement_list += "6"
#   elif (character.upper() == "I"):
#     character_replacement_list += "1"
#   elif (character.upper() == "O"):
#     character_replacement_list += "0"
#   elif (character.upper() == "S"):
#     character_replacement_list += "5"
#   elif (character.upper() == "T"):
#     character_replacement_list += "7"
#   else:
#     character_replacement_list += (character)
# print (character_replacement_list)


# for character in string_as_a_string:
#   for replaceable in characters_to_be_replaced:
#     if character.upper() == replaceable:
#       character_replacement_list.append(Characters_to_replace_with.index(replaceable))
#     else:
#       character_replacement_list.append(character)
# print (character_replacement_list)


# --Long-long Vowels
# long_vowel_string = "Bookkeeper"

# result = ""
# current = ""
# previous = ""

# for i in range(0,len(long_vowel_string)):
#   current = long_vowel_string[i]
#   if (current == previous):
#     result = result + 4 * current
#   else:
#     result = result + current
#   previous = current
# print (result)


# --Caesar Cypher
# def decrypt_function(encrypted_letter):
#   number = encrypted_list.index(encrypted_letter)
#   decrypted_message.append(decrypted_list[number])

# message = "lbh zhfg hayrnea jung lbh unir yrnearq"
# decrypted = "abcdefghijklmnopqrstuvwxyz "
# encrypted = "nopqrstuvwxyzabcdefghijklm "
# message_list = list(message)
# decrypted_list = list(decrypted)
# encrypted_list = list(encrypted)
# decrypted_message = []

# for i in range(0,len(message_list)):
#   decrypt_function(message_list[i])

# final_decrypted_message = "".join(decrypted_message)
# print (final_decrypted_message)


# ----------LIST EXCERCISES

# number_list = [1,2,-7,-7,3,5,2,2,8,15]

# --Largest Number

# while len(number_list) > 1:
#   if (number_list[0] >= number_list[1]):
#     number_list.remove(number_list[1])
#   else:
#     number_list.remove(number_list[0])
# print (number_list[0])


# --Smallest Number

# while len(number_list) > 1:
#   if (number_list[0] <= number_list[1]):
#     number_list.remove(number_list[1])
#   else:
#     number_list.remove(number_list[0])
# print (number_list[0])


# --Even Number

# for number in number_list:
#   if (number % 2 == 0):
#     print (number)


# --Positive Numbers

# for number in number_list:
#   if (number > 0):
#     print (number)


# --Positive Numbers II

# positive_numbers = []
# for number in number_list:
#   if (number > 0):
#     positive_numbers.append(number)
# print (positive_numbers)


# --Multiply an list

# factor = 3
# multiplied_number_list = []
# for number in number_list:
#   result = number * factor
#   multiplied_number_list.append(result)
# print (multiplied_number_list)


# --Multiply Vectors

# vector_list_1 = [2,4,5]
# vector_list_2 = [2,3,5000]
# vector_list_3 = []
# position = 0

# for number in vector_list_1:
#   vector_list_3.append(vector_list_1[position] * vector_list_2[position])
#   position += 1
# print (vector_list_3)


# --Matrix Addition

# our_matrix1 = [[2,-2],[5,3]]
# our_matrix2 = [[1,0],[5,6]]
# our_matrix3 = [[0,0],[0,0]]
# for i in range(len(our_matrix1)):
#   for i2 in range(len(our_matrix1[0])):
#     our_matrix3[i][i2] = our_matrix1[i][i2] + our_matrix2[i][i2]
# for r in our_matrix3:
#   print(r)


# --Matrix Addition II
# our_matrix1 = [[2,-2],[5,3]]
# our_matrix2 = [[1,0],[5,6]]
# our_matrix3 = [[0,0],[0,0]]
# for i in range(len(our_matrix1)):
#   for i2 in range(len(our_matrix1[0])):
#     our_matrix3[i][i2] = our_matrix1[i][i2] + our_matrix2[i][i2]
# for r in our_matrix3:
#   print(r)


# --De-dup
# number_list = [1,2,-7,-7,3,5,2,2,8,15]
# non_duplicate_number_list = []
# for i in number_list:
#   if (i not in non_duplicate_number_list):
#     non_duplicate_number_list.append(i)
# print (non_duplicate_number_list)


# --BONUS--Matrix Multiplication


# ----------LOOOP EXCERCISES

# -- 1 to 10
# for i in range(1,11):
#   print (i)


# -- n to m
# n = int(raw_input("Please enter a number: "))
# m = int(raw_input("Thanks! Now please enter a higher number: "))
# for i in range(n,m+1):
#   print (i)


# --Odd Numbers
# for i in range(1,11,2):
#   print (i)


# --Print a Square
# n = int(raw_input("Please pick your number!" ))
# for i in range(1,n+1):
#   print (n * "*")

# --Print a Square II
# n = int(raw_input("Please pick your number!" ))
# for i in range(1,n+1):
#   print (n * "*")

# --Print a Box
# h = int(raw_input("How high is your Box? "))
# w = int(raw_input("How wide is your Box? "))
# for i in range(1,h+1):
#   if (i == 1 or i == h):
#     print (w * "*")
#   else:
#     print ("*" + (w - 2) * " " + "*")

# --Print a Triangle
# h = 4
# h = int(raw_input("How high do you want to go with this? "))
# w = -1
# for i in range(1,h+1):
#   w = w + 2
#   print ((h-i) * " " + (w * "*") + (h-i) * " ")

# --Multiplication Table
# for number in range(1,11):
#   for numbers in range(1,11):
#     print("%i" + " X " + "%i" + " = " + "%i") % (number,numbers,number * numbers)

# BONUSES




