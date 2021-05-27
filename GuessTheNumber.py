
num = 40
guesses = 6
print("Welcome To The Guess Game, You have only 6 turn to guess")
print("Start Game By entering value b\w 100:")
while True:
        if guesses == 0:
            break
        x = int(input())
        if x < 10: 
            print("Enter a Big value,you're too far")
        if x >= 10 and x <= 20: 
            print("Enter a Big value,you're close")
        elif x >= 20 and x <= 30:
            print("Enter a big value, you're too close")
        elif x >= 30 and x < 40: 
            print("Enter a big value,you're too close")
        elif x > 40 and x <= 50: 
            print("Enter a small value,you're too close")
        elif x >= 50 and x <=60:
            print("Enter a small value, you're close")
        elif x >= 60 and x <= 70:
            print("Enter a small value,you're too far")
        elif x >= 70 and x <= 80:
            print("You Enter Wrong Value")
        elif x >= 80 and x <= 90:
            print("Enter a small value, you're close")
        elif x >= 90 and x <= 100:
            print("Enter a small value, you're close")

        guesses = guesses-1
        if guesses == 5 and x != 40:
            print("You Remained with 5 chances\n")
        if guesses == 4 and x != 40:
            print("You Remained with 4 chances\n")
        if guesses == 3 and x != 40:
            print("You Remained with 3 chances\n")
        if guesses == 2 and x != 40:
            print("You Remained with 2 chances\n")
        if guesses == 1 and x != 40:
            print("You Remained with 1 chances\n")
        if guesses == 0:
            print("Game Over\n")
            print("Guessing Number is:\n",num)
        if num == x:
            print("Congrats You Won the game\n")
            print("No of guesses you left: \n",guesses)
            break

