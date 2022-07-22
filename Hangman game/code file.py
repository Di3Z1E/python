import time
import re

#Intro screen // Developed by David_Azani
HANGMAN_ASCII_ART = print(""" \n \t\tWelcome to Hangman game! \n
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
""")

#Display landing page and the amount of maximum tries.
HANGMAN_ASCII_ART
print("The maximum tries available in this game are: 6\n\n")

#Print the first question
user_choosen_letter = input("Enter a letter: ")

#Settings to show only lowercase letters
strlen = len(user_choosen_letter)
lowerCaseStr = user_choosen_letter.lower()
upperCaseStr = user_choosen_letter.lower()
user_choosen_letter = lowerCaseStr

#Hide the the text as the user enterd
user_choosen_letter = '_'*len(user_choosen_letter)
print(' _ '*len(user_choosen_letter)) 

#Keeps the screen on for 3 seconds
print("The window will close in 3 seconds")
time.sleep(1)
print("The window will close in 2 seconds")
time.sleep(1)
print("The window will close in 1 seconds")
time.sleep(1)