import random
import time
import os

def pantalla(tablero,turno):
    print("*"*42)
    print("*",end="");print("tres en raya o tateti".center(40),end="");print("*")
    print("*",end="");print(" ".center(40),end="");print("*")
    print("*",end="");print("1     |2     |3     ".center(40),end="");print("*")
    print("*",end="");print("   {}  |   {}  |   {}  ".format(tablero[0],tablero[1],tablero[2]).center(40),end="");print("*")
    print("*",end="");print("      |      |      ".center(40),end="");print("*")
    print("*",end="");print(" ------+------+------".center(40),end="");print("*")
    print("*",end="");print("4     |5     |6     ".center(40),end="");print("*")
    print("*",end="");print("   {}  |   {}  |   {}  ".format(tablero[3],tablero[4],tablero[5]).center(40),end="");print("*")
    print("*",end="");print("      |      |      ".center(40),end="");print("*")
    print("*",end="");print(" ------+------+------".center(40),end="");print("*")
    print("*",end="");print("7     |8     |9     ".center(40),end="");print("*")
    print("*",end="");print("   {}  |   {}  |   {}  ".format(tablero[6],tablero[7],tablero[8]).center(40),end="");print("*")
    print("*",end="");print("      |      |      ".center(40),end="");print("*")
    print("*",end="");print(" ".center(40),end="");print("*")
    print("*",end="");print("Turno".center(40),end="");print("*")
    print("*",end="");print(" ".center(40),end="");print("*")
    print("*",end="");print("  {} ".format(turno).center(40),end="");print("*")
    print("*",end="");print(" ".center(40),end="");print("*")
    print("*"*42)

def dif():
    print("*"*42)
    print("*",end="");print("tres en raya o tateti".center(40),end="");print("*")
    print("*",end="");print(" ".center(40),end="");print("*")
    print("*",end="");print("1 Facil".center(40),end="");print("*")
    print("*",end="");print(" ".center(40),end="");print("*")
    print("*",end="");print(" 2 Dificil".center(40),end="");print("*")
    print("*",end="");print(" ".center(40),end="");print("*")
    print("*",end="");print('Elije ficha "X" o "O"'.center(40),end="");print("*")
    print("*",end="");print(" ".center(40),end="");print("*")
    print("*"*42)
    while True:
        dif=input("Nivel.:")
        if dif=="1" or dif=="2":
            ficha=""
            while ficha.upper() != "X" and ficha.upper() != "O":
                ficha=input("elije ficha ..:")
                if ficha.upper() == "X":
                    jug="X"
                    ord="O"
                else:
                    jug="O"
                    ord="X"
            break

    return dif,jug,ord

def ganador(tablero,jugador):
    if tablero[0] == tablero[1] == tablero[2] == jugador or \
       tablero[3] == tablero[4] == tablero[5] == jugador or \
       tablero[6] == tablero[7] == tablero[8] == jugador or \
       tablero[0] == tablero[3] == tablero[6] == jugador or \
       tablero[1] == tablero[4] == tablero[7] == jugador or \
       tablero[2] == tablero[5] == tablero[8] == jugador or \
       tablero[0] == tablero[4] == tablero[8] == jugador or \
       tablero[6] == tablero[4] == tablero[2] == jugador:
        return True
    else:
        return False 

def tab_lleno(tablero):
    for i in tablero:
       if i == " ":
           return False
    else:
        return True

def cas_libre(tablero,ind):
    return tablero[ind]==" "

def mov(tablero):
    posi=["1","2","3","4","5","6","7","8","9"]
    pos=None
    while True:
        if pos not in posi:
            pos=input(" ingrese juego 1 a 9 :")

        else:
            pos=int(pos)
            if not cas_libre(tablero, pos-1):
                print("ocupado")
            else:
                return pos-1

