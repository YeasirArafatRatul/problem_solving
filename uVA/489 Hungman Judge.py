
while True:
    n = int(input())
    if n == -1:
        break
    else:
        solution = str(input())
        guess = str(input())

        count = 0
        for i in guess:
            if i in solution:
                solution = solution.replace(i,'')     
            else:
                count += 1
                if count == 7:
                    break
                
                
        if solution == '':
            print(f'Round {n}')
            print('You win.')

        elif count < 7:
            print(f'Round {n}')
            print('You chickened out.')
        else:
            print(f'Round {n}')
            print('You lose.')

