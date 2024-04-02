start_workout = input('Start workout (Y/N)? ').upper()
print(start_workout)

if start_workout == 'Y':
    exercise = input('Exercise? ')
    while True:
        while True:
            try: 
                reps = int(input('Reps? '))
                break
            except ValueError: 
                print('Error! Insert an integer number (e.g. \'8\' or \'12\')')
                continue
        choice = input('More reps (R), new exercise (N) or end workout (Q)? ').upper()
        if choice == 'R':
            continue
        elif choice == 'N': 
            next_exercise = input('Next exercise? ')
        elif choice == 'Q': 
            break
        else: 
            print('Error! Value not allowed! It must be "R", "N" or "Q"')
    print('Well done!')
else: 
    print('Alright, see you next time!')
    quit()
