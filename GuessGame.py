secret_number = 15
attempts = 0
guessed_value = 0
while attempts < 3:
    input_number = int(input('Enter your guess: '))
    if input_number == secret_number:
        print("Well done!")
        guessed_value = 1
        break
    else:
        print("Oops! That was Wrong.")
    attempts += 1
if attempts == 3 and guessed_value == 0:
    print("Game over!")