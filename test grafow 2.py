
for z in range(0,100):

    i=  z/100
    a1=10+20*i
    a2=16
    a3=18-i
    b1=17
    b2=18
    b3=18
    c1=18
    c2=15
    c3=25*i**2+11

    listaA = [a1, a2, a3]
    listaB = [b1, b2, b3]
    listaC = [c1, c2, c3]

    minA = min(listaA)
    maxA = max(listaA)
    minB = min(listaB)
    maxB = max(listaB)
    minC = min(listaC)
    maxC = max(listaC)

    H1 = (i*minA+(1-i)*maxA)
    H2 = (i*minB+(1-i)*maxB)
    H3 = (i*minC+(1-i)*maxC)

    listaH = [H1, H2, H3]
    print('Lambda: ', i)
    print(' max Hurwitza: ', max(listaH))




