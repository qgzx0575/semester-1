# Week 1.2, Session 2: Task 6

machine_temp = int(input("Enter the machine's temperature: "))
machine_psi = int(input("Enter the machine's pressure: "))
machine_status = int(input("Is the machine operational? (1 for yes, 0 for no): "))

if machine_status == 1:
    if machine_temp < 50:
        print("The machine's temperature is currently low, no action is needed.")
    elif 50 <= machine_temp <= 80:
        print("The machine's temperaure is currently within safe limits.") 
    else:
        print("The machine's temperature is currently high, you must shut down the machine.")

    if machine_psi < 70:
        print("The machine's pressure is currently low, no action is needed.")
    elif 70 <= machine_psi <= 100:
        print("The machine's pressure is currently within safe limits.") 
    else:
        print("The machine's pressure is currently high, you must shut down the machine.")

    if 50 <= machine_temp <= 80 and 70 <= machine_psi <= 100:
        print("Everything is normal, the machine is running just fine.")
    else:
        print("The machine must be shutdown for everyone's safety.")
else:
    print("The machine has been shut down, no immediate action is needed.")