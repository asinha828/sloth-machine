import random

MAX_LINES = 5
MAX_BET = 10000
MIN_BET = 500

ROWS = 5
COLS = 5

symbol_count = {
    "A": 5,
    "B": 7,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(coloumns, lines, bet, values):
    win = 0
    winning_lines = []
    for line in range(lines):
        symbol = coloumns[0][line]
        for coloumn in coloumns:
            symbol_to_check = coloumn[line]
            if symbol != symbol_to_check:
                break
        else:
            win += values[symbol] * bet
            winning_lines.append(line + 1)
    return win


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, sym_cnt in symbols.items():  # gives both the keys and values
        for _ in range(sym_cnt):
            all_symbols.append(symbol)

    # what values will go with every single coloumns
    coloumns = []  # defining coloumns list
    for col in range(cols):
        coloumn = []
        current_symbols = all_symbols[:]
        for row in range(rows):  # rows ==coloums
            value = random.choice(current_symbols)
            current_symbols.remove(value)  # remove the picked random value so we dont pic it again
            coloumn.append(value)
        coloumns.append(col)
    return coloumns


def print_slots_machine(coloumns):
    for row in range(len(coloumns[0])):  # no of rows in each of our coloumns
        for i, coloumn in enumerate(coloumns):
            if i != len(coloumns) - 1:  # max index we have to access a elemnet in coloum list
                print(coloumn[row], end="|")
            else:
                print(coloumn[row], end=" ")
        print()


def deposit():  # collecting user input that gets deposit
    while True:  # it will tell the user to give the amount until it is a valid input
        amount = input("what would you like to deposit? $")
        if amount.isdigit():  # if it's a valid input (might be a whole number) no negavtive
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please print the number")
    return amount


def get_no_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid no of lines")
        else:
            print("Please print the number")
    return lines


def get_bet():
    while True:
        amount = input("How much do you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please print the number")
    return amount


def spin(balance):
    lines = get_no_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet the amount , your current balance is ${balance}")
        else:
            break
    print(f"you are betting  ${bet} on  {lines} lines. Total bet is equal to : ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slots_machine(slots)
    Win, winning_lines = check_winnings(slots, lines, bet, symbol_value)  # type: ignore
    print(f"YOU WON ${Win}.")
    print(f"you won on lines: ", *winning_lines)
    return Win - total_bet


def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        an = input("Press enter to play (q to quit).")
        if an == "q":
            break
    print("you left with ${balance}")