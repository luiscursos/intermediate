
            ###  Challenges ###


# https://retosdeprogramacion.com/semanales2022

print("\nRETO 0 - FIZZ BUZZ\n")


'''
 Reto #0: EL FAMOSO "FIZZ BUZZ”
 FÁCIL | Publicación: 27/12/21 | Resolución: 03/01/22



 Escribe un programa que muestre por consola (con un print) los
 números de 1 a 100 (ambos incluidos y con un salto de línea entre
 cada impresión), sustituyendo los siguientes:
 - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''
def fizzbuzz():
    for i in range (1, 100+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizzbuzz()


print("\nRETO 1 - ANAGRAMA\n")


'''
 Reto #1: ¿ES UN ANAGRAMA?
 MEDIA | Publicación: 03/01/22 | Resolución: 10/01/22


 Escribe una función que reciba dos palabras (String) y retorne
 verdadero o falso (Bool) según sean o no anagramas.
 - Un Anagrama consiste en formar una palabra reordenando TODAS
   las letras de otra palabra inicial.
 - NO hace falta comprobar que ambas palabras existan.
 - Dos palabras exactamente iguales no son anagrama.

'''


def is_anagram():


    string_a = input("Enter the string_a: ") 
    string_b = input("Enter the string_b: ")
    
    if string_a.lower == string_b.lower:
        return False
    
    return sorted(string_a.lower())== sorted(string_b.lower())
      

print(is_anagram())



print("\nRETO 2 - FIBONACCI\n")


'''
Reto #2: LA SUCESIÓN DE FIBONACCI
DIFÍCIL | Publicación: 10/01/22 | Resolución: 17/01/22


 Escribe un programa que imprima los 50 primeros números de la sucesión
 de Fibonacci empezando en 0.
 - La serie Fibonacci se compone por una sucesión de números en
   la que el siguiente siempre es la suma de los dos anteriores.
   0, 1, 1, 2, 3, 5, 8, 13...


   valor1 ; valor2 ; valor3 ; valor4 ; valor5 ; valor6
   prev=0   next=1   fib=2                       --> 1 Iteracion ; print = 0
            prev=1   next=2    fib=3             --> 2 Iteracion ; print = 1
                     prev=1    next=2            --> 3 Iteracion ; print = 1
                               prev=3            -->  4 Iteracion ; print = 3
'''                      



def fibonacci ():
    prev = 0
    next = 1
    for index in range(50):
        print(prev)
        fib = prev+next
        prev=next
        next=fib

        

fibonacci()


print("\nRETO 3 - NUMEROS PRIMOS\n")


'''
Reto #3: ¿ES UN NÚMERO PRIMO?
MEDIA | Publicación: 17/01/22 | Resolución: 24/01/22


 Escribe un programa que se encargue de comprobar si un número es o no primo.
 Hecho esto, imprime los números primos entre 1 y 100.
/
'''

def is_prime(final_number):

    for number in range (1,final_number):
        if number >=2:
            is_divisible = False
            for index in range(2,number):
                if number%index==0:
                    is_divisible=True
                    break
            
            if not is_divisible:
                print(number,"Is prime")

is_prime(10)



print("\nRETO 4 - AREA DE UN POLIGONO\n")


'''
Reto #4: ÁREA DE UN POLÍGONO
FÁCIL | Publicación: 24/01/22 | Resolución: 31/01/22


 Crea una única función (importante que sólo sea una) que sea capaz
 de calcular y retornar el área de un polígono.
 - La función recibirá por parámetro sólo UN polígono a la vez.
 - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 - Imprime el cálculo del área de un polígono de cada tipo.

 Área de un Triángulo:

                        Área = base * altura
                                _____________
                                    2


                                    
Área de un cuadrado:

                        Área = lado * lado




Área de un rectángulo = 

                        Área = base * altura

                                    '''

def polygon_area():
    print('''
             1 - Triángulo
             2 - Cuadrado
             3 - Rectángulo
    ''')

    option = int(input("Choice option: "))

    if option == 1:
        base = int(input("Enter base of triángle: "))
        height = int(input("Enter height of triángle: "))
        print ("The area of triangle is ",(base*height)//2)

    elif option == 2:
        side = int(input("Enter side of square: "))
        print ("The area of square is ",side*side)
    
    elif option == 3:
        base = int(input("Enter base of rectangle: "))
        height = int(input("Enter height of rectangle: "))
        print ("The area of rectangle is ",base*height)

    else:
        print ("choice 1, 2, 3")


polygon_area()



print("\nRETO 5 - CALCULAR EL ASPECT RATIO DE UNA IMAGEN\n")


'''
Reto #5: ASPECT RATIO DE UNA IMAGEN
DIFÍCIL | Publicación: 01/02/22 | Resolución: 07/02/22


 Crea un programa que se encargue de calcular el aspect ratio de una
 imagen a partir de una url.
 - Url de ejemplo: https://raw.githubusercontent.com/mouredev/
   mouredev/master/mouredev_github_profile.png
 - Por ratio hacemos referencia por ejemplo a los "16:9" de una
   imagen de 1920*1080px.


'''


print("\nRETO 6 - INVIRTIENDO CADENAS\n")

'''
Reto #6: INVIRTIENDO CADENAS
FÁCIL | Publicación: 07/02/22 | Resolución: 14/02/22


 Crea un programa que invierta el orden de una cadena de texto
 sin usar funciones propias del lenguaje que lo hagan de forma automática.
 - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"


'''

def reverse_chain():
    string = input("Enter a string: ")
    print("The reverse string: ", string[::-1])
    

reverse_chain()



def reverse():
    text = input("Enter a text: ")
    reversed_text=''
    for index in range(0,len(text)):
        reversed_text += text[len(text)-index-1]
       
    print(reversed_text)

reverse()