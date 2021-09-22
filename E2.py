#Loop with condition: While
#Realizes operations between three numbers
#ejercicio2: Num, Num, Num --> Num
#Receives three numbers a, b and c
# If a/b is bigger than 30, return a/c*b**3
# If a/b y equal/lower than 30, return the sum of the powers of -> 
# two until 30

def ejercicio2 (a, b, c):
 n = 2
 suma = 0
 sumas = 0
 if a/b > 30:
     suma = a/c*b**3
     return suma
 if a/b <= 30:
    while n <= 30:
        sumas += n**2
        n += 2
    return sumas


def test_ejercicio2():
    assert ejercicio2(2, 4, 8) == 4960
    assert ejercicio2(10, 5, 7) == 4960
    assert ejercicio2(100, 2, 7) == 114.28571428571429

#test_ejercicio2()
