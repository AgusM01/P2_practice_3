# Loop with condition: While

#Show every multiple of 5 lower than 100 and bigger than 20
def ejercicio1 (n = 100):
   h = " "
   while n >= 20:
    h += " " + str(n)
    n -= 5
   return h


#Assert doesn't work 
def test_ejercicio1 ():
   assert ejercicio1(100) == ' 100 95 90 85 80 75 70 65 60 55 50 45 40 35 30 25 20'

#test_ejercicio1()
