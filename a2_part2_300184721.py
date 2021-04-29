# Family name: Samy Touabi 
# Student number: 300184721  
# Course: IT1 1120 C
# Assignment Number 2
# year 2020


###################
# Exercice 2.1
###################

def min_enclosing_rectangle(radius, x, y):
    '''(float, float, float) -> float, float OR None
        This function prompts the user to enter a radius and x,y coordinates
        Returns a new set of x,y coordinates if radius is positive, otherwise
        the function returns None
        Preconditions: radius, x, and y must all be real numbers
    '''
    new_x = x - radius
    new_y = y - radius
    
    if radius < 0:
        return None
    
    return new_x, new_y


###################
# Exercice 2.2
###################

def vote_percentage(results):
    '''(str) -> float
    Preconditions: string results has at least one yes or no and that the only words
    present are yes, no and/or abstained
    Returns a float in a decimal inferior or equal to 1 to represent a percentage
    '''
    yes_count = results.count("yes")
    no_count = results.count("no")
    total = yes_count + no_count
    percentage_yes = yes_count / total
    return percentage_yes


###################
# Exercice 2.3
###################

def vote():
    '''( ) -> None
    This function prompts the user to enter a desired amount of yes/no/abstained
    and prints, based on the percentage of yes, in what manner a vote passes
    Preconditions: only words present in the input prompt are yes, no and/or abstained
    '''
    ballot = input("Enter the yes, no, abstained votes one by one and then press enter: ")
    if vote_percentage(ballot) == 1:
        print("proposal passes unanimously")
    elif vote_percentage(ballot) >= 2/3:
        print("proposal passes with super majority")
    elif vote_percentage(ballot) >= 1/2:
        print("proposal passes with simple majority")
    else:
        print("proposal fails")
        
