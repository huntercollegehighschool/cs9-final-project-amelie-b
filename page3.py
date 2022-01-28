#Use of this page is optional. If you use code here, make sure either import page3 or from page3 import * appear on your main.py page.

list_6 = ["s", "a", "e", "s", "p", "r"]

print(list_6)

list_6_ans = ["PASSER", "PARSES", "REPASS", "SPARES", "SPARSE", "SPEARS"]

total = 0

trial_3 = input("What 6-letter words can you think of that contain these 6 letters? Enter them one by one! Remember: enter your words in ALL CAPS. You may not enter a word twice. What is your first word? Enter return if you wish to return to the title page:  ")

while total < 6:
  if (trial_3 == "PASSER") and (trial_3 in list_6_ans):
    print("Nice!")
    list_6_ans.remove("PASSER")
    total = total + 1
    trial_3 = input("What other 6-letter word can you think of that contain these 6 letters? If you have entered 6 uniwue correct answers, enter a random letter or number: ")
  elif (trial_3 == "PARSES") and (trial_3 in list_6_ans):
    print("Great!")
    list_6_ans.remove("PARSES")
    total = total + 1
    trial_3 = input("What other 6-letter word can you think of that contain these 6 letters? If you have entered 6 uniwue correct answers, enter a random letter or number: ")
  elif (trial_3 == "REPASS") and (trial_3 in list_6_ans):
    print("Good!")
    list_6_ans.remove("REPASS")
    total = total + 1
    trial_3 = input("What other 6-letter word can you think of that contain these 6 letters? If you have entered 6 uniwue correct answers, enter a random letter or number: ")
  elif (trial_3 == "SPARES") and (trial_3 in list_6_ans):
    print("Terrific!")
    list_6_ans.remove("SPARES")
    total = total + 1
    trial_3 = input("What other 6-letter word can you think of that contain these 6 letters? If you have entered 6 uniwue correct answers, enter a random letter or number: ")
  elif (trial_3 == "SPARSE") and (trial_3 in list_6_ans):
    print("Good job!")
    list_6_ans.remove("SPARSE")
    total = total + 1
    trial_3 = input("What other 6-letter word can you think of that contain these 6 letters? If you have entered 6 uniwue correct answers, enter a random letter or number: ")
   elif (trial_3 == "SPEARS") and (trial_3 in list_6_ans):
    print("Good job!")
    list_6_ans.remove("SPEARS")
    total = total + 1
    trial_3 = input("What other 6-letter word can you think of that contain these 6 letters? If you have entered 6 uniwue correct answers, enter a random letter or number: ")
  elif trial_3 == "RETURN":
    in_number = input("Welcome to the Anagram Aneurysm: The game not guaranteed to give you a headache. Please enter 4, 5, 6, or 7 for the number of letters you wish to try solving: ")
    if in_number == "4":
      import page1
    elif in_number == "5":
      import page2
    elif in_number == "6":
      import page3
    elif in_number == "7":
      import page4
    else:
      in_number = input("Sorry; your input is invalid. Please enter 4, 5, 6, or 7 for the number of letters you wish to have")
  else:
    print("Uh-oh! It looks like that word isn't on the list! Would you like to try again or return?")
    trial_3 = input("Enter another word to try again and enter return to return: ")

print("Congratulations! You finished this puzzle!")

in_number = input("Please enter 4, 5, or 7 for the number of letters you wish to try solving: ")

if in_number == "4":
  import page1
elif in_number == "5":
  import page2
elif in_number == "6":
  import page3
elif in_number == "7":
  import page4
else:
  in_number = input("Sorry; your input is invalid. Please enter 4, 5, 6, or 7 for the number of letters you wish to have")