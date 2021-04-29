# Family name: Samy Touabi 
# Student number: 300184721  
# Course: ITI 1120 C
# Assignment Number 4 Question 1
# year 2020

raw_input = input("Please enter a list of integers separated by spaces: ").strip().split()
n = int(input("Please input an integer: "))

int_list = []
for i in raw_input:
    int_list.append(int(i))

def number_divisible(int_list, n):
    '''(list of int, int) -> int
    Preconditions: int_list and n are real integers
    Returns the amount of elements in int_list divisible by n
    '''
    counter = 0
    for i in range(len(int_list)):
        if int_list[i] % n == 0:
            counter = counter + 1
    return counter

print("The number of elements divisible by " + str(n) + " is " + str(number_divisible(int_list, n)))
