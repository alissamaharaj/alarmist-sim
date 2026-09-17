**START**

*17-09-26: Decided on making a temperature-based alarm system; researching industrial temperature ranges, generally, temperatures for PLCs, sensors, and other standard electrical components seems to be in this approximate range: -40°C < temp > 185°C.

Using the 'traffic light' warning system to assign thresholds:

🟢 Normal: 0°C <= temp <= 55°C

🟡 Warning: Low: -20°C <= temp <= 0°; High: 55°C <= temp <= 70°C

🔴 Critical: Low: temp < -20°C; High: temp > 55°C

