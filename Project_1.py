#Project 1 - Black Jack Game
#Code Team: Chris Hernandez and Edward Gonzalez

#Imporing the random module.
import random

#Defining the function called, num without a(any) parameter(s).
def num():
    #Globalizing the variable two so that it can be used outside the function num.
    global two
    #Globalizing the variable three so that it can be used outside the function num.
    global three
    #Globalizing the variable four so that it can be used outside the function num.
    global four
    #Globalizing the variable five so that it can be used outside the function num.
    global five
    #Globalizing the variable six so that it can be used outside the function num.
    global six
    #Globalizing the variable seven so that it can be used outside the function num.
    global seven
    #Globalizing the variable eight so that it can be used outside the function num.
    global eight
    #Globalizing the variable nine so that it can be used outside the function num.
    global nine
    #Globalizing the variable ten so that it can be used outside the function num.
    global ten
    #Globalizing the variable jack so that it can be used outside the function num.
    global jack
    #Globalizing the variable two so that it can be used outside the function num.
    global king
    #Globalizing the variable queen so that it can be used outside the function num.
    global queen
    #Globalizing the variable ace so that it can be used outside the function num.
    global ace
    #Assigning each suit for the number 2 card as a list to the variable two.
    two = ["2 of clubs", "2 of diamonds", "2 of hearts", "2 of spades"]
    #Assigning each suit for the number 3 card as a list to the variable three.
    three = ["3 of clubs", "3 of diamonds", "3 of hearts", "3 of spades"]
    #Assigning each suit for the number 4 card as a list to the variable four.
    four = ["4 of clubs", "4 of diamonds", "4 of hearts", "4 of spades"]
    #Assigning each suit for the number 5 card as a list to the variable five.
    five = ["5 of clubs", "5 of diamonds", "5 of hearts", "5 of spades"]
    #Assigning each suit for the number 6 card as a list to the variable six.
    six = ["6 of clubs", "6 of diamonds", "6 of hearts", "6 of spades"]
    #Assigning each suit for the number 7 card as a list to the variable seven.
    seven = ["7 of clubs", "7 of diamonds", "7 of hearts", "7 of spades"]
    #Assigning each suit for the number 8 card as a list to the variable eight.
    eight = ["8 of clubs", "8 of diamonds", "8 of hearts", "8 of spades"]
    #Assigning each suit for the number 9 card as a list to the variable nine.
    nine = ["9 of clubs", "9 of diamonds", "9 of hearts", "9 of spades"]
    #Assigning each suit for the number 10 card as a list to the variable ten.
    ten = ["10 of clubs", "10 of diamonds", "10 of hearts", "10 of spades"]
    #Assigning each suit for the jack card as a list to the variable jack.
    jack = ["jack of clubs", "jack of diamonds", "jack of hearts", "jack of spades"]
    #Assigning each suit for the king card as a list to the variable king.
    king = ["king of clubs", "king of diamonds", "king of hearts", "king of spades"]
    #Assigning each suit for the queen card as a list to the variable queen.
    queen = ["queen of clubs", "queen of diamonds", "queen of hearts", "queen of spades"]
    #Assigning each suit for the ace card as a list to the variable ace.
    ace = ["ace of clubs", "ace of diamonds", "ace of hearts", "ace of spades"]

