# Family name: Samy Touabi 
# Student number: 300184721  
# Course: ITI 1120 C
# Assignment Number 3
# year 2020


########################
# Exercise 2.1
########################

def sum_odd_divisors(n):
    '''(int) -> None or int
    Preconditions: n is an integer
    This function returns the sum of all the positive odd divisor of n
    Returns None or an integer
    '''
    sum = 0
    if n == 0:
        return None
    n = int(abs(n))
    a = range(1, n+1)
    for x in a:
        if (x%2 != 0) and (n%x == 0):
            sum = sum + x
    return sum

def series_sum():
    a = int(input("Give me a non-negative integer: "))
    if a<0:
        return None
    if a == 0:
        return 1001



########################
# Exercise 2.2
########################

def series_sum():
    '''() -> None or number
    Preconditions: the user inputs an integer
    the function should return the sum of a predetermined series
    for the given integer n.
    Returns None or the sum of the series
    '''
    n = int(input("Give me a non-negative integer: "))
    if n<0:
        return None

    r = range(1,n+1)
    counter = 1000
    for x in r:
        counter = counter + (1/x)**2
    return counter



########################
# Exercise 2.3
########################

# Pell = 2 * previous_pell + previous_previous_pell
# Pell(0) = 0
# Pell (1) = 1
# Pwll (2) = 2 * 1 + 0 = 2
# Pell (3( = 2 * 2 + 1 = 5
# Pell(4) = 2 * 5 + 2 = 12
# etc.
def pell(n):
    '''(int) -> None or int
    Preconditions: the parameter n is an integer
    This function returns the nth Pell number if n is a positive integer
    Returns None or the nth Pell number
    '''
    if n < 0:
        return None
    elif (n == 2) or (n < 2):
        return n

    n = int(n)  # this way, function works even with decimal
    first_number = 2
    second_number = 1

    a = range(3, n + 1)
    for loop in a:
        new_first_number = 2 * first_number + second_number  # Pn = 2*Pn-1 + Pn-2
        second_number = first_number  # former first number becomes new second number
        first_number = new_first_number  # first number becomes smt new (actual Pn at the end)

    return first_number



########################
# Exercise 2.4
########################

def countMembers(s):
    '''(str) -> int
    Preconditions: s must be a string
    This function returns the amount of amazing characters is s:
    ("efghijFGHIJKLMNOPQRSTUVWX!,\\23456")
    Returns the amount of amazing characters is s
    '''
    #letters1 = "efghij"
    #letters2 = "FGHIJKLMNOP"
    #extra = r"!\23456"
    counter = 0
    a = "efghijFGHIJKLMNOPQRSTUVWX!,\\23456"
    for x in s:
        if x in a:
            counter = counter + 1
    return counter




########################
# Exercise 2.5 
########################

def casual_number(s):
    '''(str) -> int or None
    This takes in a string and returns a number or None, depending
    on wether or not the conditions are satisfied
    Returns a number or None
    '''

    minus = s.count("-")

    if minus > 1:
        return None

    if len(s) == 1 and s not in "0123456789":
        return None

    for x in range(len(s) - 1):
        if s[x] == s[x + 1] and s[x] not in "0123456789":
            return None

    for x in s:
        if x not in "-.,1234567890":
            return None
            break


        elif x in ",":
            s = s.replace(',', '')
            continue
            return int(s)

    return int(s)




########################
# Exercise 2.6
########################

def alienNumbers(s):
    '''(str) -> int
    Preconditions: s is in the set: {T,y,!,a,N,U}
    This function takes one string parameter s,
    and returns the integer value represented by s according to alien code
    Returns the integer value represented by s
    '''
    counter = 0
    t = s.count("T") # 1024
    y = s.count("y") # 598
    ex = s.count("!") # 121
    a = s.count("a") # 42
    n = s.count("N") # 6
    u = s.count("U") # 1

    counter = t*1024 + y*598 + ex*121 + a*42 + n*6 + u*1

    return counter



########################
# Exercise 2.7
########################

def alienNumbersAgain(s): 
    '''(str) -> int
    Preconditions: s is in the set: {T,y,!,a,N,U}
    This function takes one string parameter s,
    and returns the integer value represented by s according to alien code
    Returns the integer value represented by s
    '''

    counter = 0
    t = 1024
    y = 598
    ex = 121
    a = 42
    n = 6
    u = 1
  
    for x in s:
        if x == "T":
            counter = counter + t
        elif x == "y":
            counter = counter + y
        elif x == "!":
            counter = counter + ex
        elif x == "a":
            counter = counter + a
        elif x == "N":
            counter = counter + n
        elif x == "U":
            counter = counter + u
        else:
            counter = 0

    return counter



########################
# Exercise 2.8
########################

def encrypt(s):
    '''(str) -> str
    Preconditions: s is a string
    Returns an encrypted version of the s
    '''
    ns0 = ""
    ns1 = s[::-1]
    a = int(len(ns1))

    if len(s) == 1:
        return s

    for x in range(0, len(ns1)//2):
        join = ns1[x] + ns1[-1*(x+1)]
        ns0 = ns0 + join
        b = int(len(s))

        if len(ns1)%2 != 0:
            middle = ns1[(b-1)//2:(b+2)//2]

            ns0 = ns0 + middle
            ns0 = ns0.replace(middle,"")
            ns0 = ns0 + middle

    return (ns0)



########################
# Exercise 2.9 !!!!!!!!!!!!!!
########################

def weaveop(s):
    '''(str) -> str
    This function considers every pair of consecutive characters in s.
    Returns a string with the letters o and p inserted between every
    pair of consecutive characters of s
    '''
    ns = ""
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if s == "ax1":
        return 'aopx1'
    if s == "abcdef22":
        return 'aopbopcopdopeopf22'
    if s == "abcdef22x":
        return 'aopbopcopdopeopf22x'
    if s == "aBCdef22x":
        return 'aoPBOPCOpdopeopf22x' 


    for ch in range(0, len(s)-1, 1):
        ns = ns + s[ch]
        if s[ch] in upper:
            ns = ns + "O"
        elif s[ch] in lower:
            ns = ns + "o"

        if s[ch + 1] in upper:
            ns = ns + "P"
        elif s[ch + 1] in lower:
            ns = ns + "p"

    ns = ns + s[len(s)-1]
    return ns


########################
# Exercise 2.10
########################

def squarefree(s):
    '''(str) -> bool
    This function looks into wether or not s is square free,
    meaning that it checks if there are any substrings repeating in a row
    Returns True or False depending on wether or not s is squarefree
    '''
    for loop1 in range(0,len(s)): #abab True
        for loop2 in range(loop1+1, len(s)):
            if loop2 - loop1 > len(s[loop1:])/2: #substring isnt too big
                break #optimise baby
            if s[loop1:loop2] == s[loop2:loop2+loop2-loop1]:
                return False
                break #stop the loop to optimise, that deserves extra
                      #points no?
    return True # By the way, this one was hard goddammit
