import random

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
    return temp    

time = 0
print("STARTING TEMPERATURE ALARM")
for temp in [round(random.uniform(-50, 100) ,2) for _ in range(24)]:
    time = time + 1
    print("Time:", time, "Temperature:", temp)
    temp_alarm(temp)
    if temp < -20 or temp > 70:
        print("Temperature Critical, attention required.")
        while True:
            cond = input("Was maintenance performed? (Yes/No): ")
            if cond == "Yes":
                print("Maintenance performed.")
                break
            elif cond == "No":
                print("Maintenance not performed. Please perform maintenance.")
                continue
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")
    
print("ENDING TEMPERATURE ALARM")
    