#Defining the function, called useramount without a(any) parameter(s).
def useramount():
    #Globalizing the variable accumulate so that it can be used outside the function useramount.
    global accumulate
    #Assigning the integer number 0 to the variable accumulate.
    accumulate = 0
    #Using a for loop to assign an item from the list in the variable usercard to the variable x for each iteration.
    for x in usercard:
        #An if statement that will execute the code below it if the condition "2" is in the string in the variable x.
        if ("2" in x):
            #Assigning the result of accumulate + 2 to the variable accumulate.
            accumulate+=2
        #An elif statement that will execute the code below it if the condition "3" is in the string in the variable x.
        elif ("3" in x):
            #Assigning the result of accumulate + 3 to the variable accumulate.
            accumulate+=3
        #An elif statement that will execute the code below it if the condition "4" is in the string in the variable x.
        elif ("4" in x):
            #Assigning the result of accumulate + 4 to the variable accumulate.
            accumulate+=4
        #An elif statement that will execute the code below it if the condition "5" is in the string in the variable x.
        elif ("5" in x):
            #Assigning the result of accumulate + 5 to the variable accumulate.
            accumulate+=5
        #An elif statement that will execute the code below it if the condition "6" is in the string in the variable x.
        elif ("6" in x):
            #Assigning the result of accumulate + 6 to the variable accumulate.
            accumulate+=6
        #An elif statement that will execute the code below it if the condition "7" is in the string in the variable x.
        elif ("7" in x):
            #Assigning the result of accumulate + 7 to the variable accumulate.
            accumulate+=7
        #An elif statement that will execute the code below it if the condition "8" is in the string in the variable x.
        elif ("8" in x):
            #Assigning the result of accumulate + 8 to the variable accumulate.
            accumulate+=8
        #An elif statement that will execute the code below it if the condition "9" is in the string in the variable x.
        elif ("9" in x):
            #Assigning the result of accumulate + 9 to the variable accumulate.
            accumulate+=9
        #An elif statement that will execute the code below it if the condition "10" in x or "jack" in x or "king" in x or "queen" in x is true.
        elif ("10" in x or "jack" in x or "king" in x or "queen" in x):
            #Assigning the result of accumulate + 10 to the variable accumulate.
            accumulate+=10
        #An elif statement that will execute the code below it if "ace" is in the string in the variable x.
        elif ("ace" in x):
            #An if statement that will execute the code below it if the condition accumulate >= 11 is true.
            if (accumulate >= 11):
                #Assigning the result of accumulate + 1 to the variable accumulate.
                accumulate+=1
            #An else keyword that will execute the code below it if the other conditional statement is not true.
            else:
                #Assigning the result of accumulate + 11 to the variable accumulate.
                accumulate+=11

#Defining the function, called dealeramount without a(any) parameter(s).
def dealeramount():
    #Globalizing the variable accumulate2 so that it can be used outside the function dealeramount.
    global accumulate2
    #Assigning the integer number 0 to the variable accumulate2.
    accumulate2 = 0
    #Using a for loop to assign an item from the list in the variable dealercard to the variable y for each iteration .
    for y in dealercard:
        #An if statement that will execute the code below it if "2" is in the sting in the variable y.
        if ("2" in y):
            #Assigning the result of accumulate2 + 2 to the variable accumulate2.
            accumulate2+=2
        #An elif statement that will execute the code below it if "3" is in the string in the variable y.
        elif ("3" in y):
            #Assigning the result of accumulate2 + 3 to the variable accumulate2.
            accumulate2+=3
        #An elif statement that will execute the code below it if "4" is in the string in the variable y.
        elif ("4" in y):
            #Assigning the result of accumulate2 + 4 to the variable accumulate2.
            accumulate2+=4
        #An elif statement that will execute the code below it if "5" is in the string in the variable y.
        elif ("5" in y):
            #Assigning the result of accumulate2 + 5 to the variable accumulate2.
            accumulate2+=5
        #An elif statement that will execute the code below it if "6" is in the string in the variable y.
        elif ("6" in y):
            #Assigning the result of accumulate2 + 6 to the variable accumulate2.
            accumulate2+=6
        #An elif statement that will execute the code below it if "7" is in the string in the variable y.
        elif ("7" in y):
            #Assigning the result of accumulate2 + 7 the variable accumulate2.
            accumulate2+=7
        #An elif statement that will execute the code below it if "8" is in the string in the variable y.
        elif ("8" in y):
            #Assigning the result of accumulate2 + 8 to the variable accumulate2.
            accumulate2+=8
        #An elif statement that will execute the code below it if "9" is in the string in the variable y.
        elif ("9" in y):
            #Assigning the result of accumulate2 + 9 to the variable accumulate2.
            accumulate2+=9
        #An elif statement that will execute the code below it if "10" in y or "jack" in y or "king" in y or "queen" in y is true.
        elif ("10" in y or "jack" in y or "king" in y or "queen" in y):
            #Assigning the result of accumulate2 + 10 to the variable accumulate2.
            accumulate2+=10
        #An elif statement that will execute the code below it if "ace" is in the string in the variable y.
        elif ("ace" in y):
            #An if statement that will execute the code below it if the condition accumulate2 >= 11 is true.
            if (accumulate2 >= 11):
                #Assigning the result of accumulate2 + 1 to the variable accumulate2.
                accumulate2+=1
            #An else keyword that will execute the code below it if the other conditional statement is not true.
            else:
                #Assigning the result of accumulate2 + 11 to the variable accumulate2.
                accumulate2+=11

