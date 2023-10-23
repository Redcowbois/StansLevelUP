from numpy import log10 

class LevelManager:
    # Args: 
    # timeSpent = int
    # timeHistory = int list of size 5
    def __init__(self, timeSpent, timeHistory):
        self.timeSpent = timeSpent
        self.timeHistory = timeHistory
    

    # Takes a time spent in hours and returns a level value based
    # on a logarithmic function
    def timeToLevel(self):
        level = (57 * log10(self.timeSpent + 12)) - 60
        return level
    

    # Adds the amount of time added to the stack
    # If the stack is full, remove lowest element then push
    def addToHistory(self, newTime):
        if self.timeHistory.size() < 5:
            self.timeHistory.append(newTime)
        else:
            self.timeHistory.pop(0)
            self.timeHistory.append(newTime)


    # Removes from history stack
    # Returns -1 if empty    
    def removeFromHistory(self):
        if self.timeHistory:
            return self.timeHistory.pop()
        else:
            return -1


    # Add a time in hours to the total and to the history stack
    def addTime(self, newTime):
        self.addToHistory(newTime)
        return self.timeSpent + newTime
    







    