phonebook_data = [
    {
        "name": "Melissa",
        "number": "404-235-5428"
    },
    {
        "name": "Joe",
        "number": "404-235-2125"
    },
    {
        "name": "Mike",
        "number": "770-134-2229"
    },
    {
        "name": "Igor",
        "number": "770-233-3461"
    }
]

main_menu_choice = raw_input("Electronic Phone Book \n"
" ===================== \n"
"1. Look up an entry\n"
"2. Set an entry\n"
"3. Delete an entry\n"
"4. List all entries\n"
"5. Search for an entry\n"
"6. Quit\n"
"What do you want to do (1-6)?\n ")

def main_menu():
  raw_input("Electronic Phone Book \n"
" ===================== \n"
"1. Look up an entry\n"
"2. Set an entry\n"
"3. Delete an entry\n"
"4. List all entries\n"
"5. Search for an entry\n"
"6. Quit\n"
"What do you want to do (1-5)?\n ")

# ------Main Menu Choice 1------
if (main_menu_choice == "1"):
  who_to_find = raw_input("Who would you like to look up? ")
  for i in phonebook_data:
    if (i["name"] == who_to_find):
      print ("Entry found for %s: " % (who_to_find) + i["number"])
      main_menu()
    # else:
    #   print ("That person is not in the phonebook")

# ------Main Menu Choice 2------
elif (main_menu_choice == "2"):
  name_to_enter = raw_input("Please enter the name: ")
  number_to_enter = raw_input("Please enter their number: ")
  phonebook_data.append({"name": name_to_enter, "number": number_to_enter})
  main_menu()

# ------Main Menu Choice 3------
elif (main_menu_choice == "3"):
  who_to_delete = raw_input("Who should be removed from the phonebook? ")
  for i in phonebook_data:
    if (i["name"] == who_to_delete):
      phonebook_data.remove(i)
      print ("They have been removed from our records.")

# ------Main Menu Choice 4------
elif (main_menu_choice == "4"):
  for i in phonebook_data:
    print ("Entry found for %s: %s" % (i["name"], i["number"]))

# ------Main Menu Choice 5------
# elif (main_menu_choice =="5"):

# ------Main Menu Choice 6------
elif (main_menu_choice =="6"):
  print ("good bye")

# ------Non-existent Main Menu Choices------
# else:
#   print ("I'm sorry, that's not a valid option. Try again! ")
#   main_menu()
