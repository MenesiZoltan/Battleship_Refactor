import os


def generate_game_board():
    table = [["_" for x in range(10)]for y in range(10)]
    return table


def print_board(board_ID):
    row_name = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    print("    | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10|")
    print("–" * 45)
    for i in range(10):
        print("  %s | " %(row_name[i]) + "{} | {} | {} | {} | {} | {} | {} | {} | {} | {} |".format(board_ID[i][0], board_ID[i][1], board_ID[i][2], board_ID[i][3], board_ID[i][4], board_ID[i][5], board_ID[i][6], board_ID[i][7], board_ID[i][8], board_ID[i][9]))
        print("–" * 45)


def request_player_input():
    available_inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    player_input = input()
    while player_input not in available_inputs:
        print("Invalid input, please try again(COOrDINATE): ") 
        player_input = input()
    player_input = int(player_input)
    return player_input


def coordinate_is_available(x_coordinate, y_coordinate, board):
    if board[x_coordinate - 1][y_coordinate - 1] == "\u23CF":
        return False
    if board[x_coordinate - 1][y_coordinate - 1] == "_":
        return True

def check_if_ship_is_outside_of_game_board_left_or_up(row_number, column_number, ship_length):
     if ship_length > 1:
        direction_of_ship = input("Please enter direction of ship - up, down, left, right: ")
        if direction_of_ship == "up":
            if row_number - ship_length < 0:
                raise IndexError
            return direction_of_ship
        if direction_of_ship == "left":
            if column_number - ship_length < 0:
                raise IndexError
            return direction_of_ship
        return direction_of_ship


def input_check_function(board, ship_length):
    is_input_ok = False
    while is_input_ok == False:
        print("Please enter row coordinate:")
        x_coordinate = request_player_input()
        print("Please enter column coordinate:")
        y_coordinate = request_player_input()
        if coordinate_is_available(x_coordinate, y_coordinate, board) == True:
            is_input_ok = True
        else:
            print("Ship Starting coordinate already taken, please enter another one.")
        
    input_list = [x_coordinate, y_coordinate]  
    return input_list


def print_ship_placement_turn(ship_length, ship_number):
    for i in range(4):
        if ship_length == i + 1:
            print("Placing Gunboats - Max %d, length %d." %(4 - i, i + 1))
            print("Ships remaining: " + str(ship_number))
            ship_number -= 1


def request_player_ships(board, ship_length, ship_number):
    while ship_number > 0:
        try:
            os.system("clear")
            print_ship_placement_turn(ship_length, ship_number)
            # for x in board:
                # print(x)
            print_board(board)
            ship_block_counter = 0
            input_list = input_check_function(board, ship_length)
            row_number = input_list[0]
            column_number = input_list[1]
            direction_of_ship = check_if_ship_is_outside_of_game_board_left_or_up(row_number, column_number, ship_length)
            if ship_length > 1:
                if direction_of_ship == "up":
                    for x in range(0, ship_length):
                        board[(row_number - 1) + ship_block_counter - (ship_length - 1)][column_number - 1] = "\u23CF"
                        ship_block_counter += 1
                if direction_of_ship == "down":
                    for x in range(0, ship_length):
                        board[(row_number - 1) - ship_block_counter + (ship_length - 1)][column_number - 1] = "\u23CF"
                        ship_block_counter += 1
                if direction_of_ship == "left":
                    for x in range(0, ship_length):
                        board[row_number -1 ][(column_number - 1) + ship_block_counter - (ship_length - 1)] = "\u23CF"
                        ship_block_counter += 1
                if direction_of_ship == "right":
                    for x in range(0, ship_length):
                        board[row_number -1 ][(column_number - 1) - ship_block_counter + (ship_length - 1)] = "\u23CF"
                        ship_block_counter += 1
            else:
                board[row_number - 1][column_number - 1] = "\u23CF"
            ship_number -= 1
        except IndexError:
            print("Invalid placement. Please add new coordinates and direction.")
    os.system("clear")


def player_boards(tracker, board):
    print("Fires shot so far at:\n")
    # for x in tracker:
        # print(x)
    print_board(tracker)
    print("\n")
    print("Your board\n")
    # for y in board:
        # print(y)
    print_board(board)
    print("\n")


def fire_at_coordinate(board, enemy_board):
    row_number = int(input("row coordinate for fire: "))
    column_number = int(input("column coordinate for fire: "))
    if enemy_board[row_number - 1][column_number -1] == "\u23CF":
        board[row_number - 1][column_number - 1] = "A"
    else:    
        board[row_number - 1][column_number - 1] = "\u2716"
    enemy_board[row_number - 1][column_number - 1] = "X"
    os.system("clear")


def win_condition(player_board):
    for x in player_board:
        for y in x:
            if "\u23CF" in x:
                return False
    return True


def main():
    number_of_ships = [4, 3, 2, 1]
    length_of_ships = [1, 2, 3, 4]
    game_board_p1 = generate_game_board()
    game_board_p2 = generate_game_board()
    player1_tracker = generate_game_board()
    player2_tracker = generate_game_board()
    for x in range(3):
        request_player_ships(game_board_p1, length_of_ships[x], number_of_ships[x])
    for x in range(3):
        request_player_ships(game_board_p2, length_of_ships[x], number_of_ships[x])
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

if __name__ == "__main__":
    main()