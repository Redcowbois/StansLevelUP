import re

#Return: (int, int list)
# Reads what is in the storage txt file
def readStorage():
    try: #See if file exists
        currentFile = open("storage.txt", "r")

    except: #If file doesn't exist -> default values
        print("File doesn't exist")
        returnValue = (0, [0])
    
    else: #If file exists -> get values
        print("File already exists")
        storedLevel = int(currentFile.readline()[:-1])

        storedHistory = currentFile.readline()
        if re.search(r"[0:9]", storedHistory) != None: 
            storedHistory = storedHistory.split(",")
            for i in range(len(storedHistory)):
                storedHistory[i] = int(storedHistory[i])
        else:
            storedHistory = []

        returnValue = (storedLevel, storedHistory)
        currentFile.close() 

    finally: #Actually return
        return returnValue


#Args: 
# level = int;
# historyStack = int list 
# Writes the current values to the storage txt file
def writeStorage(level, historyStack):
    file = open("storage.txt", "w")
    
    stringHistory = ""
    for x in historyStack:
        stringHistory += str(x) + ","
    stringHistory = stringHistory[:len(stringHistory)-1]

    file.write(str(level)+"\n")
    file.write(stringHistory)
    file.close()
    
