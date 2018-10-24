import random

def betting_on_horse():
    betting_is_on = True
    while betting_is_on:
        try:
            bet = input("Which horse you wanna bet on? ")
            bet = int(bet)
            if bet > 0 and bet < 9:
                print("jó a bemenet!!")
                return bet
                betting_cash_amount()
                betting_is_on = False
            else:
                print("Try again homie, this is not the right number!")
        except(ValueError, TypeError):
            print("This is not a number at all.")

def betting_cash_amount():
    betting_is_on = True
    while betting_is_on:
        try:
            bet_amount = input("How much you wanna bet? ")
            bet_amount = int(bet_amount)
            if bet_amount > money:
                print("Not enough money to bet!")
            else:
                betting_odds()
                return bet_amount
        except(ValueError, TypeError):
            print("Incorrect amount!")

def betting_odds():
    





money = 100
horses = ['Chop Chop', 'Indian Sea', 'Iriss Spirit', 
          'Parknacilla', 'Pytilla', 'Rainbow Heart', 
          'Storm Athena', 'Tartlette']

betting_on_horse()