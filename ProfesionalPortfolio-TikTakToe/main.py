
tic_tac_toe = f"""

    1  |   2    |  3
 _ _ _ _ _ _ _ _ _ _ _
    4  |   5    |  6
 _ _ _ _ _ _ _ _ _ _ _
    7  |   8    |  9
       
 """
check = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]

print("Welcome to Tic/Tac/Toe ")
print(f"Here is the Dashboard, the numbers are the position for your move{tic_tac_toe}")

answer = input("Which player do you want to be?  1 (X) or 2 (O): ")

continue_playing = True


def check_winning_Horizontal():
    global continue_playing
    try:
        if check[0] + check[1] + check[2] == "XXX":
            continue_playing = False
            print("Player X Win")

        elif check[3] + check[4] + check[5] == "XXX":
            continue_playing = False
            print("Player X Win")

        elif check[6] + check[7] + check[8] == "XXX":
            continue_playing = False
            print("Player X Win")
    except TypeError:
        pass


def check_winning_Vertical():
    global continue_playing
    try:
        if check[0] + check[3] + check[6] == "XXX":
            continue_playing = False
            print("Player X Win")

        elif check[1] + check[4] + check[7] == "XXX":
            continue_playing = False
            print("Player X Win")

        elif check[2] + check[5] + check[8] == "XXX":
            continue_playing = False
            print("Player X Win")
    except TypeError:
        pass


def check_winning_diagonal():
    global continue_playing
    try:
        if check[0] + check[4] + check[8] == "XXX":
            continue_playing = False
            print("Player X Win")
        elif check[2] + check[4] + check[6] == "XXX":
            continue_playing = False
            print("Player X Win")
    except TypeError:
        pass


def check_x_winning():
    check_winning_Horizontal()
    check_winning_Vertical()
    check_winning_diagonal()


def check_winning_Horizontal_O():
    global continue_playing
    try:
        if check[0] + check[1] + check[2] == 0:
            continue_playing = False
            print("Player O Win")

        elif check[3] + check[4] + check[5] == 0:
            continue_playing = False
            print("Player O Win")

        elif check[6] + check[7] + check[8] == 0:
            continue_playing = False
            print("Player O Win")

    except TypeError:
        pass


def check_winning_Vertical_O():
    global continue_playing
    try:
        if check[0] + check[3] + check[6] == 0:
            continue_playing = False
            print("Player O Win")

        elif check[1] + check[4] + check[7] == 0:
            continue_playing = False
            print("Player O Win")

        elif check[2] + check[5] + check[8] == 0:
            continue_playing = False
            print("Player O Win")

    except TypeError:
        pass


def check_winning_diagonal_O():
    global continue_playing
    try:
        if check[0] + check[4] + check[8] == 0:
            continue_playing = False
            print("Player O Win")
        elif check[2] + check[4] + check[6] == 0:
            continue_playing = False
            print("Player O Win")
    except TypeError:
        pass


def check_O_winning():
    check_winning_Horizontal_O()
    check_winning_Vertical_O()
    check_winning_diagonal_O()


def player_X():
    global tic_tac_toe
    move = input("Player 1: Your move? type a number: ")
    tic_tac_toe = tic_tac_toe.replace(move, "X")
    check[int(move) - 1] = "X"
    print(tic_tac_toe)
    check_x_winning()


def player_O():
    global tic_tac_toe
    move_player2 = input("Player 2 : Your move?: ")
    tic_tac_toe = tic_tac_toe.replace(move_player2, "O")
    check[int(move_player2) - 1] = 0
    print(tic_tac_toe)
    check_O_winning()


is_a_draw = 0

while continue_playing:
    if answer == "1" and continue_playing == True:
        player_X()
        is_a_draw += 1
        if is_a_draw == 9 and continue_playing == True:
            print("is a draw")
            continue_playing = False
        if continue_playing:
            player_O()
            check_winning_Horizontal_O()
            check_winning_Vertical_O()
            check_winning_diagonal_O()
            is_a_draw += 1
            if is_a_draw == 9 and continue_playing == True:
                print("is a draw")
                continue_playing = False


    else:
        player_O()
        is_a_draw += 1
        if is_a_draw == 9 and continue_playing == True:
            print("is a draw")
            continue_playing = False
        if continue_playing:
            player_X()
            check_winning_Horizontal()
            check_winning_Vertical()
            check_winning_diagonal()
            is_a_draw += 1
            if is_a_draw == 9 and continue_playing == True:
                print("is a draw")
                continue_playing = False



