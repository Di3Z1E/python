import time
temp_to_convert = input("Insert the temperature you would like to convert: ").upper()
if temp_to_convert.endswith("F"):
    converted_temp = temp_to_convert.replace("F","")
    converted_temp = (float(converted_temp) * 5 - 160)/9
    print( str(converted_temp) + "C")

elif temp_to_convert.endswith("C"):
    converted_temp = temp_to_convert.replace("C","")
    converted_temp = (float(converted_temp) * 9 + 160)/5
    print(str(converted_temp) + "F")
	
time.sleep(3)