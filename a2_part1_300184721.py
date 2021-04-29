# Family name: Samy Touabi 
# Student number: 300184721  
# Course: IT1 1120 C
# Assignment Number 2
# year 2020

import random
import math


def elementary_school_quiz(flag, n):
    # Your code for elementary_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    #
    # Preconditions: flag is 0 or 1, n is 1 or 2

    '''(int, int) - > int
    Preconditions: flag is 0 or 1, n is 1 or 2
    This question gives a set amount of question (1 or 2) on substractions
    or on exponents based on the inputted answer.
    Returns the amount of right answers (0, 1, or 2)
    '''

    counter = 0

    if n == 1 and flag == 0:
        
        x = random.randint(1, 9)
        y = random.randint(1, 9)
        a = str(x)
        b = str(y)
        answer = y - x

        print("Question 1:")
        student_answer = input("What is " + b + " - " + a + " : ")
        if (int(student_answer) == answer):
            counter = counter + 1

    if n == 2 and flag == 0:
        x1 = random.randint(1, 9)
        y1 = random.randint(1, 9)

        x2 = random.randint(1, 9)
        y2 = random.randint(1, 9)

        a = str(x1)
        b = str(y1)
        c = str(x2)
        d = str(y2)

        answer1 = y1 - x1
        answer2 = y2 - x2

        print("Question 1:")
        student_answer1 = input("What is " + b + " - " + a + " : ")
        if (int(student_answer1) == answer1):
            counter = counter + 1

        print("Question 2:")
        student_answer2 = input("What is " + d + " - " + c + " : ")
        if (int(student_answer2) == answer2):
            counter = counter + 1


    if n == 1 and flag == 1:
        x = random.randint(1, 9)
        y = random.randint(1, 9)
        a = str(x)
        b = str(y)
        answer = x ** y

        print("Question 1:")
        student_answer = input("What is " + a + " to the power of " + b + " : ")

        if (int(student_answer) == answer):
            counter = counter + 1


    if n == 2 and flag == 1:
        x1 = random.randint(1, 9)
        y1 = random.randint(1, 9)

        x2 = random.randint(1, 9)
        y2 = random.randint(1, 9)

        a = str(x1)
        b = str(y1)
        c = str(x2)
        d = str(y2)

        answer1 = x1 ** y1
        answer2 = x2 ** y2

        print("Question 1:")
        student_answer1 = input("What is " + a + " to the power of " + b + " : ")
        if (int(student_answer1) == answer1):
            counter = counter + 1

        print("Question 2:")
        student_answer2 = input("What is " + c + " to the power of " + d + " : ")
        if (int(student_answer2) == answer2):
            counter = counter + 1

    return counter






def high_school_quiz(a, b, c):
    # Your code for high_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function ⋅
    '''(number, number, number) -> None
    Preconditions: a, b and c are all real numbers
    This functions takes the coefficients of a quadratic formula as input and
    returns the type of roots belonging to that formula as well as their values 
    '''

    discriminant = b ** 2 - 4 * a * c

    d = str(a)
    e = str(b)
    f = str(c)

    if (a == 0) and (b == 0) and (c != 0):
        print("The quadratic equation 0x + " + f + " = 0")
        print("is satisfied for no number x")

    elif (a == 0) and (b != 0) and (c != 0):
        x = str(-c / b)
        print("The linear equation")
        print(e + "x + " + f + " = 0")
        print("has the following root/solution:", x)

    elif (a == 0) and (b == 0) and (c == 0):
        print("The quadratic equation 0x + 0 = 0")
        print("Is satisfied with all numbers x")

    elif (discriminant < 0):
        xa = str((-1 * b) / (2 * a))
        xb = str((math.sqrt(abs(b ** 2 - 4 * a * c))) / (2 * a))

        print("The quadratic equation " + d + "x^2 + " + e + "x + " + f)
        print("Has the following complex roots:")
        print(xa, "+ i", xb)
        print("and")
        print(xa, "- i", xb)

    elif (discriminant == 0):
        print("The quadratic equation " + d + "x^2 + " + e + "x + " + f)
        x1 = str((-b + math.sqrt(discriminant)) / (2 * a))
        print("has only one solution, a real root:")
        print(x1)

    elif (discriminant > 0):
        x1 = str((-b + math.sqrt(discriminant)) / (2 * a))
        x2 = str((-b - math.sqrt(discriminant)) / (2 * a))

        print("The quadratic equation " + d + "x^2 + " + e + "x + " + f)
        print("has the following real roots:")
        print(x1, "and", x2)

