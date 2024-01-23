"""  
Your program should print each number from 1 to 100 in turn.

When the number is divisible by 3 then instead of printing the number it should print "Fizz".

When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
"""

words = ["Fizz", "Buzz", "FizzBuzz"]

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(words[2])
    elif num % 3 == 0:
        print(words[0])
    elif num % 5 == 0:
        print(words[1])
    else:
        print(num)
