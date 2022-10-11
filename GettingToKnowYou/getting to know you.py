# Hi, my name is David and I'm building a python script to get to know the user.
# I will try to develop this script each time I can to make it more interactive and fun to use.
# Disclaimer: I'm not a developer, I'm more into software testing and R&D support in general.
# I'm building this script to maintain my abilities to write and understand code better each day to be more efficient at work.

#Import necessary modules for this script to work
from fileinput import close
import os

#Clear the screen from any outputs
os.system('cls')

# defined the bot name for this script
bot_name = "John"

# Greeting
print("Hi! \nmy name is", bot_name, "and I'm exicted to meet you today!")
print("I would like to ask a few questions about you to get to know you better!")

# Get the user first name and store the answer in f_name
print("\nLet's start with your name, can you tell me please your first name?")
f_name = input("")
print("\n\nWell hello", f_name.title(), "I'm happy to finally meet you!")

# Get the user last name and store the answer in l_name
print("\ndo you think you can tell me your last name as well?")
l_name = input("")
print("Thank you", f_name.title(), l_name.title(), "I'm glad we getting to know each other!")

# Get the user age and store the answer in age
print("\nHow old are you?")
age = float(input(""))
if age <= 6:
    print("you can't be that young, try to be honest")
    exit()
elif age >= 120:
    print("you can't be that old, try to be honest")
    exit()
else:
    print("")

# Get the user input and store the answer in job to understand if the user have a job
print("Please tell me, do you have a job?, \nEnter only yes or no")

job = input("")
if job.lower() == "yes":  
    print("\nThank you for your answer!")  
elif job.lower()=="no":  
    print("\nThank you for your answer!")  
else:  
    print("\nyou enterd invalid answer, try again.")
    exit()

if job == "yes":
    print("can you tell me what indstury you working at? (High-tech/Food/Delivery/etc)")
    job_indstury = input("")
elif job == "no":
    print("Would you like to tell me which indstury would you like to work? (High-tech/Food/Delivery/etc)")
    job_indstury = input("")

# In case the user answerd yes at the job question this dialog will appear
if job == "yes":
    print("\ncan you plaese tell me for how many years you work in this indstury?")
    print("please write down with numbers only")
    years_Job = float(input(""))
    if years_Job >= age:
        print("\nYou enterd a bigger number of years then your own age, don't lie")
        exit()
    elif job == "no":
        print("would you like me to suggest to you how to start?")
        job_seek = input("")
        if job_seek == "yes":
            print("I would suggest you try to open a linkedin account and start from there")
        else:
            print("Alright, i may suggest later my offer to help you with this matter")
    else:
        print("\nThank you", f_name.title(), l_name.title(), "for the answer")


# Get user most liked type of food
print("\nI'm going to ask you for what youd liked most from the list, please enter the correct number that apply to you.")
print("1. Pasta, 2. Rice, 3. Pizza, 4. Hambuger, 5. Noodles")
fav_food = int(input(""))
if fav_food == 1:  
    print("\nyeah! pasta is the best!")
    fav_food = "pasta"
elif fav_food == 2:  
    print("\nrice is for sure good with every dinner!")
    fav_food = "rice"
elif fav_food == 3:  
    print("\nthere is nothing better then pizza and movie!")  
    fav_food = "pizza"
elif fav_food == 4:  
    print("\nyou like hamburgers, me too!")
    fav_food = "hamburgers"
elif fav_food == 5:  
    print("\nthere is nothing like noodles right?")
    fav_food = "noodles"
else:  
    print("\nyou enterd invalid answer, try again.")
    exit()

if job == "yes":
    print("\nI was really happy to finally meet you", f_name, l_name, ", I also likes", fav_food, 
    """\nI can see you have some really nice amount of expeirnce at""", job_indstury,
    "you stiil young! just a", age, "years old, there is so much you can do!")
elif job == "no":
    print("\nI was really happy to finally meet you", f_name, l_name, ", I also likes", fav_food, """ \nI can see you still don't have a job,
    I would recommend to search on linkedin for a new opprtinuties for""",job_indstury, "and start your way up from there!"
    "you stiil young! just a", age, "years old, there is so much you can do!")