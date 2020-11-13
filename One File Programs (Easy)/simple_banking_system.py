import random, sys, sqlite3


class BankingSystem:

    def __init__(self):
        self.id = 1
        self.iin = '400000'
        self.account_identifier = ''
        self.checksum = ''
        self.current_card_number = ''
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
        self.current_card_number = self.iin + self.account_identifier + self.checksum
        print('\nYour card has been created')
        print('Your card number:\n{}'.format(self.current_card_number))
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

        t = (self.id, self.current_card_number, self.pin,)
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

    def check_luhn_algo(self, card_number):
        card_number = [int(dgt) for dgt in card_number]
        # Pop last digit
        total = card_number.pop()
        for i in range(len(card_number)):
            if i % 2 == 0:
                card_number[i] *= 2
            if card_number[i] > 9:
                card_number[i] -= 9
        for dgt in card_number:
            total += dgt
        if total % 10 == 0:
            return True
        else:
            return False

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
                self.current_card_number = c_number[0]
                self.logged_in_menu()
            else:
                print('\nWrong card number or PIN!\n')

    def get_balance(self):
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()
        t = (self.current_card_number,)
        c.execute('SELECT balance FROM card WHERE number = ?', t)
        self.balance = c.fetchone()[0]
        print('\nBalance: {}\n'.format(self.balance))
        conn.close()

    def add_income(self):
        new_amount = int(input('Enter income:\n'))
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()
        self.get_balance()
        new_amount += self.balance
        t = (new_amount, self.current_card_number,)
        c.execute('''
        UPDATE card
        SET balance = ?
        WHERE number = ?
        ''', t)
        conn.commit()
        conn.close()
        print('Income was added!')

    def transfer_money(self):
        print('Transfer')
        print('Enter card number:')
        receiver_card_number = input()
        # RECEIVER CARD FAILED LUHN ALGORITHM
        if not self.check_luhn_algo(receiver_card_number):
            print('Probably you made a mistake in the card number. Please try again!')
        else:
            # TRANSFER MONEY TO OWN ACCOUNT
            if self.current_card_number == receiver_card_number:
                print('You can\'t transfer money to the same account!')
            else:
                conn = sqlite3.connect('card.s3db')
                c = conn.cursor()
                c.execute('SELECT * FROM card WHERE number = ?', (receiver_card_number,))
                # RECEIVER CARD DOESN'T EXISTS IN DATABASE
                if c.fetchone() is None:
                    print('Such a card does not exist.')
                else:
                    print('Enter how much money you want to transfer:')
                    transfer_amount = int(input())
                    c.execute('SELECT balance FROM card WHERE number = ?', (self.current_card_number,))
                    sender_balance = c.fetchone()[0]
                    # MORE MONEY THAN HE HAS
                    if transfer_amount > sender_balance:
                        print('Not enough money!')
                    else:
                        sender_balance -= transfer_amount
                        c.execute('SELECT balance FROM card WHERE number = ?', (receiver_card_number,))
                        receiver_balance = c.fetchone()[0]
                        receiver_balance += transfer_amount
                        c.execute('''
                        UPDATE card
                        SET balance = ?
                        WHERE number = ?''', (sender_balance, self.current_card_number,))
                        conn.commit()
                        c.execute('''
                        UPDATE card
                        SET balance = ?
                        WHERE number = ?''', (receiver_balance, receiver_card_number))
                        conn.commit()
                        conn.close()
                        print('Success!')

    def close_account(self):
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()
        t = (self.current_card_number,)
        c.execute('DELETE FROM card WHERE number = ?', t)
        conn.commit()
        conn.close()
        print('\nThe account has been closed!\n')

    def logged_in_menu(self, n=1):
        while n:
            print('''
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit''')
            n = int(input())
            if n == 1:
                self.get_balance()
            elif n == 2:
                self.add_income()
            elif n == 3:
                self.transfer_money()
            elif n == 4:
                self.close_account()
                break
            elif n == 5:
                print('\nYou have successfully logged out!\n')
                break
        if not n:
            sys.exit('\nBye!\n')


simple_banking_system = BankingSystem()
simple_banking_system.create_database()
simple_banking_system.menu()