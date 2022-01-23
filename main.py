"""
Name(s): Amelie Bi
Name of Project: Anagram Aneurysm
"""

#Write the main part of your program here. Use of the other pages is optional.

in_number = input("Welcome to the Anagram Aneurysm: The game NOT guaranteed to give you a headache. Please enter 4, 5, 6, or 7 for the number of letters you wish to try solving: ")

if in_number == "4":
  import page1
elif in_number == "5":
  import page2
elif in_number == "6":
  import page3
elif in_number == "7":
  import page4
else:
  in_number = input("Sorry; your input is invalid. Please enter 4, 5, 6, or 7 for the number of letters you wish to try: ")
#import page5  # uncomment if you're using page5