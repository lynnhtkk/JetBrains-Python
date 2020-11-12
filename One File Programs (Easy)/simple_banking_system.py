import random, sys, sqlite3

class BankingSystem:

    def __init__(self):
        self.id = 1
        self.iin = '400000'
        self.account_identifier = ''
        self.checksum = ''
        self.card_number = ''
        self.pin = ''
        self.balance = 0

    def create_database(self):
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS card (
        id INTEGER PRIMARY KEY,
        number TEXT,
        pin TEXT,
        balance INTEGER DEFAULT 0);''')
        conn.commit()
        conn.close()

    def menu(self, n=1):
        while n:
            print('''
1. Create an account
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
        self.checksum = self.calculate_checksum(self.iin + self.account_identifier)
        self.card_number = self.iin + self.account_identifier + self.checksum
        print('\nYour card has been created')
        print('Your card number:\n{}'.format(self.card_number))
        print('Your card PIN:\n{}'.format(self.pin))

        # INSERT DATA INTO DATABASE card.s3db TABLE card
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()
        # DETERMINE THE id
        c.execute('SELECT MAX(id) FROM card')
        if c.fetchone()[0] is None:
            self.id = 1
        else:
            c.execute('SELECT MAX(id) FROM card')
            self.id = c.fetchone()[0] + 1

        t = (self.id, self.card_number, self.pin,)
        c.execute('INSERT INTO card (id,number,pin) VALUES (?,?,?)', t)
        conn.commit()
        conn.close()

    def calculate_checksum(self, card_number):
        card_number_digits = [int(dgt) for dgt in card_number]
        for i in range(len(card_number_digits)):
            if i % 2 == 0:
                card_number_digits[i] *= 2
            if card_number_digits[i] > 9:
                card_number_digits[i] -= 9
        total = 0
        for dgt in card_number_digits:
            total += dgt
        for x in range(10):
            if (total + x) % 10 == 0:
                return str(x)

    def log_in(self):
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()
        print('\nEnter your card number:')
        c_number = (input(),)
        print('Enter your PIN:')
        c_pin = input()
        c.execute('SELECT pin FROM card WHERE number=?', c_number)
        if c.fetchone() is None:
            print('\nWrong card number or PIN!\n')
        else:
            c.execute('SELECT pin FROM card WHERE number=?', c_number)
            real_pin = c.fetchone()[0]
            if real_pin == c_pin:
                print('\nYou have successfully logged in!\n')
                c.execute('SELECT balance FROM card WHERE number=?', c_number)
                self.balance = c.fetchone()[0]
                self.logged_in_menu()
            else:
                print('\nWrong card number or PIN!\n')

    def logged_in_menu(self, n=1):
        while n:
            print('''
1. Balance
2. Log out
0. Exit''')
            n = int(input())
            if n == 1:
                print('\nBalance: {}\n'.format(self.balance))
            elif n == 2:
                print('\nYou have successfully logged out!\n')
                break
        if not n:
            sys.exit('\nBye!\n')


simple_banking_system = BankingSystem()
simple_banking_system.create_database()
simple_banking_system.menu()
