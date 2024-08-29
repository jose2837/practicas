print ("Bienvenido a su programa para calcular el factorial de un número")
n=  int (input("ingrese el número del que desea saber su factorial:"))

factorial= 1
for i in range (1,n+1):
    factorial *= i 
print("el factorial es:")
print(factorial)