#For Loop

#Shows the iteraction of a for loop
#ejercicio5: None -> None
#Receive nothing
#Return in a string-form, the iterations of a for loop
def ejercicio5(s):
 for x in range (s):
     for z in range (x):
        print(z)
 print("***************")


#Idk how to make this assert
def test_ejercicio5 ():
    assert ejercicio5(2) == None

#test_ejercicio5()


