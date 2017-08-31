# goes through an array of integers from 1 to 45
for num in range(1, 46):
    if num % 15 == 0:
        # prints fizzbuzz if num is divisible by 3 and 5
        print("fizzbuzz")

    elif num % 3 == 0:
        # prints fizz if num is divisible by 3
        print("fizz")

    elif num % 5 == 0:
        # prints buzz if num is divisible by 5
        print("buzz")

    else:
        # prints num if not divisible by 3, 5, or both.
        print(num)
