print("Welcome to the NEW Tick-Tock-Toe. Copyright (c) 2022 Parsa Aryan")
print("No need to set the Caps Lock to On anymore.")


game_over = False
turn_number = 1
empty_space_character = "8"
table = []

#The number of ways in which a person has won the game
victories = 0

#Commonly used Messages (Note: There are no CONSTANTS in Python)
EMPTY_INPUT_ERROR_MESSAGE = "No input entered!"
BAD_INPUT_ERROR_MESSAGE = "Command not recognized!"
OUT_OF_RANGE_ERROR_MESSAGE = "Out of range!"
SINGLE_VICTORY_MESSAGE = "---SINGLE VICTORY---"
DOUBLE_VICTORY_MESSAGE = "---DOUBLE VICTORY---"
TRIPLE_VICTORY_MESSAGE = "---TRIPLE VICTORY---"
SPIDER_VICTORY_MESSAGE = "---SPIDER VICTORY---"


#Takes input for table size; limitations are for avoiding crazy stuff, like 1000x1000 tables
def table_size_select():
    player_desired_table_size = input("Please enter your desired table size from 3-20.")
    if len(player_desired_table_size) == 0:
        print(EMPTY_INPUT_ERROR_MESSAGE)
        table_size_select()
    elif player_desired_table_size.isnumeric() == True:
        if int(player_desired_table_size) >= 3 and int(player_desired_table_size) <= 20:
            global table_size
            table_size = int(player_desired_table_size)
        else:
            print(OUT_OF_RANGE_ERROR_MESSAGE)
            table_size_select()
    else:
        print(BAD_INPUT_ERROR_MESSAGE)
        table_size_select()
    return f"The table size is: {table_size}x{table_size}"


table_size_selection = table_size_select()
print(table_size_selection)

#Table creator
def table_creator():
    table_x = table_size
    table_y = table_size
    global table
    table = [empty_space_character] * table_x #if table_size==3 >>table=["0","0","0"]
    for n in range (table_x): table[n] = [empty_space_character] * table_y #>>table=[["0","0","0"],["0","0","0"],["0","0","0"]]


table_creator()


#Displays the table
def display():
    display_line = "-"
    display_content = "|"
    for n in range(table_size):
        display_line = display_line + " - -"
    print(display_line)
    for n in range(table_size):
        display_content = table[n]
        display_content = str(display_content)
        display_content = display_content.replace("[","| ")
        display_content = display_content.replace(", "," | ")
        display_content = display_content.replace("]"," |")
        display_content = display_content.replace("'","")
        print(display_content)
        print(display_line)


#Checks victory by clearing a row (-)
def row_winner_check():
    rows_to_check = list()
    for l in range(table_size):
        for m in range(table_size):
            rows_to_check.append(table[l][m])
        if rows_to_check.count(rows_to_check[0]) == len(rows_to_check) and rows_to_check[0] != empty_space_character:
            print(f"{rows_to_check[0]} CLEARS ROW {l + 1}.")
            global victories
            victories += 1
            if victories == 1:
                print(SINGLE_VICTORY_MESSAGE)
                global game_over
                game_over = True
            break
        else:
            rows_to_check.clear()


#Checks victory by clearing a column (|)
def column_winner_check():
    columns_to_check = list()
    for l in range(table_size):
        for m in range(table_size):
            columns_to_check.append(table[m][l])
        if columns_to_check.count(columns_to_check[0]) == len(columns_to_check) and columns_to_check[0] != empty_space_character:
            print(f"{columns_to_check[0]} CLEARS COLUMN {l + 1}.")
            global victories
            victories += 1
            if victories == 1:
                print(SINGLE_VICTORY_MESSAGE)
                global game_over
                game_over = True
            elif victories == 2:
                print(DOUBLE_VICTORY_MESSAGE)
            break
        else:
            columns_to_check.clear()



