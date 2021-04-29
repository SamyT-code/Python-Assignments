# Family name: Samy Touabi 
# Student number: 300184721  
# Course: ITI 1120 C
# Assignment Number 3
# year 2020


########################
# Exercise 1
########################

def is_up_monotone(X, d):
    '''(str, str) -> bool
    Preconditions: X and d are integers (inside a string)
    and d is a multiple of the length of X
    This function seperates the number entered in X into d
    digits and determines if these numbers are up-monotone
    Returns True or False
    '''
    # Your code for is_up_monotone function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    flag = False
    ns = ""
    digits = int(d)

    for i in range(0, len(X) // digits):
        ns = ns + X[digits * i: i * digits + digits] + ","

    ns = ns[:-1]

    print(ns)

    ns1 = ns.replace(",","")

    for i in range(0, len(ns1)//digits-1):
        if float(ns1[i*digits:i*digits+digits]) >= float(ns1[i*digits+digits:i*digits+digits+digits]):
            flag = False
            break
        else:
            flag = True


    if len(X) == int(d):
        flag = True

    return flag

# you can add more function definitions here if you like


# main

print("*******************************************")
print("**")
print("*__Welcome to up-monotone-inquiry__*")
print("**")
print("*******************************************")

name = input("What is your name? ")
print("*******************************************")
print("**")
print("*__" + name + ", welcome to up-monotone inquiry" + "__*")
print("**")
print("*******************************************")

# Your code for the welcome message goes here, instead of name="Vida"
# name="Vida"

flag = True
newflag = True
while flag:
    question = input(name + ", would you like to test if a number admits an up-monotone split of given size? ")
    question = (question.strip()).lower()
    if question == 'no':
        flag = False
    # YOUR CODE GOES HERE. The next line should be elif or else.
    elif question == "yes":  # if question is yes
        print("Good choice!")
        X = input("Enter a positive integer: ")

        if X == "" or X == "0":
            print("You must enter a number. Try again.")
            continue

        for i in X:
            if i not in "-.0123456789":
                print("The input can only contain digits. Try again.")
                newflag = False
                break
            else:
                newflag = True

        if newflag == False:
            continue

        if float(X) != abs(float(X)):
            print("The input has to be a positive integer. Try again.")
            continue

        if float(X)%1 != 0:
            print("The input can only contain digits. Try again.")
            continue


        print("Input the split. The split has to divide the length of " + X + " i.e. " + str(len(X)))
        d = input("")

        if d.isdigit() == False:
            print("You must enter a positive number. Try again.")
            continue

        if int(len(X)) % int(d) == 0:
            if is_up_monotone(X, d) == True:
                print("The sequence is up-monotone")
            else:
                print("The sequence is not up-monotone")
        else:
            print("does not divide " + str(len(X)) + ". Try again.")

    else:
        print("Please enter yes or no. Try again.")

print("*******************************************")
print("**")
print("*__Good bye " + name + "!__*")
print("**")
print("*******************************************")

# finally your code goes here too.
