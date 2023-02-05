        ### LAMBDAS ###


# Las lambdas son funciones anónimas.
# Puede tener parametros de entrada -> first_value, second_value
# Después de los dos puntos indicamos que operacion hacer con los parametros de entrada
# Asignamos la labda a una variable y después cuando sea llamada pasamos los valores

sum_two_values = (lambda first_value, second_value:first_value+second_value)

print(sum_two_values(5,2))

multiply_values = lambda  first_value, second_value:first_value * second_value - 3
print(multiply_values(5,2))


def sum_three_values(values):
    return lambda  first_value, second_value:first_value * second_value + values


print(sum_three_values(5)(2,4))
