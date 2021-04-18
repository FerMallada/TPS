

def guess(j):
    import random
    num = random.randint(0, 100)
    for i in range(1, j):
        x = int(input('enter a number between 0 and 100: '))
        if x < 0 or x > 100:
            print('Out of range.')
        else:
            if x == num:
                print('Congratulations, you guessed in {0} tries.'.format(i))
                break
            elif x < num:
                print('it is bigger.')
            else:
                print('it is smaller.')
    else:
        print('GAME OVER')


n = 6
guess(n)