def mov_ord(tablero, jug):
    #horizontal 1
    if  tablero[0] == tablero[1] == jug and  tablero[2] == " ":
        return 2
    elif tablero[0] == tablero[2] == jug and  tablero[1] == " ":
        return 1
    elif tablero[1] == tablero[2] == jug and  tablero[0] == " ":
        return 0
     #horizontal 2
    elif tablero[3] == tablero[4] == jug and  tablero[5] == " ":
        return 5
    elif tablero[3] == tablero[5] == jug and  tablero[4] == " ":
        return 4
    elif tablero[4] == tablero[5] == jug and  tablero[3] == " ":
        return 3
    #horizontal 3
    elif tablero[6] == tablero[7] == jug and  tablero[8] == " ":
        return 8
    elif tablero[6] == tablero[8] == jug and  tablero[7] == " ":
        return 7
    elif tablero[8] == tablero[7] == jug and  tablero[6] == " ":
        return 6
    #diagonales
    elif tablero[0] == tablero[4] == jug and  tablero[8] == " ":
        return 8
    elif tablero[0] == tablero[8] == jug and  tablero[4] == " ":
        return 4
    elif tablero[8] == tablero[4] == jug and  tablero[0] == " ":
        return 0
    elif tablero[7] == tablero[4] == jug and  tablero[2] == " ":
        return 2
    elif tablero[7] == tablero[2] == jug and  tablero[4] == " ":
        return 4
    elif tablero[2] == tablero[4] == jug and  tablero[7] == " ":
        return 7
    #vertical 1
    elif tablero[0] == tablero[3] == jug and  tablero[6] == " ":
        return 6
    elif tablero[0] == tablero[6] == jug and  tablero[3] == " ":
        return 3
    elif tablero[3] == tablero[6] == jug and  tablero[0] == " ":
        return 0
    #vertical 2
    elif tablero[1] == tablero[4] == jug and  tablero[7] == " ":
        return 7
    elif tablero[1] == tablero[7] == jug and  tablero[4] == " ":
        return 4
    elif tablero[4] == tablero[7] == jug and  tablero[1] == " ":
        return 1
    #vertical 3
    elif tablero[2] == tablero[5] == jug and  tablero[8] == " ":
        return 8
    elif tablero[2] == tablero[8] == jug and  tablero[5] == " ":
        return 5
    elif tablero[5] == tablero[8] == jug and  tablero[2] == " ":
        return 2
    else:
        while True:
            ind=random.randint(0,8)
            if tablero[ind]==" ":
                break
    return ind

def mov_ord_d(tablero,us,pc):
    
    for i in range(9):
        cop=tablero[:]
        if cas_libre(cop,i):
            cop[i]=pc
            if ganador(cop,pc):
                return i

    #estas lineas remplazarias a todas de la funcion mov_ord()
    for i in range(9):
        cop=tablero[:]
        if cas_libre(cop,i):
            cop[i]=us
            if ganador(cop,us):
                return i
    
    if pc == "X":
        if tablero[4] == " ":
            return 4
        elif tablero[0]== " " or tablero[2]== " " or \
             tablero[6]== " " or tablero[8]== " ":
            vac=[]
            for i in [0,2,6,8]:
                if tablero[i] == " ":
                    vac.append(i)

            return random.choice(vac)
        else:
            vac1=[]
            for i in [1,3,5,7]:
                if tablero[i] == " ":
                    vac1.append(i)

            return random.choice(vac1)


    if pc == "O":
        c = 0
        for i in range(9):
            if tablero[i] == " ":
                c += 1
            if c == 7:
                if tablero[4] == " ":
                    return 4
    while True:
        ind=random.randint(0,8)
        if not cas_libre(cop,ind):
            ind=random.randint(0,8)
        else:
            return ind





def juego():
    tablero=[" "]*9
    os.system("clear")
    niv,jug,ord = dif()
    if jug == "X":
        turno = "Humano"
    else:
        turno = "Ordenador"
    pantalla(tablero,turno)
    while True:
        if tab_lleno(tablero):
            os.system("clear")
            pantalla(tablero,"fin del juego")
            print("*"*42)
            print("*",end="");print(" ".center(40),end="");print("*")
            print("*",end="");print("EMPATE".center(40),end="");print("*")
            print("*",end="");print(" ".center(40),end="");print("*")
            print("*"*42)
            seg=input("Deseas Seguir Jugando  S/N :")
            if seg.upper() == "S":
                juego()
            else:
                exit()
        elif turno == "Humano":
            cas=mov(tablero)
            tablero[cas] = jug
            turno = "Ordenador"
            if ganador(tablero,jug):
                os.system("clear")
                pantalla(tablero,"fin del juego")
                print("*"*42)
                print("*",end="");print(" ".center(40),end="");print("*")
                print("*",end="");print("GANASTE".center(40),end="");print("*")
                print("*",end="");print(" ".center(40),end="");print("*")
                print("*"*42)
                seg=input("Deseas Seguir Jugando  S/N :")
                if seg.upper() == "S":
                    juego()
                else:
                    exit()
            os.system("clear")
            pantalla(tablero,turno)
        elif turno == "Ordenador":
            print("          Estoy Pensando...:")
            time.sleep(2)
            if niv=="1":
                cas=mov_ord(tablero,jug)
            elif niv == "2":
                cas=mov_ord_d(tablero,jug,ord)
            tablero[cas]= ord
            turno = "Humano"
            if ganador(tablero,ord):
                os.system("clear")
                pantalla(tablero,"fin del juego")
                print("*"*42)
                print("*",end="");print(" ".center(40),end="");print("*")
                print("*",end="");print("PERDISTE".center(40),end="");print("*")
                print("*",end="");print(" ".center(40),end="");print("*")
                print("*"*42)
                seg=input("Deseas Seguir Jugando  S/N :")
                if seg.upper() == "S":
                    juego()
                else:
                    exit()
            os.system("clear")
            pantalla(tablero,turno)




juego() 
