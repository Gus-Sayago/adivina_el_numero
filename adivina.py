from random import randint
# el usuario debe adivinar un número que se genera al azar
# esta primera versión solo permite un intento
# en la siguiente version daremos más oportunidades y pistas

#generamos un numero al azar entre 1 y 10 y lo guardamos en una variable
numero_a_adivinar = randint(1,10)

print("******* ADIVINA EL NÚMERO!!! ********")
#pedimos al usuario que adivine el número
numero_usuario = int(input("Adivina un número entre 1 y 10: "))

#verificamos si acertó el número
if(numero_usuario == numero_a_adivinar):
    print("ACERTASTE!!!!")
    
else:
    print("PERDISTE!!!")

#mostramos el número a adivinar
print(f"El número era {numero_a_adivinar}")