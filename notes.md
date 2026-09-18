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

*18-09-26: I want to modify the code so that it simulates a 24-hour period of monitoring with a value recorded every hour so I'd need to have temperature data for 24 instances. From what I've learnt so far, to do this I'd have to generate values manually and list them, but I really didn't want to do that, I wanted the values to be randomized. I looked online to teach myself how to do this and it seems fairly simple, so I hope I can make it work.



