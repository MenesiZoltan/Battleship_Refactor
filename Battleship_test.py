import os


def generate_game_board(size):
    table = [["_" for x in range(size)]for y in range(size)]
    return table


def request_player_ships(board, ship_length, ship_number):
    while ship_number > 0:
        os.system("clear")
        print_ship_placement_turn(ship_length, ship_number)
        for x in board:
            print(x)
        ship_block_counter = 0
        row_number = int(input("Please enter row: "))
        column_number = int(input("Please enter column: "))
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
    return board

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
    board[row_number - 1][column_number - 1] = "\u2716"
    enemy_board[row_number - 1][column_number - 1] = "X"
    os.system("clear")
    return board


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
    board_size = 10
    number_of_gunboats = 4
    length_of_gunboats = 1
    number_of_destroyers = 3
    length_of_destroyers = 2
    number_of_cruisers = 2
    length_of_cruisers = 3
    number_of_carriers = 1
    length_of_carriers = 4
    #Generate game board and trackers
    game_board_p1 = generate_game_board(board_size)
    game_board_p2 = generate_game_board(board_size)
    player1_tracker = generate_game_board(board_size)
    player2_tracker = generate_game_board(board_size)
    #Add ships for both players, need to improve further
    player1_board = request_player_ships(game_board_p1, length_of_gunboats, number_of_gunboats)
    #player1_board = request_player_ships(game_board_p1, length_of_destroyers, number_of_destroyers)
    #player1_board = request_player_ships(game_board_p1, length_of_cruisers, number_of_cruisers)
    #player1_board = request_player_ships(game_board_p1, length_of_carriers, number_of_carriers)

    player2_board = request_player_ships(game_board_p2, length_of_gunboats, number_of_gunboats)
    #player2_board = request_player_ships(game_board_p2, length_of_destroyers, number_of_destroyers)
    #player2_board = request_player_ships(game_board_p2, length_of_cruisers, number_of_cruisers)
    #player2_board = request_player_ships(game_board_p2, length_of_carriers, number_of_carriers)
    #Players taking turns, tracking shots fired and received, Win Condition checks if any ships are remaining in opponets game board.
    #Exit when win condition is met.
    while True:
        print("Player 1 turn:")
        player_boards(player1_tracker, player1_board)
        fire_at_coordinate(player1_tracker, player2_board)
        if win_condition(player2_board) == True:
            print("Player 1 won!")
            exit()
        print("Player 2 turn:")
        player_boards(player2_tracker, player2_board)
        fire_at_coordinate(player2_tracker, player1_board)
        if win_condition(player1_board) == True:
            print("Player 2 won!")
            exit()

main()