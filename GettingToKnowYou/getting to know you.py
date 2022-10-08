#This program will get to know the user 
from fileinput import close

bot_name = "John"

print("Hi!, my name is", bot_name, "and I'm exicted to meet you today!")
print("I would like to ask a few question about you to get to know you better!")

print("Let's start with you name, can you tell me please your first name?")
f_name = input("")
print("Well hello", f_name.title(), "I'm happy to finally meet you!")

print(" do you think you can tell me your last name as well?")
l_name = input("")
print("Thank you", f_name.title(), l_name.title(), "I'm glad we getting to know each other!")

print("How old are you?")
age = float(input(""))

print("Please tell me, do you have a job?, Enter only yes or no")

job = input("")
if job.lower() == "yes":  
    print("Thank you for your answer!")  
elif job.lower()=="no":  
    print("Thank you for your answer!")  
else:  
    print("you enterd invalid answer, try again.")
    exit()

print("can you plaese tell me for how many years you work in this indstury?")
print("please write down with numbers only")
years_Job = float(input(""))
if years_Job >= age:
    print("You enterd a bigger number of years then your own age, don't lie")
else:
    print("Thank you", f_name.title(), l_name.title(), "for the answer")

print("I'm goign to ask you for what youd liked most from the list, please enter the correct number that apply to you.")
print("1. Pasta, 2. Rice, 3. Pizza, 4. Hambuger, 5. Noodles")
fav_food = int(input(""))
if fav_food == 1:  
    print("yeah! pasta is the best!")  
elif fav_food == 2:  
    print("rice is for sure good with every dinner!")  
elif fav_food == 3:  
    print("there is nothing better then pizza and movie!")  
elif fav_food == 4:  
    print("you like hamburgers, me too!")
elif fav_food == 4:  
    print("there is nothing like noodles right?") 
else:  
    print("you enterd invalid answer, try again.")
    exit()