#Checks victory by clearing the slash (/)
def slash_winner_check():
    slash = list()
    for n in range(table_size):
        slash.append(table[n][-(n+1)])
    if slash.count(slash[0]) == len(slash) and slash[0] != empty_space_character:
        print(f"{slash[0]} ACHEIVES A SLASH VICTORY.")
        global victories
        victories += 1
        if victories == 1:
            print(SINGLE_VICTORY_MESSAGE)
            global game_over
            game_over = True
        elif victories == 2:
            print(DOUBLE_VICTORY_MESSAGE)
        elif victories == 3:
            print(TRIPLE_VICTORY_MESSAGE)
    else:
        pass


#Checks victory by clearing the backslash (\)
def backslash_winner_check():
    backslash = list()
    for n in range(table_size):
        backslash.append(table[n][n])
    if backslash.count(backslash[0]) == len(backslash) and backslash[0] != empty_space_character:
        print(f"{backslash[0]} ACHEIVES A BACKSLASH VICTORY.")
        global victories
        victories += 1
        if victories == 1:
            print(SINGLE_VICTORY_MESSAGE)
            global game_over
            game_over = True 
        elif victories == 2:
            print(DOUBLE_VICTORY_MESSAGE)
        elif victories == 3:
            print(TRIPLE_VICTORY_MESSAGE)
        elif victories == 4:
            print(SPIDER_VICTORY_MESSAGE)
    else:
        pass


#Fills the spaces; called in player_turn function
def space_filler(four_digit_location=str(),letter=str()):
    row_number = int(four_digit_location[0:2])
    column_number = int(four_digit_location[2:4])
    if table[row_number - 1][column_number - 1] in ["X","O"]:
        print("Sorry. Already picked up. Choose another one.")
        player_turn(letter)
    else:
        table[row_number - 1][column_number - 1] = letter
        global turn_number
        turn_number += 1


#Takes the input for the desired space and sends it to space_filler function
def player_turn(desired_letter=str()):
    desired_letter_backup = desired_letter
    print("Please enter a 4-digit number, the first two the row, the second two the column.")
    print("For example: 2001 means row 20, column 01")
    target_location = input()
    if len(target_location) == 0:
        print(EMPTY_INPUT_ERROR_MESSAGE)
        player_turn(desired_letter_backup)
    elif len(target_location) == 4:
        if target_location.isnumeric() == True:
            if int(target_location[0:2]) > table_size or int(target_location[2:4]) > table_size:
                print(OUT_OF_RANGE_ERROR_MESSAGE)
            else:
                space_filler(target_location,desired_letter_backup)
        else:
            print("Only NUMBERS, please.")
            player_turn(desired_letter_backup)
    elif len(target_location) != 0 and len(target_location) != 4:
        print(OUT_OF_RANGE_ERROR_MESSAGE)
        player_turn(desired_letter_backup)
    else:
        print(BAD_INPUT_ERROR_MESSAGE)
        player_turn(desired_letter_backup)


#Resets the values to the original ones
def restarter():
    global game_over
    game_over = False
    global turn_number
    turn_number = 1
    global victories
    victories = 0
    global table
    table.clear()
    global table_size 
    table_size = 3
    table_size_selection = table_size_select()
    print(table_size_selection)
    table_creator()


#Replay options; called in two_player_mode function
def replay():
    global table_size
    table_size
    display()
    replay_confirmation = input("Do you wish to replay? (Y/N)").upper()

    if len(replay_confirmation) == 0:
        print("No input entered!")
        replay()

    elif replay_confirmation[0] == "Y":
        restarter()

    elif replay_confirmation[0] == "N":
            input()
            exit()

    else:
        print("Command not recognized.")
        replay()


#Does the main stuff
def two_player_mode():
    global game_over

    while game_over == False and turn_number <= (table_size ** 2):

        if turn_number % 2 == 1:
            print(f"Player X")
            print(f"Turn: {turn_number}")
            display()
            player_turn("X")
            row_winner_check()
            column_winner_check()
            slash_winner_check()
            backslash_winner_check()

        elif turn_number % 2 == 0:
            print(f"Player O")
            print(f"Turn: {turn_number}")
            display()
            player_turn("O")
            row_winner_check()
            column_winner_check()
            slash_winner_check()
            backslash_winner_check()

    if game_over == False and turn_number == (table_size ** 2):
        game_over = True
        display()
        print("It's a Draw!")

    replay()
    two_player_mode()


two_player_mode()