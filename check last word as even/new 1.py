import time

def last_early():
    my_string = input("Enter two words: ")
    last_letter = my_string[-1]
    another_words = my_string[:-1]
    if last_letter in another_words:
        return True
    else:
        return False




print(last_early())
time.sleep(3)