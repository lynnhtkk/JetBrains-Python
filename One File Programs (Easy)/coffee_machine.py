class CoffeeMachine:

    def __init__(self):
        self.cash = 550
        self.water = 400
        self.milk = 540
        self.c_bean = 120
        self.cups = 9

    def __str__(self):
        return  'The coffee machine has:\n'\
                f'{self.water} of water\n'\
                f'{self.milk} of milk\n'\
                f'{self.c_bean} of coffee beans\n'\
                f'{self.cups} of disopsable cups\n'\
                f'{self.cash} of money\n'

    def buy(self):
        self.coffee_type = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:: \n')
        if self.coffee_type == '1':
            self.result = self.check_resource(250, 0, 16)
            if self.result == 'enough':
                print('I have enough resources, making you a coffee!')
                self.water -= 250
                self.c_bean -= 16
                self.cups -= 1
                self.cash += 4
            else:
                print(f'Sorry, not enough {self.result}!')
        elif self.coffee_type == '2':
            self.result = self.check_resource(350, 75, 20)
            if self.result == 'enough':
                print('I have enough resources, making you a coffee!')
                self.water -= 350
                self.milk -= 75
                self.c_bean -= 20
                self.cups -= 1
                self.cash += 7
            else:
                print(f'Sorry, not enough {self.result}!')
        elif self.coffee_type == '3':
            self.result = self.check_resource(200, 100, 12)
            if self.result == 'enough':
                print('I have enough resources, making you a coffee!')
                self.water -= 200
                self.milk -= 100
                self.c_bean -= 12
                self.cups -= 1
                self.cash += 6
            else:
                print(f'Sorry, not enough {self.result}!')
        elif self.coffee_type == 'back':
            return

    def check_resource(self, w, m, b):
        if self.water < w:
            return 'water'
        elif self.milk < m:
            return 'milk'
        elif self.c_bean < b:
            return 'coffee beans'
        elif self.cups == 0:
            return 'cups'
        else:
            return 'enough'

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add:\n'))
        self.milk += int(input('Write how many ml of milk do you want to add:\n'))
        self.c_bean += int(input('Write how many g of coffee beans do you want to add:\n'))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add:\n'))


    def take(self):
        print(f'I gave you {self.cash} $')
        self.cash = 0

    def remaining(self):
        print(self)

    def get_input(self):
        while True:
            self.action = input('Write action (buy, fill, take, remaining, exit): \n')
            if self.action == 'buy':
                self.buy()
            elif self.action == 'fill':
                self.fill()
            elif self.action == 'take':
                self.take()
            elif self.action == 'remaining':
                self.remaining()
            elif self.action == 'exit':
                break

uit = CoffeeMachine()
uit.get_input()
