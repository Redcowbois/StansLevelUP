from numpy import log10 
from math import floor

class LevelManager:
    # Args: 
    # timeSpent = float
    # timeHistory = float list of size 5
    def __init__(self, timeSpent, timeHistory):
        self.timeSpent = timeSpent
        self.timeHistory = timeHistory
    

    # Takes a time spent in hours and returns a level value based
    # on a logarithmic function
    def timeToLevel(self):
        temp = 0
        if self.timeSpent <= 200:
            return (100 * log10(self.timeSpent + 15.9)) - 120
        else:
            temp = 200 - self.timeSpent
            return ((100 * log10(200 + 15.9)) - 120) + (0.2 * temp)
    

    # Adds the amount of time added to the stack
    # If the stack is full, remove lowest element then push
    def addToHistory(self, newTime):
        if len(self.timeHistory) < 5:
            self.timeHistory.append(newTime)
        else:
            self.timeHistory.pop(0)
            self.timeHistory.append(newTime)


    # Removes from history stack and removes that value from timeSpent
    # Returns -1 if empty    
    def undoEntry(self):
        if self.timeHistory:
            value = self.timeHistory.pop()
            self.timeSpent = self.timeSpent - value
            return value
        else:
            return -1


    # Add a time in hours to the total and to the history stack
    def addTime(self, newTime):
        self.addToHistory(newTime)
        self.timeSpent = self.timeSpent + newTime
    







    