## alarmist-sim: Alarm & Safety Logic Simulator 🚨

"alarmist-sim" is a temperature alarm and safety-response simulator, built to model the core decision logic behind industrial safety systems: continuous monitoring, threshold-based alerting, and mandatory operator response before a process can return to normal. Built as Python Project 1 of my self-study track in control systems and industrial data engineering (following Python for Everybody, Ch. 1–5).

---

### What it Does

The simulator generates random temperature readings for a 24-hour period and evaluates each one against defined safety thresholds. Depending on which threshold range the value falls in, it reports an alarm state: 'Normal', 'Warning', or 'Critical'. 

When a 'Critical' reading occurs, the simulator operation cycle is stopped and prompts the user to confirm whether necessary maintenance has been performed to ensure the temperature is back within range. Unless it is back within range, it will be re-tested and reprompted as many times as required.

### Design Rationale

The idea behind this project design is standard procedure in industrial control systems and safety condition monitoring: faults always require dedicated attention and testing. I could have just created a value checker alarm that prints an alarm state for specific thresholds, but my technical background has ingrained proper safety and fault rectification protocols in me. It only felt right to me that the system would need retesting and verification before being allowed to continue following a fault. 

For this reason, I built in the following features: The 'CRITICAL' alarm state completely halts operation. It can only resume if it confirms that an operator has dedicated attention to the fault, and it must retest and confirm the fault was rectified. If not rectified, it remains halted until it can confirm rectification.

### State Diagram

stateDiagram-v2
[*] --> Normal
Normal --> Warning: deviation from safe range
Warning --> Critical: further deviation
Normal --> Critical: severe deviation
Critical --> AwaitingMaintenance: alarm triggered
AwaitingMaintenance --> AwaitingMaintenance: "No" / invalid input
AwaitingMaintenance --> Retest: "Yes" confirmed
Retest --> AwaitingMaintenance: still critical
Retest --> Normal: resolved
Retest --> Warning: resolved
