# Family name: Samy Touabi 
# Student number: 300184721  
# Course: ITI 1120 C
# Assignment Number 4 Question 3
# year 2020

raw_input = input("Please enter a list of integers separated by spaces: ").strip().split()
n = []
for i in raw_input:
    n.append(float(i))
    
def longest_run(n):
    '''(list of numbers) -> int
    Preconditions: the list is made up of numbers
    Returns the lenght of the longest run of the list
    '''
    counter = 1
    new_counter = 1
    a = len(n)

    if a==0 : # If list is empty
        return 0
    
    for i in range(a-1):
        if n[i] == n[i+1]:
            counter = counter + 1
        elif n[i] != n[i+1]:
            counter = 1 #restart the counter

        if counter > new_counter:
            new_counter = counter

    return new_counter

print(longest_run(n))
