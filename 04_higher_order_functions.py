### HIGHER ORDER FUNCTIONS ###


def sum_one (value):
    return value + 1

def sum_five (value):
    return value + 5

def sum_two_values_and_one (first_value, second_value):
    return sum_one (first_value + second_value)


print(sum_two_values_and_one(5,2))

# Dentro de f_sum pasamos la funcion sum_five

def sum_two_values_and_add_values(first_value, second_value,f_sum):
    return f_sum (first_value+ second_value)

print(sum_two_values_and_add_values(5,2,sum_one))
print(sum_two_values_and_add_values(5,2,sum_five))





### CLOSURES ###


# Las closures son un concepto de funciones de orden superior
# Retornar funciones no valores

def sum_ten ():
    def add (value):
        return value + 10
    return add

add_closures = sum_ten()
print(add_closures(10))


def sum_ten_nums (original_value):
    def add (value):
        return value + 10 + original_value
    return add

add_closures = sum_ten_nums(1)
print(add_closures(5))


### BUILT-IN HIGHER ORDER FUNCTIONS ###

# Las funciones de orden superior pueden ejecutar otras funciones

#   Map
# Map necesita un iterable y otra función
# La función map() siempre va a necesitar un conjunto iterable y después devuelve otro iterable aplicando la funcion sobre los elementos del iterable
# Map devuelve un objeto, que tras pasarlo a una lista, podemos imprimirla


def multiply_two(number):
    return number*2

numbers = [2, 5, 10, 21, 30]

# Map a iterado sobra la lista y ha ejecutado sobre cada valor la función que hemos pasado y el objeto de resultado lo pasamos  a una lista
print(list(map(multiply_two, numbers)))
print(list(map(lambda number:number*2, numbers)))


# Map admite varios iterables con los actuar simultaneamente
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

print(list(map(lambda x,y:x*y, a,b)))


# Filter
# Necesitamos una función y un iterable igual que map
# Hay que pasarlo a list para poder imprimir el objeto en modo lista    
# Necesita que la funcion devuelva un True / False para saber com filtrar
def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter (filter_greater_than_ten, numbers)))




