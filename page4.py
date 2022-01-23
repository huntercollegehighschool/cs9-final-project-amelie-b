#Use of this page is optional. If you use code here, make sure either import page4 or from page4 import * appear on your main.py page.

list_6 = ["a", "a", "g", "m", "n", "r"]

print(list_6)

list_6_ans = ["ANAGRAM"]

total = 0

trial_4 = input("What 6-letter words can you think of that contain these 5 letters? Enter them one by one! Remember: enter your words in ALL CAPS. You may not enter a word twice. What is your first word? Enter return if you wish to return to the title page:  ")

while total < 1:
  if (trial_4 == "ANAGRAM") and (trial_4 in list_6_ans):
    print("Nice!")
    list_6_ans.remove("LEAPT")
    total = total + 1
    trial_4 = input("Congratulations! You've finished this puzzle! Enter a random letter or number to indicate that you wish to try another puzzle: ")
  elif trial_4 == "RETURN":
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

in_number = input("Please enter 4, 5, or 6 for the number of letters you wish to try solving: ")

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