#Defining the function called, num without a(any) parameter(s).
def hitOrStay():
    #Printing a string and a new line to the display.
    print("Do you want to hit or do you want to stay?\n")
    #Receiving user input and assigning the input value as a string to the variable value.
    value = input("Type 1 and press enter if you want to hit or type 0 and press enter if you want to stay: ")
    #Print function.
    print()
    #Printing 50 asterisks in a row to the display.
    print('*' * 50, '\n')
    #Returning the content of the variable value.
    return value

#Defining the function called, winOrLose without a(any) parameter(s).
def winOrLose():
    #An if statement that will execute the code below it if the condition accumulate > 21 is true.
    if (accumulate2 > 21):
        #Printing a string to the display and using the end="" statement to prevent the interpreter from printing text on the next line.
        print("The dealer has the cards ", end="")
        #Using a for loop to assign an item from the list in the variable dealercard to the variable i for each iteration.
        for i in dealercard:
            #An if statement that will execute the code below it if the condition i == dealercard[-1] is true.
            if (i == dealercard[-1]):
                #Printing a string and formatting it to also display the variable i.
                print(f"and {i}.")
            #An else keyword that will execute the code below it if the other conditional statement is not true.
            else:
                #Printing a string and formatting it to also display the variable i. In addition, the end="" statement is used to prevent the interpreter from printing text on the next line.
                print(f"{i}, ", end="")
        #Print function.
        print()
        #Printing a string and a new line as well as formatting it to also display the variable accumulate2.
        print(f"The total value of the dealer's cards is: {accumulate2}\n")
        #Printing a string and a new line to the display.
        print("The dealer drew over 21. You win!\n")
        #Calling the function restart() and assinging its return value to the variable again.
        again = restart()
        #An if statement that will execute the code below it if the condition again == 'Y' or again == 'y' is true.
        if ((again == 'Y') or (again == 'y')):
            #Calling the function game.
            game()
        #An else keyword that will execute the code below it if the other conditional statement is not true.
        else:
            #Printing a string to the display.
            print("Game has ended.")
    #An elif statement that will execute the code below it if the condition accumulate == accumulate2 is true.
    elif (accumulate == accumulate2):
        #Printing a string to the display and using the end="" statement to prevent the interpreter from printing text on the next line.
        print("The dealer has the cards ", end="")
        #Using a for loop to assign an item from the list in the variable dealercard to the variable i for each iteration.
        for i in dealercard:
            #An if statement that will execute the code below it if the condition i == dealercard[-1] is true.
            if (i == dealercard[-1]):
                #Printing a string and formatting it to also display the variable i.
                print(f"and {i}.")
            #An else keyword that will execute the code below it if the other conditional statement is not true.
            else:
                #Printing a string and formatting it to also display the variable i. In addition, the end="" statement is used to prevent the interpreter from printing text on the next line.
                print(f"{i}, ", end="")
        #Print function.
        print()
        #Printing a string and a new line as well as formatting it to also display the variable accumulate2.
        print(f"The total value of the dealer's cards is: {accumulate2}\n")
        #Printing a string and a new line to the display.
        print("It is a tie!\n")
        #Calling the function restart and assigning its return value to the variable again.
        again = restart()
        #An if statement that will execute the code below it if the condition again == 'Y' or again == 'y' is true.
        if ((again == 'Y') or (again == 'y')):
            #Calling the function game.
            game()
        #An else keyword that will execute the code below it if the other conditional statement is not true.
        else:
            #Printing a string to the display.
            print("Game has ended.")
    #An elif statement that will execute the code below it if the condition accumulate > accumulate2 is true.
    elif (accumulate > accumulate2):
        #Printing a string to the display and using the end="" statement to prevent the interpreter from printing text on the next line.
        print("The dealer has the cards ", end="")
        #Using a for loop to assign an item from the list in the variable dealercard to the variable i for each iteration.
        for i in dealercard:
            #An if statement that will execute the code below it if the condition i == dealercard[-1] is true.
            if (i == dealercard[-1]):
                #Printing a string and formatting it to also display the variable i.
                print(f"and {i}.")
            #An else keyword that will execute the code below it if the other conditional statement is not true.
            else:
                #Printing a string and formatting it to also display the variable i. In addition, the end="" statement is used to prevent the interpreter from printing text on the next line.
                print(f"{i}, ", end="")
        #Print function.
        print()
        #Printing a string and a new line as well as formatting it to also display the variable accumulate2.
        print(f"The total value of the dealer's cards is: {accumulate2}\n")
        #Printing a string to the display and a new line to the display.
        print("The value of your cards is greater than the value of the dealer's cards. You win!\n")
        #Calling the function restart() and assinging its return value to the variable again.
        again = restart()
        #An if statement that will execute the code below it if the condition again == 'Y' or again == 'y' is true.
        if ((again == 'Y') or (again == 'y')):
            #Calling the function game.
            game()
        #An else keyword that will execute the code below it if the other conditional statement is not true.
        else:
            #Printing a string to the display.
            print("Game has ended.")
    #An else keyword that will execute the code below it if the other conditional statements are not true.
    else:
        #Printing a string to the display and using the end="" statement to prevent the interpreter from printing text on the next line.
        print("The dealer has the cards ", end="")
        #Using a for loop to assign an item from the list in the variable dealercard to the variable i for each iteration.
        for i in dealercard:
            #An if statement that will execute the code below it if the condition i == dealercard[-1] is true.
            if (i == dealercard[-1]):
                #Printing a string and formatting it to also display the variable i.
                print(f"and {i}.")
            #An else keyword that will execute the code below it if the other conditional statement is not true.
            else:
                #Printing a string and formatting it to also display the variable i. In addition, the end="" statement is used to prevent the interpreter from printing text on the next line.
                print(f"{i}, ", end="")
        #Print function.
        print()
        #Printing a string and a new line as well as formatting it to also display the variable accumulate2.
        print(f"The total value of the dealer's cards is: {accumulate2}\n")
        #Printing a string to the display and a new line to the display.
        print("The value of your cards is less than the value of the dealer's cards. You lose!\n")
        #Calling the function restart() and assinging its return value to the variable again.
        again = restart()
        #An if statement that will execute the code below it if the condition again == 'Y' or again == 'y is true.
        if ((again == 'Y') or (again == 'y')):
            #Calling the function game.
            game()
        #An else keyword that will execute the code below it if the other conditional statement is not true.
        else:
            #Printing a string to the display.
            print("Game has ended.")

