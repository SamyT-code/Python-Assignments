# Family name: Samy Touabi 
# Student number: 300184721  
# Course: IT1 1120 C
# Assignment Number 1
# year 2020



########################
# Question 1
########################

def poem_generator():
    ''' ( ) -> None
    This function prompts the user to enter a city and a name in string
    Prints a poem that includes the name and the city of birth
    '''

    name = input("Enter your name: ")
    city = input("Enter your city of birth: ")

    print("")
    print(name + " was, by no means, a quiet and peaceful child")
    print("The troubles " + name + " made, never were mild ")
    print("At " + city + ", " + name + " was known")
    print("For always being alone")
    print("And always, reports for " + name + "'s bad behaviour were filed")

    return




########################
# Question 2
########################

def impl2loz(w):
    ''' (number) -> number, number
    Precondition: w is a non-negative number
    Returns l (an integer) and o (a non-negative number smaller than 16)
    '''
        
    u = w - int(w)	
    o = 16 * u
    l = int(w - o/16)
    return (l, o) # return l first, then o




########################
# Question 3
########################

def pale(n):
    ''' (int) -> bool
    Returns true or false depending on the number being pale or not 
    preconditions: n is a positive integer with four digits
    '''
    w = n // 1000
    x = n // 100 - w * 10
    y = n // 10 - (n // 100 * 10)
    z = n - (n // 10 * 10)
    condition = not( ( z % 4 == 0 ) or ( ( w == 3 and x ==3) or
                ( x == 3 and y == 3 ) or (y == 3 and z == 3) ) )
    return condition




########################
# Question 4
########################

def bibformat(author,title,city,publisher,year):
    ''' (str, str, str, str, str) -> None
    Prints the elements in a bibliographic format
    '''
    print("'" + author + " (" + str(year) + "). " + title + ". " + city +
          ": " + publisher + ".'")
    return 



########################
# Question 5
########################

def bibformat_display():
    ''' (str, str, str, str, str) -> None
    prompts the user for a book title, name of the author,
    year of publication, publisher and the headquarter city of the publisher
    '''
    title = input("What is the title of the book: ")
    author = input("What is the name of the author: ")
    year = input("What is the year of the publication: ")
    publisher = input("What is the name of the publisher: ")
    city = input("In what city was the book published: ")
    print("")
    print(bibformat(author, title, city, publisher, year))
    
    return 



########################
# Question 6
########################

def compound(x, y, z):
    ''' (int, int, int) -> bool
    Returns true or false depending on the conditions beig all met or not
    Preconditions: x, y and z are all integers
    '''
    return  ( (x%2 == 0) and (y%2 != 0) and (z%2 != 0) ) and ( ((x + y) > 100)  or ((x + z) > 100) or  ((y + z) > 100) )




########################
# Question 7
########################

def  funct(p):
    ''' (number) -> None
    Prints a message telling you the solution for r
    Precondition: p must be greater or equal to 11
    '''
    import math
    r = math.sqrt(math.log(p-10,5))
    print("The solution is ", r)
    return 




########################
# Question 8
########################

def gol(n):
    ''' (number) -> number
    Returns the minimum number of times that n needs to be divided by 2
    in order to get a number equal or smaller than 1
    Precondition: n is bigger or equal to 1 
    '''
    import math
    d = math.ceil(math.log(n,2))
    return d




########################
# Question 9
########################

def cad_cashier(price,payment):
    ''' (number, number) -> number
    Returns the change in a canadian currency format
    Precondition: price and payment are two real non-negative numbers
    with two decimal places as input, where payment>=price and where
    the second decimal in payment is 0 or 5 
    '''
    exact_return = payment - price
    round_multiplication = round(exact_return * 2, 1)
    division = round_multiplication / 2
    change = round(division, 2)
    change = float(change)
    
    return change




########################
# Question 10
########################

def min_CAD_coins(price,payment):
    ''' (number, number) -> int, int, int, int, int
    Returns the minimum amount of change in coins (and their type)
    a cashier can return
    Precondition: price and payment are two real non-negative numbers
    with two decimal places as input, where payment>=price and where
    the second decimal in payment is 0 or 5
    '''

    spare = cad_cashier(price, payment) * 100 + 1
    t = int(spare // 200)
    spare = spare - (t * 200)
    l = int(spare // 100)
    spare = spare - (l * 100)
    q = int(spare // 25)
    spare = spare - (q * 25)
    d = int(spare // 10)
    spare = spare - (d * 10)
    n = int(spare // 5)
    spare = spare - (n * 5)
    return t, l, q, d, n

