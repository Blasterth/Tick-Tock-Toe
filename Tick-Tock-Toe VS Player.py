print("Welcome to Tick-Tock-Toe.    Copyright (c) 2022 Parsa Aryan")
print("Please set the Caps Lock to On.")

row1 = [1,2,3]
row2 = [4,5,6]
row3 = [7,8,9]
column1 = [1,4,7]
column2 = [2,5,8]
column3 = [3,6,9]
slope1 = [1,5,9]
slope2 = [3,5,7]

ways_to_win = [row1,row2,row3,column1,column2,column3,slope1,slope2]

row1_empty_spaces = [0,0,0]
row2_empty_spaces = [0,0,0]
row3_empty_spaces = [0,0,0]

global game_over
game_over = False

global turn_number
turn_number = 1


def player_confirm(desired_letter = str):
    letter = desired_letter
    player_confirmation = input(f"Player {letter}, please confirm your presense by typing {letter}.")

    if len(player_confirmation) == 0:
        print("No input entered!")
        player_confirm(letter)

    elif player_confirmation[0] == letter:
        print(f"Welcome, Player {letter}")

    else:
        print("Command not recognized.")
        player_confirm(letter)


player_confirm("X")
player_confirm("O")


def display():
    for item1, item2, item3 in row1, row2, row3:
        print(f"{item1},{item2},{item3}")


def empty_spaces_display():
    for item1, item2, item3 in row1_empty_spaces, row2_empty_spaces, row3_empty_spaces:
        print(f"{item1},{item2},{item3}")


def player_turn(desired_letter = str):
    letter = desired_letter
    player_choice = input(f"Please input your letter in your desired space.")

    if len(player_choice) == 0:
        print("No input entered!")
        player_turn(letter)

    elif player_choice.isnumeric() == True:
        player_choice = player_choice[0]
        player_choice = int(player_choice)

        if player_choice in range(1,10):


            def one_to_three():

                if player_choice in range(1,4):

                    if row1[player_choice - 1] == ("X" or "O"):
                        print("Sorry, this space is occupied.\nPlease try another one.")
                        player_turn(letter)

                    else:
                        row1[player_choice - 1] = letter
                        row1_empty_spaces[player_choice - 1] = "|"

                        if player_choice % 3 == 2:
                            column1[0] = letter

                        elif player_choice % 3 == 1:
                            column2[0] = letter

                        elif player_choice % 3 == 0:
                            column3[0] = letter

                        if (player_choice - 1) % 4 == 0:
                            slope1[0] = letter

                        elif (player_choice - 1) % 4 == 2:
                            slope2[0] = letter


            def four_to_six():

                if player_choice in range(4,7):

                    if row2[player_choice - 4] == ("X" or "O"):
                        print("Sorry, this space is occupied.\nPlease try another one.")
                        player_turn(letter)

                    else:
                        row2[player_choice - 4] = letter
                        row2_empty_spaces[player_choice - 4] = "|"
                        
                        if player_choice % 3 == 2:
                            column1[1] = letter

                        elif player_choice % 3 == 1:
                            column2[1] = letter

                        elif player_choice % 3 == 0:
                            column3[1] = letter

                        if (player_choice - 1) % 4 == 0:
                            slope1[1] = letter
                            slope2[1] = letter

                        else:
                            pass


            def seven_to_nine():

                if player_choice in range(7,10):

                    if row3[player_choice - 7] == ("X" or "O"):
                        print("Sorry, this space is occupied.\nPlease try another one.")
                        player_turn(letter)

                    else:
                        row3[player_choice - 7] = letter
                        row3_empty_spaces[player_choice - 7] = "|"
                        
                        if player_choice % 3 == 2:
                            column1[2] = letter

                        elif player_choice % 3 == 1:
                            column2[2] = letter

                        elif player_choice % 3 == 0:
                            column3[2] = letter

                        if (player_choice - 7) % 4 == 0:
                            slope1[0] = letter

                        elif (player_choice - 7) % 4 == 2:
                            slope2[0] = letter


            one_to_three()
            four_to_six()
            seven_to_nine()

            global turn_number
            turn_number += 1

        elif player_choice == 0:
                empty_spaces_display()
                input("Please input something to progress.")
                player_turn(letter)

    else:
        print("Command not recognized.")
        player_turn(letter)


def winner_check(ways_to_win):

    for item1,item2,item3 in ways_to_win:

        if item1 == item2 and item2 == item3:

            if item1 == "X":
                print("Player X Wins!")
                global game_over
                game_over = True

            elif item1 == "O":
                print("Player O Wins!")
                game_over = True
    
    display()


def space_cleaner():
    global game_over
    game_over = False
    global turn_number
    turn_number = 1
    global row1
    row1 = [1,2,3]
    global row2
    row2 = [4,5,6]
    global row3
    row3 = [7,8,9]
    global column1
    column1 = [1,4,7]
    global column2
    column2 = [2,5,8]
    global column3
    column3 = [3,6,9]
    global slope1
    slope1 = [1,5,9]
    global slope2
    slope2 = [3,5,7]
    global ways_to_win
    ways_to_win = [row1,row2,row3,column1,column2,column3,slope1,slope2]
    global row1_empty_spaces
    row1_empty_spaces = [0,0,0]
    global row2_empty_spaces
    row2_empty_spaces = [0,0,0]
    global row3_empty_spaces
    row3_empty_spaces = [0,0,0]


def replay():
    replay_confirmation = input("Do you wish to replay? (Y/N)")

    if len(replay_confirmation) == 0:
        print("No input entered!")
        replay()

    elif replay_confirmation[0] == "Y":
        player_confirm("X")
        player_confirm("O")
        space_cleaner()
        two_player_mode()

    elif replay_confirmation[0] == "N":
            input()
            exit()

    else:
        print("Command not recognized.")
        replay()


def two_player_mode():
    global game_over

    while game_over == False and turn_number <= 9:

        if turn_number % 2 == 1:
            print("Player X")
            print(f"Turn: {turn_number}")
            display()
            player_turn("X")
            winner_check(ways_to_win)

        elif turn_number % 2 == 0:
            print("Player O")
            print(f"Turn: {turn_number}")
            display()
            player_turn("O")
            winner_check(ways_to_win)

    if game_over == False and turn_number == 9:
        game_over = True
        display()
        print("It's a Draw!")

    replay()


two_player_mode()