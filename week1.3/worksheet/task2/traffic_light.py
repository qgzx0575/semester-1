"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Jayakrishnan Jayaprasad
"""
states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

while systime in range(0, maxtime+1):
    state = list(states.keys())[0]
    print(f"Time {systime:03} State {state}")
    states.update({state: states.get(state)-1})
    if states.get(state) == 0:
        states.pop(state)
    systime += 1