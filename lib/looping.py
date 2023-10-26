#!/usr/bin/env python3

def happy_new_year():
    number = 10
    while number > 1:
        print(number)
        number-=1
    print(number)
    print("Happy New Year!")
    

def square_integers(int_list):
    new_list = [num * num for num in int_list]
    return new_list

def fizzbuzz():
    for position in range(100):
        num = position + 1
        three = num % 3 == 0
        five = num % 5 == 0
        # ipdb.set_trace()
        if three and five:
            print("FizzBuzz")
        elif three and not five:
            print("Fizz")
        elif five and not three:
            print("Buzz")
        else:
            print(num)
        

