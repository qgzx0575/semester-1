
import matplotlib.pyplot as plt  # import library

x = [ k for k in range(10) ]  # create a range for the data
y = [ k*k for k in x ]      # create a simple function y=x^2

plt.plot(x,y)  # create a 2d plot

plt.xlabel('x')
plt.ylabel('y=x^2')  # annotate

plt.show()  # display

# Test the example as is on the slides
# - Modify the data and the range
# - Plot in different ways
# Read matplotlib documentation
# - Test some other plotting functions
