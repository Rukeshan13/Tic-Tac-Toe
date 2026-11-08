brd = ["1","2,","3",
       "4","5","6",
       "7","8","9"]
plys = {
    "X" : "Player_1",
    "O" : "Player_2"
}

win_combinations=(
    (0,1,2),
    (3,4,5),
    (6,7,8),
    (0,3,6),
    (1,4,7),
    (2,5,8),
    (0,4,8),
    (2,4,6)
)
occupied = set()

def Dis_brd():
    print()
    print(brd[0],"|", brd[1],"|", brd[2])
    print("--+---+--")
    print(brd[3],"|", brd[4],"|", brd[5])
    print("--+---+--")
    print(brd[6],"|", brd[7],"|", brd[8])
    print()

def check_winner(symbol):
    for combination in win_combinations:
        if all(brd[position] == symbol for position in combination):
            return True
        return False

def make_move(symbol):
    while True:
        choice = input(
            f"{plys[symbol]} ({symbol}), choose a position (1 to 9):"
        )    
        if not choice.isdigit():
            print("Please enter a valid number.")
            continue
        position = int(choice) - 1

        if position < 0 or position > 8:
            print("Please choose a position btw 1 to 9.")
            continue
        if position in occupied:
            print("This position is already occuiped.")
            continue
        brd[position] = symbol
        occupied.add(position)
        break
print("Welcome to the Game of TTT..")
current_player = "X"
while True:
    Dis_brd()

    make_move(current_player)

    if check_winner(current_player):
        Dis_brd()
        print(plys[current_player], "Wins!..")
        break
    if len(occupied) == 9:
        Dis_brd()
        print("Thats A Draw.")
        break
    current_player = "O" if current_player == "X" else "X"

print("\nThanks for playing.")

