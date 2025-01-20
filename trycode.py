'''# A simple decorator function
def decorator(func):
                
    def wrapper():
        print("Transaction initiated..")
        func()
        print("Transaction completed..")
    return wrapper

# Applying the decorator to a function
@decorator

def hello():
    print("...Executing all the steps of Transaction...")
#hello1 = decorator(hello)
hello() 

A simple decorator function
def decorator(func):
  
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

# Applying the decorator to a function
@decorator

def greet():
    print("Hello, World!")

greet()'''
'''try:
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    result = a / b
    print('Result is: ', result)
except ZeroDivisionError:
    print('Cannot divide by zero!')
except ValueError:
    print('Please enter valid integers!')
except Exception as e:
    print('An error occurred: ', e)'''
    
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def move(self, steps):
        self.position += steps

class GameBoard:
    def __init__(self):
        self.board = [i for i in range(101)]
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

    def check_snakes_and_ladders(self, player):
        if player.position in self.snakes:
            player.position = self.snakes[player.position]
        elif player.position in self.ladders:
            player.position = self.ladders[player.position]

def play_game():
    player1 = Player('Player 1')
    player2 = Player('Player 2')
    board = GameBoard()
    players = [player1, player2]

    while True:
        for player in players:
            input(f"{player.name}'s turn. Press Enter to roll the dice...")
            dice_roll = player.roll_dice()
            print(f"{player.name} rolled a {dice_roll}")
            player.move(dice_roll)
            print(f"{player.name} moved to position {player.position}")
            board.check_snakes_and_ladders(player)
            print(f"{player.name} is now at position {player.position}")

            if player.position >= 100:
                print(f"{player.name} wins!")
                return

if __name__ == "__main__":
    play_game()
    