#Defining a function called, draw_cpu without a(any) parameter(s).
def draw_cpu():
    #A while loop that will continuously execute the code below it as long as the condition accumulate2 < 17 is true.
    while (accumulate2 < 17):
        #Using the random.choice method to randomly assign a specific card set as a list to the variable card2.
        card2 = random.choice([two, three, four, five, six, seven, eight, nine, ten, jack, king, queen, ace])
        #A while loop that will continuously execute the code below it as long as the condition card2 == [] is true.
        while (card2 == []):
            #Using the random.choice method to randomly assign a specific card set as a list to the variable card2.
            card2 = random.choice([two, three, four, five, six, seven, eight, nine, ten, jack, king, queen, ace])
        #Using the random.randrange method to randomly assign a number from the range 0 and len(card2) to the variable number2.
        number2 = random.randrange(0,len(card2))
        #Retrieving an integer number in the variable number2 and using the number as an index to retrieve an item from the list in the variable card2. Then, the item is appended to the list in the variable dealercard.
        dealercard.append(card2[number2])
        #Printing a string and a new line as well as formatting to also display an item from the list in the variable card2.
        print(f"The dealer drew a {card2[number2]}\n")
        #Using the pop method to pop out an item from the list in the variable card2.
        card2.pop(number2)
        #Calling the function dealeramount.
        dealeramount()

