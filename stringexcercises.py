# ----------STRING EXCERCISES
string_as_a_string = "This is a string"

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
# position = 0

# for character in string_as_a_string:



# for character in string_as_a_string.upper():
#   if (character == "A"):
#     character_replacement_list.append("4")
#   elif (character == "E"):
#     character_replacement_list.append("3")
#   elif (character == "G"):
#     character_replacement_list.append("6")
#   elif (character == "I"):
#     character_replacement_list.append("1")
#   elif (character == "O"):
#     character_replacement_list.append("0")
#   elif (character == "S"):
#     character_replacement_list.append("5")
#   elif (character == "T"):
#     character_replacement_list.append("7")
#   else:
#     character_replacement_list.append(character)
# print ("".join(character_replacement_list))


# for character in string_as_a_string.upper():
#   for replaceable in characters_to_be_replaced:
#     print string_as_a_string.upper()
#     print (character)
#     print (replaceable)
#     if character == replaceable:
#       print (replaceable)
#       print (character)
#       print Characters_to_replace_with.index(replaceable)
#       print Characters_to_replace_with.index(character)
#       character_replacement_list.append(Characters_to_replace_with.index(replaceable))
#     else:
#       print (character)
#       character_replacement_list.append(character)
# print (character_replacement_list)
#   if character == characters_to_be_replaced[i]:


# --Long-long Vowels



# --Caesar Cypher


# ----------LIST EXCERCISES

number_list = [1,2,-7,3,5,-2,2,8,15]

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
our_matrix1 = [[2,-2],[5,3]]
our_matrix2 = [[1,0],[5,6]]
our_matrix3 = [[0,0],[0,0]]
for i in range(len(our_matrix1)):
  for i2 in range(len(our_matrix1[0])):
    our_matrix3[i][i2] = our_matrix1[i][i2] + our_matrix2[i][i2]
for r in our_matrix3:
  print(r)

# --De-dup


# --BONUS--Matrix Multiplication


# ----------LOOOP EXCERCISES
