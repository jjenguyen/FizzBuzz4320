for i in range(1, 101):
    # check if number is divisible by 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # check if number is only divisible by 3
    elif i % 3 == 0:
        print("Fizz")
    # check if number is only divisible by 5
    elif i % 5 == 0:
        print("Buzz")
    # if number is not divisible by 3 or 5, print the number
    else:
        print(i)