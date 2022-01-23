#Use of this page is optional. If you use code here, make sure either import page1 or from page1 import * appear on your main.py page.

list_4 = ["o", "p", "s", "t"]

print(list_4)

list_4_ans = ["OPTS", "POST", "POTS", "STOP", "TOPS"]

total = 0

trial_1 = input("What 4-letter words can you think of that contain these 4 letters? Enter them one by one! Remember: enter your words in ALL CAPS. You may not enter a word twice. What is your first word? Enter return if you wish to return to the title page:  ")

while total < 4:
  if (trial_1 == "OPTS") and (trial_1 in list_4_ans):
    print("Nice!")
    list_4_ans.remove("OPTS")
    total = total + 1
    trial_1 = input("What other 4-letter word can you think of that contain these 4 letters? If you have entered 5 uniwue correct answers, enter a random letter or number: ")
  elif (trial_1 == "POST") and (trial_1 in list_4_ans):
    print("Great!")
    list_4_ans.remove("POST")
    total = total + 1
    trial_1 = input("What other 4-letter word can you think of that contain these 4 letters? If you have entered 5 uniwue correct answers, enter a random letter or number: ")
  elif (trial_1 == "POTS") and (trial_1 in list_4_ans):
    print("Good!")
    list_4_ans.remove("POTS")
    total = total + 1
    trial_1 = input("What other 4-letter word can you think of that contain these 4 letters? If you have entered 5 uniwue correct answers, enter a random letter or number: ")
  elif (trial_1 == "STOP") and (trial_1 in list_4_ans):
    print("Terrific!")
    list_4_ans.remove("STOP")
    total = total + 1
    trial_1 = input("What other 4-letter word can you think of that contain these 4 letters? If you have entered 5 uniwue correct answers, enter a random letter or number: ")
  elif (trial_1 == "TOPS") and (trial_1 in list_4_ans):
    print("Good job!")
    list_4_ans.remove("TOPS")
    total = total + 1
    trial_1 = input("What other 4-letter word can you think of that contain these 4 letters? If you have entered 5 uniwue correct answers, enter a random letter or number: ")
  elif trial_1 == "RETURN":
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
    trial_1 = input("Enter another word to try again and enter return to return: ")

print("Congratulations! You finished this puzzle!")

in_number = input("Please enter 5, 6, or 7 for the number of letters you wish to try solving: ")

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