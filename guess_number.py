from random import randint, choice

a = 0
numbers = [x for x in range(1, 11)]

while True:
    numbers_2 = numbers
        
    if a == 0:
        number = choice(numbers)
        print("I thought in a number between 1 and 10, guess the number." + 
            "\n\t(Write quit to exit)")
    elif a > 0:
        numbers_2.remove(number)
        number = choice(numbers_2)
        print("I thought in a different number between 1 and 10, guess the number." + 
            "\n\t(Write quit to exit)")
    
    while True:
        guess = input()
        if guess.lower() == 'quit':
            break
        try:
            if int(guess) > 10 or int(guess) < 0:
                print("The number must be between 0 and 10.")
            elif int(guess) == number:
                print ("You guessed it right!")
                break
            elif int(guess) > number:
                print ("The number I thought is lower, try again.")
            elif int(guess) < number:
                print ("The number I thought is higher, try again.")
        except ValueError:
            print("I didn't understand you...")

    if guess.lower() == 'quit':
            break
    a += 1
    
    
    
