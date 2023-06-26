import random


def get_list(length):
	return [random.randint(0, 20) for i in range(0, length)]


list_1 = get_list(20)
list_2 = get_list(20)
list_1 = set(list_1)
list_2 = set(list_2)
print(sorted(list_1.intersection(list_2)))
