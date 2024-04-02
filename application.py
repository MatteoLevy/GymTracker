# Verify that the input is among the valid options, throws error otherwise and asks for input again.
start_workout_choices = ["Y", "N"]
while True:
    start_workout = input('Start workout (Y/N)? ').upper()
    if start_workout in start_workout_choices:
        break
    else:
        print('Error! Value not allowed! It must be "Y" or "N"')

if start_workout == 'Y':
    exercise = input('Exercise? ')
    while True:
        # Verify that the reps input is an integer, throws error otherwise and asks for input again.
        while True:
            try: 
                reps = int(input('Reps? '))
                break
            except ValueError: 
                print('Error! Insert an integer number (e.g. \'8\' or \'12\')')
                continue
        
        # Verify that the input is among the valid options, throws error otherwise and asks for input again.
        valid_choices = ["R", "N", "Q"]
        while True:
            choice = input('More reps (R), new exercise (N), or end workout (Q)? ').upper()
            if choice in valid_choices:
                break
            else:
                print('Error! Value not allowed! It must be "R", "N", or "Q"')

        if choice == 'R':
            continue
        elif choice == 'N': 
            next_exercise = input('Next exercise? ')
        elif choice == 'Q': 
            break
        else: 
            print('Error!')
    print('Well done!')
else: 
    print('Alright, see you next time!')
    quit()
