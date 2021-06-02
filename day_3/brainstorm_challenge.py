# day_3/brainstorm_challenge.py

"""
5 Ideas that you and your partner might want to work on. 

Ex. I want to make a digital system for tracking husky bucks. 

1. 
2. 
3. 
4. 
5.

After you have 5 ideas written down think about how you might go about building 
the ideas with what you know so far. How could you break it down and make it out
of code? Write that down below:

Ex. I need way to map uniue ids (maybe student ids?) to accounts held by students
so maybe i can use a dictionary to hold ids(card_numbers) as keys and a class
representing student accounts as values then I just need a way to debit and
credit to the student's account.


After you finish listing your 5 ideas and finish breaking down one of them you can
start working on a command line version below.
"""

class HuskyBucksSystem:
    """
    This is an example command line version of a husky bucks system
    """
    def __init__(self) -> None:
        self.accounts = {}

    def add_student(self, student_id, name) -> None:
        self.accounts[student_id] = Student(name)

    def is_id_valid(self, id):
        return self.accounts.get(id) != None

    def check_for_funds(self, student_id, amount):
        return self.get_balance(student_id) >= amount

    def get_balance(self, student_id):
        return self.accounts[student_id].current_balance() 

    def debit_student(self, student_id, amount):
        self.accounts[student_id].debit(amount)

    def credit_student(self, student_id, amount):
        self.accounts[student_id].credit(amount)

    def start(self):
        print('Hello thanks for banking with husky')
        while True:
            user_input = None
            while user_input not in ('a', 'check', 'c', 'd', 'e'):
                if user_input != None:
                    print("That wasn't an option")
                print('What would you like to do?')
                print('Enter (a) to add a student')
                print('Enter (check) to check a students funds')
                print('Enter (c) to credit a student')
                print('Enter (d) to debit a student')
                print('Enter (e) to exit the system')
                user_input = input('Please enter an option: ')

            if user_input == 'a':
                name = input('Please enter a name: ')
                id = self.get_id()
                self.add_student(id, name)
                print(f'{name} was added to the Husky bucks system')
            elif user_input == 'check':
                id = self.get_id()
                balance = self.get_balance(id)
                print(f'The balance of account: {id} is {balance}')
            elif user_input == 'c':
                id = self.get_id()
                if self.is_id_valid(id) == True:
                    amount = self.get_amount()
                    old_balance = self.get_balance(id)
                    self.credit_student(id, amount)
                    new_balance = self.get_balance(id)
                    print(f'The balance of account: {id} was {old_balance} and is now {new_balance}')
                else:
                    print('thats not a valid id.')
            elif user_input == 'd':
                id = self.get_id()
                if self.is_id_valid(id) == True:
                    amount = self.get_amount()
                    old_balance = self.get_balance(id)
                    self.debit_student(id, amount)
                    new_balance = self.get_balance(id)
                    print(f'The balance of account: {id} was {old_balance} and is now {new_balance}')
                else:
                    print('thats not a valid id.')
            elif user_input == 'e':
                break

    def get_amount(self):
        amount = None
        user_input = None
        while type(amount) is not int:
            if user_input is not None:
                print("That wasn't a number")
            user_input = input('Please enter an amount: ')
            try:
                amount = int(user_input)
            except:
                pass
        return amount

    def get_id(self):
        id = None
        user_input = None
        while type(id) is not int:
            if user_input is not None:
                print("That wasn't an id")
            user_input = input('Please enter an id: ')
            try:
                potential_id = int(user_input)
                id = potential_id
            except:
                pass
        return id


class Student:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def credit(self, amount):
        self.account_balance += amount

    def debit(self, amount):
        self.account_balance -= amount

    def current_balance(self):
        return self.account_balance

if __name__ == '__main__':
    hbs = HuskyBucksSystem()
    hbs.start()
