**START**

*17-09-26: Decided on making a temperature-based alarm system; researching industrial temperature ranges, generally, temperatures for PLCs, sensors, and other standard electrical components seem to be in this approximate range: -40°C < temp > 85°C.

Using the 'traffic light' warning system to assign thresholds:

🟢 Normal: 0°C <= temp <= 55°C

🟡 Warning: Low: -20°C <= temp <= 0°; High: 55°C <= temp <= 70°C

🔴 Critical: Low: temp < -20°C; High: temp > 55°C

Then I created a flow chart to pin down the logic for an alarm that checks a single temperature input so I could start writing the code.

<img width="544" height="897" alt="0" src="https://github.com/user-attachments/assets/72926825-3ec2-4633-b6d2-88d031e0d08d" />

The resulting alarm code is in my single_temp_alarm.py file. This will be the foundational code to build upon.

<img width="656" height="291" alt="Screenshot 2026-09-17 181414" src="https://github.com/user-attachments/assets/a2b903b4-ba6f-4aa6-b471-30b256afe808" />

*18-09-26: I want to modify the code so that it simulates a 24-hour period of monitoring with a value recorded every hour so I'd need to have temperature data for 24 instances. From what I've learnt so far, to do this I'd have to generate values manually and list them, but I really didn't want to do that; I wanted the values to be randomized. I looked online to teach myself how to do this and it seems fairly simple, so I hope I can make it work.

Before doing that, I modified the code and used manually generated temperature values to work for multiple temperature values in a loop. This updated code is in my multi_temp_alarm.py file.

<img width="278" height="540" alt="Screenshot 2026-09-18 132909" src="https://github.com/user-attachments/assets/c467ec40-1595-437c-81bf-84dc1398800a" />
<img width="278" height="260" alt="Screenshot 2026-09-18 132919" src="https://github.com/user-attachments/assets/c5b083da-7285-408c-be51-2896d1d415a7" />

After I got that working, I implemented the 'random' function to generate the values for me. It took some research to figure out how to constrain it to 24 values, and it was a bit tricky for me to understand. Regardless, it did work.
This code is in my random_temp_alarm.py file.

<img width="335" height="275" alt="Screenshot 2026-09-18 133101" src="https://github.com/user-attachments/assets/f5830b37-bf04-40e4-8520-9d08538d325e" />
<img width="332" height="540" alt="Screenshot 2026-09-18 133053" src="https://github.com/user-attachments/assets/2304b9df-c9ec-4188-a7c2-a7678c449cb4" />

Next, I modified the code again to introduce a secondary loop that, if a temperature value falls in the critical range, stops the alarm function and prompts the user to indicate maintenance performed on the system to rectify the critical temperature. I included this mostly because I thought the exercise would be more fun with another level, which was true; I enjoyed this part most because I wasn't sure it would work the way I wanted, so it was very satisfying when it did. This formed my maint_temp_alarm.py file.

<img width="479" height="540" alt="Screenshot 2026-09-18 132203" src="https://github.com/user-attachments/assets/4548ff3c-1084-4f23-9601-edb9a5bb8536" />
<img width="335" height="540" alt="Screenshot 2026-09-18 132217" src="https://github.com/user-attachments/assets/f9b78a45-1747-4034-a3eb-5945e4685fc1" />
<img width="343" height="359" alt="Screenshot 2026-09-18 132226" src="https://github.com/user-attachments/assets/a6205edf-a220-45a5-ae4a-9d03838baa7c" />

Finally, I thought the project was ready to be finalized, but there was one thing bothering me: the temperature values did not look very clean, as they had very long decimal places. I also did not know how to fix this yet, so I did one more online search to find the right prompts. It turned out to be a very simple fix, which I then implemented, and I was able to write the final program file and run it: alarmist-sim.py, my first-ever Python project.

<img width="392" height="540" alt="Screenshot 2026-09-18 134042" src="https://github.com/user-attachments/assets/bfad3791-88c5-4980-bf65-6bfff0a3dbf5" />
<img width="336" height="540" alt="Screenshot 2026-09-18 134058" src="https://github.com/user-attachments/assets/c0648ff8-43bc-432b-9d1b-416e17115a0a" />
<img width="369" height="317" alt="Screenshot 2026-09-18 134104" src="https://github.com/user-attachments/assets/f9fea821-014b-4558-b45c-d41640470769" />