#Defining a function, called draw_player without a(any) parameter(s).
def draw_player():
    #Globalizing the variable choice so that it can be used outside the function draw_player.
    global choice
    #Assigning the integer number 1 to the variable choice.
    choice = '1'
    #A while loop that will continuously execute the code below it as long as the condition accumulate < 21 is true.
    while (accumulate < 21):
        #An if statement that will execute the code below it if the condition accumulate == 21 is true.
        if (accumulate == 21):
            #Calling the function draw_cpu without an(any) argument(s).
            draw_cpu()
            #A break keyword that will make the interpreter jump out of the while loop.
            break
        #Calling the function hitOrStay() and assigning its return value to the variable choice.
        choice = hitOrStay()
        #An if statement that will execute the code the below it if the condition choice == '1' is true.
        if (choice == '1'):
            #Using the random.choice method to randomly assign a specific card set as a list to the variable card.
            card = random.choice([two, three, four, five, six, seven, eight, nine, ten, jack, king, queen, ace])
            #A while loop that will continuously execute the code below it as long as the condition card == [] is true.
            while (card == []):
                #Using the random.choice method to randomly assign a specific card set as a list to the variable card.
                card = random.choice([two, three, four, five, six, seven, eight, nine, ten, jack, king, queen, ace])
            #Using the random.randrange method to randomly assign a number from the range 0 and len(card) to the variable number.
            number = random.randrange(0,len(card))
            #Retrieving an integer number in the variable number and using the number as an index to retrieve an item from the list in the variable card. Then, the item is appended to the list in the variable usercard.
            usercard.append(card[number])
            #Printing a sring, a new line and an item from the list in the variable card to the display.
            print(f"You drew a {card[number]}.\n")
            #Using the pop method to pop out an item from the list in the variable card.
            card.pop(number)
            #Calling the function useramount without an(any) argument(s).
            useramount()
            #Printing a string and a new line as well as formatting to also display the variable accumulate.
            print(f"The total value of your cards is now: {accumulate}.\n")
        #An elif statement that will execute the code below it if the condition choice == '0'
        elif (choice == '0'):
            #Calling the function draw_cpu without an(any) argument(s).
            draw_cpu()
            #A break keyword that will make the interpreter jump out of the while loop.
            break
        #An else keyword that will execute the code below it if the other condtional statements are not true.
        else:
            #Printing a string and a new line to the display.
            print("Invalid input.\n")
            #A continue keyword that will make the interpreter jump back to the top of the while loop.
            continue

#Defining a function called, restart without a(any) parameter(s).
def restart():
    #Globalizing the variable again so that it can be used outside the function restart.
    global again
    #Retrieving user input and assigning the input value as a string to the variable again.
    again = input("Do you want to play again?(Y/N): ")
    #A while loop that will continuously execute the code below it as long as the condition again != 'Y' and again != 'y' and again != 'N' and again != 'n' is true.
    while (again != 'Y' and again != 'y' and again != 'N' and again != 'n'):
        #Printing a string and a new line to the display.
        print("Invalid input.\n")
        #Retrieving user input and assigning the input value as a string to the variable again.
        again = input("Do you want to play again?(Y/N): ")
    #Returning the content of the variable again.
    return again

