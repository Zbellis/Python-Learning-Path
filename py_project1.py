import random 

gen_number = random.randint(1, 1000)

guess_count = 0

guess_number = int(input("Guess a number between 1 - 1000: "))

while True:
    if guess_number == gen_number:
        print("Correct!")
        guess_count += 1
        print(guess_count)
        break

    elif guess_number > gen_number:
        guess_count += 1

        print("Your number is too high")
        #500 actually 450
        
        """ if guess_number - 50 == gen_number:
            print("You are really close")
        else:
            print("You are not close, keep trying")
 """
        guess_number = int(input("Guess a number between 1 - 1000: "))


    elif guess_number < gen_number:
        guess_count += 1
        print("Your number is too low")
        """ if guess_number + 50 == gen_number:
            print("You are really close")
        else:
            print("You are not close, keep trying") """
        guess_number = int(input("Guess a number between 1 - 1000: "))
        