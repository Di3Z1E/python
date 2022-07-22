import time

def distance(num1, num2, num3):
    if (((num2 - num1) == 1) or ((num3 - num1) == 1)) and (((num3 - num1 >= 2) and (num3 - num2 >= 2)) or ((num2 - num1 >= 2) and (num2 - num2 >= 2))):
        return True
    else:
        return False

input = ('Enter 3 numbers: ', distance)
print = (distance)
time.sleep(3)