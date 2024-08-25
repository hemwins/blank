check_status = False
while True:
    user_input = input('> ').upper()
    if user_input == 'START' and check_status == False:
        print("starting the car.")
        check_status = True
    elif user_input == 'START' and check_status == True:
        print("Already started. ")
    elif user_input == 'STOP'and check_status != 'stopped':
        print("stopping the car.")
        check_status = 'stopped'
    elif user_input == 'STOP'and check_status == 'stopped':
        print("Already stopped. ")
    elif user_input == 'EXIT':
        print("exiting the car. ")
        break
    elif user_input == 'HELP':
        print('''
            start - to start the car
            stop - to stop the car
            exit - to exit  ''')

