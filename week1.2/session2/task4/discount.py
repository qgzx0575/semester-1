# Week 1.2, Session 2: Task 4

# A till system needs to offer a range of discounts:
# if the user is a member of the subscription service, they get 25% off
# if they are a student and a member, 30% off
# if they are just a student, 15% off
# if none of the above, they don't get a discount

# Look at the discounts in the final_cost calculation to match these up,
# and think about WHY they are in this order!

cost = int(input("Amount spent: "))
is_member = input("Are you a member? (y/n): ").lower()
is_student = input("Are you a student? (y/n): ").lower()

if XXX:
    final_cost = cost * 0.7
elif XXX:
    final_cost = cost * 0.75
elif XXX:
    final_cost = cost * 0.85
else:
    final_cost = cost

print(f"Final amount including discount: {final_cost}")
