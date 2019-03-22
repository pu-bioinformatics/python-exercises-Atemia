#!/Users/ATEMIA/miniconda3/bin/python

### Exercise
# Create a while loop that starts with x = 0 and increments x until x is equal to 5. Each iteration should print to the console.
# Repeat the previous problem, but the loop will skip printing x = 5 to the console but will print values of x from 6 to 10.
# Create a for loop that prints values from 4 to 10 to the console.

# Question 1
x = 0
while x <= 5:
    print(x)
    x += 1

    
# Question 2
x = 0
print(x)
while x < 10:
    x += 1
    if x == 5:
        continue
    print(x)
    
# Question 3 for loop
num = range(4,11)
for i, num in enumerate(num):
    print(num) # if you want to print with their index positions add ' i'

# Question 3 while loop
#x = 4
#while x <= 10:
#    print(x)
#    x += 1

#CK: This works well
