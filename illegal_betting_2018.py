import random
import sys
import time
import os


def print_horses(horses):
    os.system("clear")
    print("\nHorses:\t\tOdds:\n")
    for horse in horses.keys():
        print(f"{horse:15} {horses[horse]:.1f}")


def betting_on_horse(horses):
    betting_is_on = True
    while betting_is_on:
        try:
            bet = input("\nWhich horse you wanna bet on? ")
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
            bet_amount = float(bet_amount)
            if bet_amount > money:
                print("Not enough money to bet!")
            elif bet_amount <= 0:
                print("You cannot bet zero or less!!")
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
    time.sleep(0.7)
    # winner_is = horses[winner_is]
    return winner_is


def play_again(in_progress):
    answer = input("Would you like to play again? ").lower().startswith("y")
    if answer == "y":
        main()
    else:
        in_progress = False





def main():
    time.sleep(3)
    money = 100
    horses = {'Chop Chop': 2.0, 'Indian Sea': 3.2, 'Iriss Spirit': 4.3, 
              'Parknacilla': 1.5, 'Pytilla': 2.5, 'Rainbow Heart': 0.7, 
              'Storm Athena': 1.8, 'Tartlette': 7.0}

    in_progress = True

    while in_progress:
        print_horses(horses)
        betted_horse = betting_on_horse(horses)
        actual_bet, new_money = betting_cash_amount(money)
        # money -= actual_bet
        # race_is_on()
        actual_winner = the_winner_is(horses)
        if new_money < 1:
            print("You lost all your money! Game Over.")
            new_money = money
            print("Here.. We grant you another 100 credit to play..")
            play_again(in_progress)
        else:
            if betted_horse == actual_winner:
                new_money += actual_bet * horses[actual_winner]
                print("Your horse won!! Your new Balance is: " + str(new_money))
                time.sleep(1)
                slow_printing("Next Race in...    3..    2..     1..")
                time.sleep(0.5)
            else:
                print("Sadly your horse was too slow!")
                slow_printing("Next Race in...    3..    2..     1..")
                time.sleep(0.5)

        money = new_money

main()