import random
import sys
import time


def print_horses(horses):
    print("Horses:\t\tOdds:\n")
    for horse in horses.keys():
        print(f"{horse:15} {horses[horse]:.1f}")


def betting_on_horse(horses):
    betting_is_on = True
    while betting_is_on:
        try:
            bet = input("Which horse you wanna bet on? ")
            bet = str(bet)
            if bet in horses.keys():
                print("You bet on: " + bet)
                return bet
            else:
                print("Try again homie, this is not right!")
        except(ValueError, TypeError):
            print("This is not a number at all.")


def betting_cash_amount(money):
    betting_is_on = True
    while betting_is_on:
        print("Available money: " + str(money))
        try:
            bet_amount = input("How much you wanna bet? ")
            bet_amount = int(bet_amount)
            if bet_amount > money:
                print("Not enough money to bet!")
            else:
                money -= bet_amount
                print("New balance after betting: " + str(money))
                return bet_amount, money
        except(ValueError, TypeError):
            print("Incorrect amount!")


def race_is_on():
    slow_printing("The race is currently in progress... ")
    even_slower_print("Please Wait.....")
    slow_printing("The race is over!!!")
    

def slow_printing(string):
    for char in string + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(1./7)


def even_slower_print(string):
    for char in string + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(1./4)


def the_winner_is(horses):
    winner_is = random.choice(list(horses.keys()))
    print("The winner is: " + winner_is)
    winner_is = horses[winner_is]
    return winner_is







def main():
    money = 100
    horses = {'Chop Chop': 2.0, 'Indian Sea': 3.2, 'Iriss Spirit': 4.3, 
              'Parknacilla': 1.5, 'Pytilla': 2.5, 'Rainbow Heart': 7.0, 
              'Storm Athena': 1.8, 'Tartlette': 0.7}
    print_horses(horses)

    print("\n")
    in_progress = True

    while in_progress:
        betted_horse = betting_on_horse(horses)
        actual_bet, new_money = betting_cash_amount(new_money)
        # money -= actual_bet
        # race_is_on()
        actual_winner = the_winner_is(horses)
        if betted_horse == actual_winner:
            new_money += actual_bet * horses[actual_winner]
            print("Your horse won!! Your new Balance is: " + new_money)
        else:
            print("Sadly your horse was too slow!")



main()