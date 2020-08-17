#
#   Python      3.8.5
#
#   Author:     Hayden Stark
#
#   Purpose:    Creating first Python program through The Tech Academy,
#               passing variables from function to function while producing
#               functional game


def start(nice=0,mean=0,name=""):
    #get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """ check if this is a new game or not
        if it's new, get the user's name.
        if not, thank the player for playing
        again and continue with the game """
    #meaning if we do not alreayd have user's name
    #then they are a new player and we need to get their name
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconverstaion. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name)       #passes 3 variables to score()


def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))


def score(nice,mean,name):
    #score function is being passed the values stored within the 3 variables
    if nice > 2:        #if valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2:        #if valid, calls lose function
        lose(nice,mean,name)
    else:               #else call nice_mean function, passing variables 
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    again(nice,mean,name)


def lose(nice,mean,name):
    print("\nAhh too bad, game over! \n{}, no one trusts you and you find yourself alone...".format(name))
    again(nice,mean,name)
    

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>>")
    

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #does not reset user's name
    start(nice,mean,name)





if __name__ == "__main__":
    start()
