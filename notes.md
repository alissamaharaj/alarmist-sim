**START**

*17-09-26: Decided on making a temperature-based alarm system; researching industrial temperature ranges, generally, temperatures for PLCs, sensors, and other standard electrical components seem to be in this approximate range: -40°C < temp > 85°C.

Using the 'traffic light' warning system to assign thresholds:

🟢 Normal: 0°C <= temp <= 55°C

🟡 Warning: Low: -20°C <= temp <= 0°; High: 55°C <= temp <= 70°C

🔴 Critical: Low: temp < -20°C; High: temp > 55°C

Then I created a flow chart to pin down the logic for an alarm that checks a single temperature input so I could start writing the code.
<img width="544" height="897" alt="0" src="https://github.com/user-attachments/assets/72926825-3ec2-4633-b6d2-88d031e0d08d" />


