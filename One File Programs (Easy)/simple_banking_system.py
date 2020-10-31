import random
import sys


class BankingSystem:
    all_card_info = {}

    def __init__(self):
        self.iin = '400000'
        self.account_identifier = ''
        self.checksum = str(random.randint(0, 9))
        self.card_number = ''
        self.pin = ''
        self.balance = 0

    def menu(self, n=1):
        while n:
            print('''1. Create an account
2. Log into account
0. Exit''')
            n = int(input())
            if n == 1:
                self.create_account()
            elif n == 2:
                self.log_in()
        print('\nBye!\n')

    def create_account(self):
        self.account_identifier = str(random.randrange(100000000, 999999999))
        self.pin = str(random.randrange(1000, 9999))
        self.card_number = self.iin + self.account_identifier + self.checksum
        print('\nYour card has been created')
        print('Your card number:\n{}'.format(self.card_number))
        print('Your card PIN:\n{}'.format(self.pin))
        BankingSystem.all_card_info[self.card_number] = self.pin

    def log_in(self):
        print('\nEnter your card number:')
        c_number = input()
        print('Enter your PIN:')
        c_pin = input()
        if not c_number in BankingSystem.all_card_info.keys():
            print('\nWrong card number or PIN!\n')
        else:
            if BankingSystem.all_card_info[c_number] == c_pin:
                print('\nYou have successfully logged in!\n')
                self.logged_in_menu()
            else:
                print('\nWrong card number or PIN!\n')

    def logged_in_menu(self, n=1):
        while n:
            print('''1. Balance
2. Log out
0. Exit''')
            n = int(input())
            if n == 1:
                print('\nBalance: {}\n'.format(self.balance))
            elif n == 2:
                print('\nYou have successfully logged out!\n')
                break
        if not n:
            print('\nBye!\n')
            sys.exit()


testing = BankingSystem()
testing.menu()