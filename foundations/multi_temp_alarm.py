#import random
def temp_alarm(temp):
    try:
        temp = float(temp)
    except ValueError:
        print("Invalid temperature input")
        quit()
    if 0 <= temp <= 55 :
        print("-Normal-")
    elif -20 <= temp <= 0 or 55 <= temp <= 70 :
        print("~Warning~")
    else:
        print("!!CRITICAL!!") 

time = 0
print("STARTING TEMPERATURE ALARM")
#temp = input("Temperature value:")
for temp in [-44, 93, -22, -15, 7, 58, 20, 12, -24, 89, -28, -42, -43, -27, 5, 9, 79, -44, 0, 89, 57, 6, 64, 100]:
    time = time + 1
    print("Time:", time, "Temperature:", temp)
    temp_alarm(temp)
    