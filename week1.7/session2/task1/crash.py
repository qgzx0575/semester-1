# Week 1.7, Session 2: Task 1 - IndexError

# Run this program and observe what happens

def assign_values(x):
    for i in range(100):
        x[i] = (i + 1) * (i + 1);

if __name__ == "__main__":
    data = [0] * 10
    assign_values(data)
    print("Done!")