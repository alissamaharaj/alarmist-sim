import random

def temp_alarm(temp):
    try:
        temp = float(temp)
    except ValueError:
        print("Invalid temperature input")
        quit()
    if 0 <= temp <= 55 :
        print("-Normal-")
        return "Normal"
    elif -20 <= temp <= 0 or 55 <= temp <= 70 :
        print("~Warning~")
        return "Warning"
    else:
        print("!!Critical!!")
        return "Critical"

time = 0
normal_count = 0
warning_count = 0
critical_count = 0
maint_count = 0
highest_dev = None
print("STARTING TEMPERATURE ALARM")
for temp in [round(random.uniform(-35, 85) ,2) for _ in range(24)]:
    time = time + 1
    print("Time:", time, "Temperature:", temp)
    alarm_state = temp_alarm(temp)
    if alarm_state == "Normal":
        normal_count = normal_count + 1
    elif alarm_state == "Warning":
        warning_count = warning_count + 1
    elif alarm_state == "Critical":
        critical_count = critical_count + 1

    if temp < -20 or temp > 70:
        if highest_dev is None or abs(temp) > abs(highest_dev):
            highest_dev = temp
        print("Temperature Critical, attention required.")
        while True:
            cond = input("Was maintenance performed? (Yes/No): ")
            if cond == "Yes":
                maint_count = maint_count + 1
                print("Maintenance performed.")
                temp = round(random.uniform(-35, 85) ,2)
                temp_alarm(temp)
                print(temp,"Temperature after maintenance.")
                if temp < -20 or temp > 70:
                    if highest_dev is None or abs(temp) > abs(highest_dev):
                        highest_dev = temp
                    print("Temperature Critical, attention required.")
                    continue
                else:
                    print("Temperature no longer critical.")
                    break   
            elif cond == "No":
                print("Maintenance not performed. Please perform maintenance.")
                continue
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")
    
print("ENDING TEMPERATURE ALARM")
print("Normal hours:", normal_count, "; Warning hours:", warning_count, "; Critical hours:", critical_count)
print("Maintenance performed:", maint_count, "times.")
print("Most extreme Critical temperature recorded:", highest_dev)