#elementary_school_quiz(0, 1)
#print(elementary_school_quiz(0, 1))



print("*******************************************")
print("**")
print(" __Welcome to my math quiz-generator__ ")
print("**")
print("*******************************************")

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

if status == '1':
    # your code goes here
    print("******************************************************************************")
    print("**")
    print("*__"+ name + ", welcome to my quiz-generator for elementary school students__*")
    print("**")
    print("******************************************************************************")
    choice_flag = int(input(name + " what would you like to practise? Enter \n0 for subtraction \n1 for exponentiation \n"))

    
    choice_n = int(input("How many practice questions would you like to do? Enter 0, 1, or 2: "))


    if (choice_flag != 0) and (choice_flag != 1):
        print("Invalid choice for question type. Only 0 or 1 is accepted.")

    if (choice_n != 1) and (choice_n != 2):
        print("Only 0, 1, or 2 are valid choices for the number of questions.")
    
    if  choice_n == 0:
        print("Zero questions. OK. Goodbye")
    elif (choice_flag == 0 and choice_n == 1):
        print(name + ", here is your question")
        a = elementary_school_quiz(0, 1)
        a = int(a)
        print(a)
        if int(a) == 1 :
            print("Congratulations "+ name+ "! You got the right anwser. You'll probably get an A tomorrow. ")
        else:
            print("I think you need some practise "+ name + ".")

    elif (choice_flag == 0 and choice_n == 2):
        print(name + ", here are your 2 questions")
        a = elementary_school_quiz(0, 2)
        a = int(a)
        print(a)
        if int(a) == 2:
            print("Congratulations " + name + "! You got the right answers. You'll probably get an A tomorrow. ")
        elif int(a) == 1:
            print("You did ok " + name + ", but I know you can do better.")
        else:
            print("I think you need some practise "+ name + ".")

    elif (choice_flag == 1 and choice_n == 1):
        a = elementary_school_quiz(1, 1)
        a = int(a)
        print(a)
        if int(a) == 1:
            print("Congratulations"+ name+ "! You got the right anwser. You'll probably get an A tomorrow. ")
        else:
            print("I think you need some practise "+ name + ".")

    elif (choice_flag == 1 and choice_n == 2):
        a = elementary_school_quiz(1, 2)
        a = int(a)
        print(a)
        if int(a) == 2:
            print("Congratulations " + name + "! You got the right answers. You'll probably get an A tomorrow. ")
        elif int(a) == 1:
            print("You did ok " + name + ", but I know you can do better.")
        else:
            print("I think you need some practise "+ name + ".")

    
elif status == '2':

    # your code for welcome message
    print("******************************************************************************")
    print("**")
    print("* __quadratic equation, a·x^2 + b·x + c= 0, solver for" + name + "__ *")
    print("**")
    print("******************************************************************************")

    flag = True
    while flag:

        # your code to handle varous form of "yes" goes here
        question = input(name + ", would you like a quadratic equation solved? ")
        question = question.replace(" ", "")
        question = question.lower()


        # your code goes here (i.e ask for coefficients a,b and c and call)
        # then make a function call and pass to the function
        # the three coefficients the pupil entered
        if question != "yes":
            flag = False
        else:
            print("Good choice!")
            a = float(input("Enter the number of the coefficient a: "))
            b = float(input("Enter the number of the coefficient b: "))
            c = float(input("Enter the number of the coefficient c: "))

            high_school_quiz(a, b, c)
 
else:
    # your code goes here
    print("Ah")
    print(name + " you are not a target audience for this software")

print("Good bye "+name+"!")
