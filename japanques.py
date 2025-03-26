import os

# For Windows
os.system('cls')

while True:
    #import os

    # For Windows
    #os.system('cls')
    print( '''Question 67
    What was the first city to have an atomic bomb dropped on it?

    1. Tokyo
    2. Hiroshima
    3. Nagasaki

    #trivia''')

    answer = input('What is your answer? ')
    #answer = int(answer)

    if (answer == '1'):
        print("WRong");
    elif (answer == '2'):
        print("right");
        break;
    elif (answer == '3'):
        print("wrong");
    else:
        print("Please enter 1, 2, or 3.")
