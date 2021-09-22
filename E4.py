# While loop

#Show the quantity of odd and even numbers from n to 100
#ejercicio4: None --> String
#Receive nothing
#Return an string which indicates the quantity of even and odd numbers
#Between n and 100
def ejercicio4(n = 1):
 p = 0
 i = 0
 while n <= 100:
     if n%2 == 0:
        p += n
     else:
        i += n
     n += 1
 return "Pares= "+ str(p) + " e Impares: "+ str(i)

#Assert doesn't work
def test_ejercicio4 ():
    assert ejercicio4() == "Pares= "+ '2500' + " e Impares: "+ '2500'

#test_ejercicio4()


