
import random


# runtime: 4*n + n^2 = O(n^2)
def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the friendship network as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    n = len(friends)
    network = []

    # Étape 1 : convert the list into something good******************
    # runtime: 1*n
    for i in range(n):
        friends[i] = friends[i].split(' ')
    # runtime: 1*n
    for i in range(1, n):  # cuz we dont wanna start with the first elementa
        friends[i][1] = int(friends[i][1])
    # runtime: 1*n
    for i in range(1, n):
        friends[i][0] = int(friends[i][0])

    # Étape 1 : convert the list into something good******************^^^^

    new_list1 = []

    # runtime: 1*n
    counter1 = 1  # cuz we dont wanna start with the first element
    while counter1 < n:
        if friends[counter1][0] not in new_list1:
            new_list1.append(int(friends[counter1][0]))
        if friends[counter1][1] not in new_list1:
            new_list1.append(int(friends[counter1][1]))
        counter1 = counter1 + 1
    new_list1.sort()

    # runtime: 1*n^2
    counter2 = 0
    n2 = len(new_list1)
    while counter2 < n2:
        new_list2 = []
        counter3 = 1
        while counter3 < n:
            if new_list1[counter2] in friends[counter3]:
                if friends[counter3][0] == new_list1[counter2]:
                    new_list2.append(friends[counter3][1])
                elif friends[counter3][0] != new_list1[counter2]:
                    new_list2.append(friends[counter3][0])
            counter3 = counter3 + 1
        create_tuple = (new_list1[counter2], new_list2)
        if new_list2 != []:
            network.append(create_tuple)
        counter2 = counter2 + 1

    # YOUR CODE GOES HERE

    # YOUR CODE GOES HERE *************************************************

    return network

def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->list
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs,
    and friends of user 1 and user 2 sorted
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]

    # YOUR CODE GOES HERE***************************************************************
#    network = create_network(network) # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    try:
        for i in network[user1][1]:
            for j in network[user2][1]:
                if i == j:
                    common.append(i)
        return common

    except:
        return common

    # YOUR CODE GOES HERE***************************************************************


###############################################################################
# My own function:
def most_common(friends):
    counter1 = 0
    highest = friends[0]

    for i in friends:
        counter2 = friends.count(i)
        if counter2 == counter1:
            if i < highest:
                highest = i
                counter1 = counter2

        elif counter2 > counter1:
            highest = i
            counter1 = counter2
    return highest
###############################################################################

def recommend(user, network):
    '''(int, 2D list)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.

    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''
#    network = create_network(network) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    n = len(network)
    acceptable = []
    already = []


    counter = 0
    for i in range(n):
        if network[i][0]==user:
            break
        counter = counter + 1


    user = counter
    #try:
    for i in network[user][1]:
        acceptable.append(i)

    new_list = []



    n_list = []
    counter = 0
    for i in range(n):
        if network[i][0] in acceptable:
            n_list.append(counter)
        counter = counter + 1


    acceptable = n_list


    for i in acceptable:
        for j in network[i][1]:
            if j not in acceptable and j != user:
                new_list.append(j)


    if new_list == []:
        return None

    max_num_friends = most_common(new_list)

    if max_num_friends == network[user][0]:
        return None
    return max_num_friends





def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    # YOUR CODE GOES HERE
#    network = create_network(network) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # for i in network:
    #     for j in range(len(i)):
    #         print(network[j][1])
    #         print("*")

    counter = 0
    for i in network:
        length = len(i[1])
        if length >= k:
            counter = counter + 1

    #print(counter)
    return counter


def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    # YOUR CODE GOES HERE
#    network = create_network(network) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    max = 0
    counter = 0
    for i in network:
        #print(i[1])
        counter = len(i[1])
        if counter > max:
            max = counter
    return max


def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    # YOUR CODE GOES HERE
#    network1 = create_network(network) #not calling it "neywork 1 crashes the program bc of next line" !!!!!!!!!!!!!!
    max = maximum_num_friends(network)
#    for i in network1:#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #print(i)
    for i in network:
        if len(i[1]) == max:
            max_friends.append(i[0])

    # YOUR CODE GOES HERE
    return max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    # YOUR CODE GOES HERE
#    network = create_network(network) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    sum = 0
    for i in network:
        counter = len(i[1])
        sum = sum + counter
    average = sum/len(network)
    return average

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''

    # YOUR CODE GOES HERE
#    network = create_network(network)  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    n = len(network)

    for i in range(n):
        if len(network[i][1]) == len(network)-1:
            return True
    return False


####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''

    # YOUR CODE GOES HERE
#    network = create_network(network) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    valid = []
    for i in network:
        valid.append(i[0])
    print(valid)
    flag = True
    while flag:
        try:
            id = int(input("Enter an integer for a user ID: "))########
            if id in valid:
                return id
                flag == False
            else:
                print("That user ID does not exist. Try again.")
        except ValueError:
            print("That was not an integer. Please try again.")


##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()

net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")


print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    
