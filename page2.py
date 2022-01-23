#Use of this page is optional. If you use code here, make sure either import page2 or from page2 import * appear on your main.py page.

list_5 = ["l", "a", "e", "t", "p"]

print(list_5)

list_5_ans = ["LEAPT", "PETAL", "PLATE", "PLEAT", "TEPAL"]

total = 0

trial_2 = input("What 5-letter words can you think of that contain these 5 letters? Enter them one by one! Remember: enter your words in ALL CAPS. You may not enter a word twice. What is your first word? Enter return if you wish to return to the title page:  ")

while total < 5:
  if (trial_2 == "LEAPT") and (trial_2 in list_5_ans):
    print("Nice!")
    list_5_ans.remove("LEAPT")
    total = total + 1
    trial_2 = input("What other 5-letter word can you think of that contain these 5 letters? If you have entered 5 uniwue correct answers, enter a random letter or number: ")
  elif (trial_2 == "PETAL") and (trial_2 in list_5_ans):
    print("Great!")
    list_5_ans.remove("PETAL")
    total = total + 1
    trial_2 = input("What other 5-letter word can you think of that contain these 5 letters? If you have entered 5 uniwue correct answers, enter a random letter or number: ")
  elif (trial_2 == "PLATE") and (trial_2 in list_5_ans):
    print("Good!")
    list_5_ans.remove("PLATE")
    total = total + 1
    trial_2 = input("What other 5-letter word can you think of that contain these 5 letters? If you have entered 5 uniwue correct answers, enter a random letter or number: ")
  elif (trial_2 == "PLEAT") and (trial_2 in list_5_ans):
    print("Terrific!")
    list_5_ans.remove("PLEAT")
    total = total + 1
    trial_2 = input("What other 5-letter word can you think of that contain these 5 letters? If you have entered 5 uniwue correct answers, enter a random letter or number: ")
  elif (trial_2 == "TEPAL") and (trial_2 in list_5_ans):
    print("Good job!")
    list_5_ans.remove("TEPAL")
    total = total + 1
    trial_2 = input("What other 5-letter word can you think of that contain these 5 letters? If you have entered 5 uniwue correct answers, enter a random letter or number: ")
  elif trial_2 == "RETURN":
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
    trial_2 = input("Enter another word to try again and enter return to return: ")

print("Congratulations! You finished this puzzle!")

in_number = input("Please enter 4, 6, or 7 for the number of letters you wish to try solving: ")

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