#Defining a function called, game without a(any) parameter(s).
def game():
    #Print function.
    print()
    #Printing a string to the display.
    print("Welcome to the Black Jack Game!")
    #Printing 50 asterisks and a new line to the display.
    print("*"*50, "\n")
    #Assigning the integer number 0 to the variable counter.
    counter = 0
    #Globalizing the variable usercard so that it can be used outside the function game.
    global usercard
    #Assigning an empty list to the variable usercard.
    usercard = []
    #Calling the fucntion num without an(any) argument(s).
    num()
    #A while loop that will continuously execute the code below it as long as the condition counter < 2 is true.
    while (counter < 2):
        #Using the random.choice method to randomly assign a specific card set as a list to the variable card.
        card = random.choice([two, three, four, five, six, seven, eight, nine, ten, jack, king, queen, ace])
        #An if statement that will execute the code below it if the condition card == [] is true.
        if (card == []):
            #A continue keyword that will make the interpreter jump back to the top of the while loop.
            continue
        #An else keyword that will execute the code below it if the other conditional statement is not true.
        else:
            #Using the random.randrange method to randomly assign a number from the range 0 and len(card) to the variable number.
            number = random.randrange(0,len(card))
            #Retrieving an integer number in the variable number and using the number as an index to retrieve an item from the list in the variable card. Then, the item is appended to the list in the variable usercard.
            usercard.append(card[number])
            #Using the pop method to pop out an item from the list in the variable card.
            card.pop(number)
            #Assigning the result of counter + 1 to the variable counter.
            counter+=1
    #Assigning the integer number 0 to the variable counter2.
    counter2 = 0
    #Globalizing the variable dealercard so that it can be used outside the function game.
    global dealercard
    #Assigning an empty list to the variable dealercard.
    dealercard = []
    #A while loop that will continuously execute the code below it as long as the condition counter2 < 2 is true.
    while (counter2 < 2):
        #Using the random.choice method to randomly assign a specific card set as a list to the variable card2.
        card2 = random.choice([two, three, four, five, six, seven, eight, nine, ten, jack, king, queen, ace])
        #An if statement that will execute the code below it if the condition card2 == [] is true.
        if (card2 == []):
            #A continue keyword that will make the interpreter jump back to the top of the while loop.
            continue
        #An else keyword that will execute the code below it if the other conditional statement is not true.
        else:
            #An else keyword that will execute the code below it if the other conditional statement is not true.
            number2 = random.randrange(0,len(card2))
            #Retrieving an integer number in the variable number2 and using the number as an index to retrieve an item from the list in the variable card2. Then, the item is appended to the list in the variable dealercard.
            dealercard.append(card2[number2])
            #Using the pop method to pop out an item from the list in the variable card2.
            card2.pop(number2)
            #Assigning the result of counter2 + 1 to the variable counter2.
            counter2+=1

    #Printing a string and a new line as well as formatting it to also display the first item in the list in the variable dealercard.
    print(f"The dealer drew two cards for itself. One card is face up and the other is face down. The face up card is the {dealercard[0]}.\n")
    #Printing a string and two new lines as well as formatting to also display the first and second items in the list in the variable usercard.
    print(f"The dealer deals two cards for you.\n\nYou have the cards {usercard[0]} and {usercard[1]}.\n")

    #Calling the function useramount without an(any) argument(s).
    useramount()
    #Calling the function dealeramount without an(any) argument(s).
    dealeramount()
    #Printing a string and a new line as well as formatting it to also display the variable accumulate.
    print(f"The total value of your cards is: {accumulate}.\n")
    #Calling the function draw_player without an(any) argument(s).
    draw_player()
    #An if statement that will execute the code below it if the condition accumulate > 21 is true.
    if (accumulate > 21):
        #Priting a string and new line to the display.
        print("You drew over 21 first. You lose!\n")
        #Calling the function restart() and assigning its return value to the variable again.
        again = restart()
        #An if statement that will execute the code below it if the condition again == 'Y' or again == 'y is true.
        if ((again == 'Y') or (again == 'y')):
            #Calling the function game without an(any) argument(s).
            game()
        #An else keyword that will execute the code below it if the other conditional statement is not true.
        else:
            #Printing a string to the display.
            print("Game has ended.")
    #An else keyword that will execute the code below it if the other conditional statement is not true.
    else:
        #Calling the function winOrLose without an(any) argument(s).
        winOrLose()
#Calling the function game without an(any) argument(s).
game()
