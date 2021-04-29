# Family name: Samy Touabi 
# Student number: 300184721  
# Course: ITI 1120 C
# Assignment Number 4 Question 2
# year 2020

raw_input = input("Please enter a list of integers separated by spaces: ").strip().split()
n = []
for i in raw_input:
    n.append(float(i))

def two_length_run(n):
    '''(list of int) -> bool
    Preconditions: The list is comprised of real numbers
    Returns True if the list has at leat one run. Returns False otherwise
    '''
    for i in range(len(n)-1):
        if n[i] == n[i+1]:
            return True
    return False

print(two_length_run(n))
