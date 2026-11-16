'''
This isn't an activity, just an example of the more advanced things you can do with a combination of libraries!

Mapping a time comparison between Euclidean algorithm vs. Stein for calculating the GCD
Feel free to have a play around with this, and look at different cases/pairs/much larger numbers.

You could also plot different things - for example, pairs could be plotted on a scatter.
'''

import pandas as pd
import matplotlib.pyplot as plt
import random
import time

# Function to compute GCD using Euclidean algorithm
def gcd_euclidean(a, b):
    while b:
        a, b = b, a % b
    return a

# Stein's binary algorithm for GCD
def gcd_stein(a, b):
    if a == b:
        return a
    elif a == 0:
        return b
    elif b == 0:
        return a
    if a % 2 == 0:
        if b % 2 == 0:
            return 2 * gcd_stein(a // 2, b // 2)
        else:
            return gcd_stein(a // 2, b)
    elif b % 2 == 0:
        return gcd_stein(a, b // 2)
    elif a > b:
        return gcd_stein((a - b) // 2, b)
    else:
        return gcd_stein(a, (b - a) // 2)

# Generate random number pairs
num_pairs = 50
data = {'Number 1': [random.randint(1, 1000) for _ in range(num_pairs)],
        'Number 2': [random.randint(1, 1000) for _ in range(num_pairs)]}

# Create a DataFrame out of the numbers
df = pd.DataFrame(data)

# You could improve this code substantially by changing these sections so that no. seconds is calculated per pair - at the moment it's running the code over
# everything, and then taking the time.
start_time = time.time()
# lambda means 'make a new unnamed function', in this case with argument 'row'. This allows us to run a function over pairs of numbers very easily.
df['GCD_Euclidean'] = df.apply(lambda row: gcd_euclidean(row['Number 1'], row['Number 2']), axis=1)
df['Euclidean_Time'] = time.time() - start_time

# Measure time for Stein's algorithm
start_time = time.time()
df['GCD_Stein'] = df.apply(lambda row: gcd_stein(row['Number 1'], row['Number 2']), axis=1)
df['Stein_Time'] = time.time() - start_time

# Plot the comparison
df[['Euclidean_Time', 'Stein_Time']].plot(kind='bar', figsize=(10, 6))
plt.title('Comparison of GCD Algorithms')
plt.ylabel('Time (seconds)')
plt.xlabel('Random Number Pairs')
plt.grid(True)
plt.show()
