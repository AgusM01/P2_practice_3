#While loop
#Sum of the numbers bigger than 20
#ejercicio3 : None --> Int
#Receive nothing
#Return the sum of all numbers from n, to 20 (n > 20)
def ejercicio3 (n = 50):
 h = 0
 while n >= 20:
     h += n
     n -= 2
 return h

def test_ejercicio3 ():
    assert ejercicio3() == 560

#test_ejercicio3()





