# Task 6

Your objective is to simulate a factory machine monitoring system using
sensor data. You will implement a program that uses user inputs to monitor
the status of a machine. Based on the inputs, your program should evaluate
the conditions and print instructions to the user.

## Instructions

### Step 1: Get User Inputs

You need to collect three inputs from the user:

1. The machine's temperature in degrees Celsius (integer)
2. The machine's pressure in PSI (integer)
3. The machine's operational status (1 for operating, 0 for stopped) (integer)

### Step 2: Evaluate Operating Conditions

Use conditional statements involving `if`, `elif` and `else` to evaluate
the operating temperature and pressure of the machine.

#### Temperature

- If the temperature is above 80°C, alert that the temperature is too high
  and recommend shutting down the machine.

- If the temperature is between 50°C and 80°C, indicate that the temperature
  is within safe limits.

- If the temperature is below 50°C, indicate that the machine temperature
  is low and no action is needed.

#### Pressure

- If the pressure exceeds 100 PSI, alert that high pressure is detected
  and recommend maintenance.

- If the pressure is between 70 PSI and 100 PSI, indicate that the
  pressure is stable.

- If the pressure is below 70 PSI, indicate that the pressure is low and the
  system is operating normally.

### Step 3: Determine Status

If the machine is currently operating, then if either temperature is too
high or pressure is too high, alert that the machine is running in unsafe
conditions and recommend shutting it down.

If everything is normal, indicate that the machine is running normally.

If the machine is not currently operating, indicate that it is stopped and
no immediate action is needed.

## Testing

After completing your program, test it with different inputs to ensure it
behaves correctly based on the conditions you implemented.

## Extension Activity

As an extension to the basic program, try logging the results to a file.
(Note that this requires knowledge of topics that we haven't yet covered!)

You should use `machine_log.txt` as the name of the log file. This file should
have the following information written to it:

- The current temperature, pressure, and operational status
- The actions taken based on the evaluations

Ensure that each entry in the log file is timestamped to track when the
evaluation occurred.
