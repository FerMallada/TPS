def adivinar(N):
    import random
    numero = random.randint(0, 100)
    for i in range (1,N):
        x=int(input('ingrese un Num entero entre 0 y 100: '))
        if x < 0 or x > 100:
            print('fuera de rango')
        else:
            if x == numero:
                print('Felicitaciones, adivinaste en {0} intentos.'.format(i))
                break
            elif x < numero:
                print('No, es un poco mayor')
            else:
                print('No, es un poco menor')
    else:
        print('numero de intentos superado')
N = 6
adivinar(N)