import random

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
                return bet_amount
        except(ValueError, TypeError):
            print("Incorrect amount!")
''' 
    def betting_odds():
        betting_is_on = True
        while betting_is_on:
            try:
                odds = input("What odds you wanna bet? ")
'''

def race_is_on():
    

def main():
    money = 100
    horses = {'Chop Chop': 2.0, 'Indian Sea': 3.2, 'Iriss Spirit': 4.3, 
              'Parknacilla': 1.5, 'Pytilla': 2.5, 'Rainbow Heart': 7.0, 
              'Storm Athena': 1.8, 'Tartlette': 0.7}
    # print(f"Horses{:15} Odds{:1}")
    print("Horses:\t\tOdds:\n")

    for horse in horses.keys():
        print(f"{horse:15} {horses[horse]:.1f}")

    print("\n")

    while True:
        betting_on_horse(horses)
        actual_bet = betting_cash_amount(money)
        money -= actual_bet
        print(money)


main()