temp = input("Temperature value:")
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
