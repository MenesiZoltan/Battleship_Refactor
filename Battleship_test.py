import os


def generate_game_board():
    table = [["_" for x in range(10)]for y in range(10)]
    return table


def request_player_input():
    available_inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    player_input = input()
    while player_input not in available_inputs:
        print("Invalid input, please try again: ") 
        player_input = input()
    player_input = int(player_input)
    return player_input

def coordinate_is_available(x_coordinate, y_coordinate, board):
    if board[x_coordinate - 1][y_coordinate - 1] == "\u23CF":
        return False
    if board[x_coordinate - 1][y_coordinate - 1] == "_":
        return True

def request_player_ships(board, ship_length, ship_number):
    while ship_number > 0:
        os.system("clear")
        print_ship_placement_turn(ship_length, ship_number)
        for x in board:
            print(x)
        ship_block_counter = 0
        is_input_ok = False
        #Will try to put 32-42 into a separate function
        while is_input_ok == False:
            print("Please enter row coordinate:")
            row_number = request_player_input()
            print("Please enter column coordinate:")
            column_number = request_player_input()
            if coordinate_is_available(row_number, column_number, board) == True:
                print("ok")
                is_input_ok = True
            else:
                print("not ok, enter new")
        if ship_length > 1:
            direction_of_ship = input("Please enter direction of ship - up, down, left, right: ")
            if direction_of_ship == "up":
                for x in range(0, ship_length):
                    board[(row_number - 1) - ship_block_counter][column_number - 1] = "\u23CF"
                    ship_block_counter += 1
                ship_number -= 1
            if direction_of_ship == "down":
                for x in range(0, ship_length):
                    board[(row_number - 1) + ship_block_counter][column_number - 1] = "\u23CF"
                    ship_block_counter += 1
                ship_number -= 1
            if direction_of_ship == "left":
                for x in range(0, ship_length):
                    board[row_number -1 ][(column_number - 1) - ship_block_counter] = "\u23CF"
                    ship_block_counter += 1
                ship_number -= 1
            if direction_of_ship == "right":
                for x in range(0, ship_length):
                    board[row_number -1 ][(column_number - 1) + ship_block_counter] = "\u23CF"
                    ship_block_counter += 1
                ship_number -= 1
        else:
            board[row_number - 1][column_number - 1] = "\u23CF"
            ship_number -= 1
    os.system("clear")


def print_ship_placement_turn(ship_length, ship_number):
    if ship_length == 1:
        print("Placing Gunboats - Max 4, length 1.")
        print("Ships remaining: " + str(ship_number))
        ship_number -= 1
    if ship_length == 2:
        print("Placing Destroyers - Max 3, length 2.")
        print("Ships remaining: " + str(ship_number))
        ship_number -= 1
    if ship_length == 3:
        print("Placing Cruisers - Max 2, length 3.")
        print("Ships remaining: " + str(ship_number))
        ship_number -= 1
    if ship_length == 4:
        print("placing Carrier - Max 1, length 4")
        print("Ships remaining: " + str(ship_number))
        ship_number -= 1


def fire_at_coordinate(board, enemy_board):
    row_number = int(input("row coordinate for fire: "))
    column_number = int(input("column coordinate for fire: "))
    if enemy_board[row_number - 1][column_number -1] == "\u23CF":
        board[row_number - 1][column_number - 1] = "A"
    else:    
        board[row_number - 1][column_number - 1] = "\u2716"
    enemy_board[row_number - 1][column_number - 1] = "X"
    os.system("clear")


def player_boards(tracker, board):
    print("Fires shot so far at:\n")
    for x in tracker:
        print(x)
    print("\n")
    print("Your board\n")
    for y in board:
        print(y)
    print("\n")


def win_condition(player_board):
    for x in player_board:
        for y in x:
            if "\u23CF" in x:
                return False
    return True


def main():
    #Variables
    number_of_ships = [4, 3, 2, 1]
    length_of_ships = [1, 2, 3, 4]
    #Generate game board and trackers
    game_board_p1 = generate_game_board()
    game_board_p2 = generate_game_board()
    player1_tracker = generate_game_board()
    player2_tracker = generate_game_board()
    #Add ships for both players, need to improve further

    """row_coordinate = request_player_input()
    column_coordinate = request_player_input()
    print(row_coordinate)
    print(column_coordinate)
    """
    for x in range(4):
        request_player_ships(game_board_p1, length_of_ships[x], number_of_ships[x])
    for x in range(4):
        request_player_ships(game_board_p2, length_of_ships[x], number_of_ships[x])

    #Players taking turns, tracking shots fired and received, Win Condition checks if any ships are remaining in opponets game board.
    #Exit when win condition is met.
    while True:
        print("Player 1 turn:")
        player_boards(player1_tracker, game_board_p1)
        fire_at_coordinate(player1_tracker, game_board_p2)
        if win_condition(game_board_p2) == True:
            print("Player 1 won!")
            exit()
        print("Player 2 turn:")
        player_boards(player2_tracker, game_board_p2)
        fire_at_coordinate(player2_tracker, game_board_p1)
        if win_condition(game_board_p1) == True:
            print("Player 2 won!")
            exit()

main()