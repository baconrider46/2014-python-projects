
import time
import random

def typeit(it,low=0.03,high=0.1):
    for letter in it:
        print(letter,end='')
        time.sleep(random.uniform(low,high))
    print()
     
typeit("Captain prepare to fire some lead!")



class Ship():
    size = None

class Carrier(Ship):
    size = 5

class Battleship(Ship):

    size = 4

class Submarine(Ship):
    size = 3

class Destroyer(Ship):
    size = 3

class PatrolBoat(Ship):
    size = 2

#---------------------------------
    
grid = [
[' ','1','2','3','4','5','6','7','8','9','10'],
['A','~','~','~','~','~','~','~','~','~','~'],
['B','~','~','~','~','~','~','~','~','~','~'],
['C','~','~','~','~','~','~','~','~','~','~'],
['D','~','~','~','~','~','~','~','~','~','~'],
['E','~','~','~','~','~','~','~','~','~','~'],
['F','~','~','~','~','~','~','~','~','~','~'],
['G','~','~','~','~','~','~','~','~','~','~'],
['H','~','~','~','~','~','~','~','~','~','~'],
['I','~','~','~','~','~','~','~','~','~','~'],
['J','~','~','~','~','~','~','~','~','~','~'],
]


def show_grid():
    for row in grid:
        for col in row:
            print(col, end=' ')
        print()
while True:
    shoot_row = input("target Row: ").strip()
    shoot_row = int(shoot_row)
    shoot_col = int(input("target column: ").strip())
    grid[shoot_row][shoot_col] = 'H'
    show_grid()
    
