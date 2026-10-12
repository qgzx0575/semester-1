# Week 1.3, Session 1: Task 1b

fruit = ['apple','pear','banana','orange']

# loop through the list
while fruit:
	print(fruit.pop())

# fruit.pop() returns orange, banana, pear, and then finally apple, just like a stack. 
# It doesn't loop because "while fruit" returns false once the stack is empty.
# Because pop() returns the last item in the stack, removing itself once popped
