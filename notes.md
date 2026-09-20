**START**

*17-09-26: Decided on making a temperature-based alarm system; researching industrial temperature ranges, generally, temperatures for PLCs, sensors, and other standard electrical components seem to be in this approximate range: -40°C < temp < 85°C.

Using the 'traffic light' warning system to assign thresholds:

🟢 Normal: 0°C <= temp <= 55°C

🟡 Warning: Low: -20°C <= temp <= 0°; High: 55°C <= temp <= 70°C

🔴 Critical: Low: temp < -20°C; High: temp > 55°C

Then I created a flow chart to pin down the logic for an alarm that checks a single temperature input so I could start writing the code.

<img width="544" height="897" alt="0" src="https://github.com/user-attachments/assets/72926825-3ec2-4633-b6d2-88d031e0d08d" />

The resulting alarm code using `if/elif/else` logic for the temperature thresholds is in my [single_temp_alarm.py](https://github.com/alissamaharaj/alarmist-sim/blob/main/foundations/single_temp_alarm.py) file. This will be the foundational code to build upon.

```python
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
```

<img width="656" height="291" alt="Screenshot 2026-09-17 181414" src="https://github.com/user-attachments/assets/a2b903b4-ba6f-4aa6-b471-30b256afe808" />

*18-09-26: I want to modify the code so that it simulates a 24-hour period of monitoring with a value recorded every hour, so I'd need to have temperature data for 24 instances. From what I've learnt so far, to do this I'd have to generate values manually and list them, but I really didn't want to do that; I wanted the values to be randomized. I looked online to teach myself how to do this, and it seems fairly simple, so I hope I can make it work.

Before doing that, I modified the code to define the base alarm thresholds as the `temp_alarm()` function and used manually generated temperature values in a definite iterating `for` loop to work for multiple values. This updated code is in my [multi_temp_alarm.py](https://github.com/alissamaharaj/alarmist-sim/blob/main/foundations/multi_temp_alarm.py) file.

```python
time = 0
print("STARTING TEMPERATURE ALARM")
#temp = input("Temperature value:")
for temp in [-44, 93, -22, -15, 7, 58, 20, 12, -24, 89, -28, -42, -43, -27, 5, 9, 79, -44, 0, 89, 57, 6, 64, 100]:
    time = time + 1
    print("Time:", time, "Temperature:", temp)
    temp_alarm(temp)
```

<img width="278" height="540" alt="Screenshot 2026-09-18 132909" src="https://github.com/user-attachments/assets/c467ec40-1595-437c-81bf-84dc1398800a" />
<img width="278" height="260" alt="Screenshot 2026-09-18 132919" src="https://github.com/user-attachments/assets/c5b083da-7285-408c-be51-2896d1d415a7" />

After I got that working, I implemented the `random.uniform()` function to generate the values for me. It took some research to figure out how to constrain it to 24 values, and it was a bit tricky for me to understand. I needed to introduce another `for` statement into the line and use that to define the range: `for _ in range().` Regardless, it did work.
This code is in my [random_temp_alarm.py](https://github.com/alissamaharaj/alarmist-sim/blob/main/foundations/random_temp_alarm.py) file.

```python
time = 0
print("STARTING TEMPERATURE ALARM")
for temp in [random.uniform(-50, 100) for _ in range(24)]:
    time = time + 1
    print("Time:", time, "Temperature:", temp)
    temp_alarm(temp)
print("ENDING TEMPERATURE ALARM")
```

<img width="332" height="540" alt="Screenshot 2026-09-18 133053" src="https://github.com/user-attachments/assets/2304b9df-c9ec-4188-a7c2-a7678c449cb4" />
<img width="335" height="275" alt="Screenshot 2026-09-18 133101" src="https://github.com/user-attachments/assets/f5830b37-bf04-40e4-8520-9d08538d325e" />

Next, I modified the code again to introduce a secondary `while` loop that, if a temperature value falls in the critical range, stops the alarm function and prompts the user to indicate if maintenance was performed on the system to rectify the critical temperature, using nested `if/elif/else` logic once again for the prompts. `if` maintenance was performed, then the loop would `break`; `elif` maintenance was not performed, the loop would `continue`.
I included this mostly because I thought the exercise would be more fun with another level, which was true; I enjoyed this part most because I wasn't sure it would work the way I wanted, so it was very satisfying when it did. This formed my [maint_temp_alarm.py](https://github.com/alissamaharaj/alarmist-sim/blob/main/foundations/maint_temp_alarm.py) file.

```python
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
```

<img width="479" height="540" alt="Screenshot 2026-09-18 132203" src="https://github.com/user-attachments/assets/4548ff3c-1084-4f23-9601-edb9a5bb8536" />
<img width="335" height="540" alt="Screenshot 2026-09-18 132217" src="https://github.com/user-attachments/assets/f9b78a45-1747-4034-a3eb-5945e4685fc1" />
<img width="343" height="359" alt="Screenshot 2026-09-18 132226" src="https://github.com/user-attachments/assets/a6205edf-a220-45a5-ae4a-9d03838baa7c" />

Finally, I thought the project was ready to be finalized, but there were a couple of things bothering me: the temperature values did not look very clean, as they had very long decimal places; because of the range, it was triggering the critical alarm too many times for the 24-hour period; and lastly, after prompting for maintenance checks, it wasn't retesting the value.

Dealing with the decimal places first, I also did not know how to fix this yet, so I did one more online search to find the right prompts. It turned out to be a very simple fix: introducing the `round()` function for the existing random value generating function and specifying the number of decimal places, which I then implemented.

```python
for temp in [round(random.uniform(-35, 85) ,2) for _ in range(24)]:
```

Next, I restricted the range slightly so it would still trigger values for all alarm stages, but without triggering 'CRITICAL' so often.

Then came the most difficult part of the entire project, the retest loop. This really challenged my understanding of loops altogether. Trying to implement the retest loop, I ran into the issue of getting stuck in the maintenance confirmation prompt. The problem was that I tried to introduce a new `while` loop within the previous loop for retesting and was getting trapped in it.

<img width="480" height="640" alt="0" src="https://github.com/user-attachments/assets/125f1c45-d53c-4149-8db2-01ceebd066dc" />
This is the broken code that kept getting stuck in the loop.

<img width="640" height="592" alt="0" src="https://github.com/user-attachments/assets/fd37765b-d590-421b-8885-30a6bb913c64" />
This is the output of that code.

(Apologies for these images not being the best; I did not screenshot them; these are what I have available.)

It took a while to realize I didn't need another loop there; I only needed it to generate one new value for the retest and then continue the same maintenance prompt loop it was already in, not introduce a new one. The additional loop was redundant, and I was very glad to be able to get rid of it.

After these changes, I was able to write the final program file and run it: [alarmist-sim.py](https://github.com/alissamaharaj/alarmist-sim/blob/main/alarmist-sim.py), my first-ever Python project.

```python
while True:
            cond = input("Was maintenance performed? (Yes/No): ")
            if cond == "Yes":
                print("Maintenance performed.")
                temp = round(random.uniform(-35, 85) ,2)
                temp_alarm(temp)
                print(temp,"Temperature after maintenance.")
                if temp < -20 or temp > 70:
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
```

<img width="506" height="540" alt="Screenshot 2026-09-18 174311" src="https://github.com/user-attachments/assets/229dd69d-e27c-43f6-968b-aba97721d2e8" />
<img width="322" height="540" alt="Screenshot 2026-09-18 174326" src="https://github.com/user-attachments/assets/d6a02258-a409-4484-a573-9d493dbaa2e6" />
<img width="353" height="540" alt="Screenshot 2026-09-18 174333" src="https://github.com/user-attachments/assets/b42a8709-c2e9-41e3-abbf-b082c8c54730" />

This was a very proud moment for me, finishing my first-ever project from scratch. I've never had the opportunity before to realize how much I enjoy the design process; this was an eye-opening experience. I feel that this really sets me on good ground for the rest of my self-study journey, as I'm more enthusiastic than ever to continue learning and reaching various milestones where I get to revisit the design process and build more projects.

**FINISH**

---

**START RUNNING REPORT EXTENSION**

*20/09/26: The first (and so far only planned) project extension. TO introduce a running report to the output. The plan is to introduce 3 new elements: a count of the Normal, Warning, and Critical hours; a count of the maintenance events triggered; and the highest deviation alert achieved for the 24-hour period.

Starting with the alarm state counters. I would have to implement 3 individual counters for each alarm state. Right now the program only prints the alarm states; it doesn't return a value that can be used to count.
