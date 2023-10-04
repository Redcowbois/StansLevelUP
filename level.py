from numpy import * 

def user_input():
    text_in = input()

    try:
        num = int(text_in)
    except:
        print("Invalid input")
        user_input()
    
user_input()