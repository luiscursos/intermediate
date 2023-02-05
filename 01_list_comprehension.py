### List Comprehension ###

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]

my_list = [i for i in range(8) ]

my_range = range(8)
print(list(my_range))

my_list = [i for i in range(8)]


def sum(numero):
    return numero+5

my_new_list=[sum(i)for i in range(8)]
print(my_new_list)

