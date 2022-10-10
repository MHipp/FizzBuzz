# For loop that iterates through till it reaches 100
for i in range(1, 101):
    # checks if remainder of 3 and 5 is 0 and prints FizzBuzz
    if(i%3 == 0 and i%5 == 0):
        print("FizzBuzz")
    # checks if remainder of 3 is 0 and prints Fizz
    elif(i%3 == 0):
        print("Fizz")
    # checks if remainder of 5 is 0 and prints Buzz
    elif(i%5 == 0):
        print("Buzz")
    # prints the number of all the other numbers
    else:
        print(i)