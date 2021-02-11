# This is Conway's Game of Life.
# Written by Ron Davis.

import random
import time
import os

class cell:
    def __init__(self, alive):
      self.alive = alive
      self.nextAlive = 0
    def alive(self):
      return self.alive
    def nextAlive(self):
      return self.nextAlive
    def setNextAlive(self, x):
      self.nextAlive = x
    def setAlive(self, x):
      self.alive = x

ip = ""

# Input checking
while(not ip.isnumeric() or int(ip) <= 0):
    ip = input("Enter number of cycles: ")
ip = int(ip)

#TODO Size field to user's screen
Cells = []
x = 200 + 3
y = 54 + 3
# Fill Cells with a 2D array of size x and y filled with random cell 
# and a boarder of dead cells
for i in range(x):
    Cells.append([])
    for j in range(y):
        if (i == 0 or i == x - 1 or j == 0 or j == y - 1):
            Cells[i].append(cell(0))
        else:
            Cells[i].append(cell(random.randint(0,1)))

# Loop until exit is True
exit = False
while(not exit):
    # Process the board
    for frame in range(ip + 1):
        string = ""

        # Print the current cells
        for j in range(1,len(Cells[0]) - 1):
            for i in range(1,len(Cells) - 1):
                if (Cells[i][j].alive):
                    string += "\u2206" # u"220E
                else:
                    string += " "
            string += "\n"
        os.system('clear')
        print(string)

        # Calculate the next frame
        for i in range(1, len(Cells) - 1):
            for j in range(1, len(Cells[0]) - 1):
                neighbors = Cells[i-1][j-1].alive + Cells[i][j-1].alive + Cells[i+1][j-1].alive + Cells[i-1][j].alive + Cells[i+1][j].alive + Cells[i-1][j+1].alive + Cells[i][j+1].alive + Cells[i+1][j+1].alive
                if (neighbors < 2 or neighbors > 3):
                    Cells[i][j].setNextAlive(0)
                elif (neighbors == 3):
                    Cells[i][j].setNextAlive(1)
                else:
                    Cells[i][j].setNextAlive(Cells[i][j].alive)

        # Stage the next frame
        for i in range(1, len(Cells) - 1):
            for j in range(1, len(Cells[0]) - 1):
                Cells[i][j].setAlive(Cells[i][j].nextAlive)
    
        # Delay so that the human eye can visualize the data
        print("time: ", frame)
        time.sleep(.4)

    # Exit condition
    ip = input("More time? Enter a number of more steps or 0 to exit: ")
    if (ip.isnumeric() and ip != "0"):
        ip = int(ip)
    else:
        exit = True
