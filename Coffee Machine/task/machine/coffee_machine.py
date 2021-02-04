class CoffeeMachine:
    water = 400
    milk = 540
    coffee_beans = 120
    coffee_cups = 9
    money = 550

    ingredients = {'water': water, 'milk': milk, 'coffee_beans': coffee_beans, 'coffee_cups': coffee_cups,
                   'money': money}

    def __init__(self):
        self.again = True

    def print_actions(self):
        print(f"""
            The coffee machine has:
            {self.ingredients['water']} of water
            {self.ingredients['milk']} of milk
            {self.ingredients['coffee_beans']} of coffee beans
            {self.ingredients['coffee_cups']} of disposable cups
            ${self.ingredients['money']} of money
            """)

        return self.ingredients

    def enough(self, requirements):
        if self.ingredients['water'] >= requirements['water']:
            if self.ingredients['milk'] >= requirements['milk']:
                if self.ingredients['coffee_beans'] >= requirements['coffee_beans']:
                    if self.ingredients['coffee_cups'] >= requirements['coffee_cups']:
                        print('I have enough resources, making you a coffee!')
                        self.ingredients['water'] -= requirements['water']
                        self.ingredients['milk'] -= requirements['milk']
                        self.ingredients['coffee_beans'] -= requirements['coffee_beans']
                        self.ingredients['coffee_cups'] -= requirements['coffee_cups']
                        self.ingredients['money'] += requirements['money']
                    else:
                        print('Sorry, not enough cups!')
                else:
                    print('Sorry, not enough beans!')
            else:
                print('Sorry, not enough milk!')
        else:
            print('Sorry, not enough water!')

        return self.ingredients

    def question(self):
        while self.again:
            question = input("Write action (buy, fill, take, remaining, exit): ")
            if question == 'buy':
                self.buy()
            elif question == 'fill':
                self.fill()
            elif question == 'take':
                self.take()
            elif question == 'remaining':
                self.remaining()
            elif question == 'exit':
                self.again = False
            else:
                print('wrong input')

    def buy(self):
        what = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if what == '1':
            requirements = {'water': 250, 'milk': 0, 'coffee_beans': 16, 'coffee_cups': 1, 'money': 4}
            self.enough(requirements)

        elif what == '2':
            requirements = {'water': 350, 'milk': 75, 'coffee_beans': 20, 'coffee_cups': 1, 'money': 7}
            self.enough(requirements)

        elif what == '3':
            requirements = {'water': 200, 'milk': 100, 'coffee_beans': 12, 'coffee_cups': 1, 'money': 6}
            self.enough(requirements)

        elif what == 'back':
            pass

    def fill(self):
        water_ques = input("Write how many ml of water do you want to add: ")
        milk_ques = input("Write how many ml of milk do you want to add: ")
        beans_ques = input("Write how many grams of coffee beans do you want to add: ")
        cups_ques = input("Write how many disposable cups of coffee do you want to add: ")
        self.ingredients['water'] += int(water_ques)
        self.ingredients['milk'] += int(milk_ques)
        self.ingredients['coffee_beans'] += int(beans_ques)
        self.ingredients['coffee_cups'] += int(cups_ques)

    def take(self):
        print("I gave you", self.ingredients['money'])
        self.ingredients['money'] -= self.ingredients['money']

    def remaining(self):
        self.print_actions()


coffee_machine = CoffeeMachine()
coffee_machine.question()







