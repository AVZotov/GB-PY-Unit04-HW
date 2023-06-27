import random


def get_int():
	flag = True
	result = 0
	while flag:
		try:
			result = int(input("Enter your value: "))
			return result
		except ValueError:
			print('Error. Please enter correct digit! ', end='')


def get_list(value):
	return [random.randint(0, 10) for _ in range(value)]
	
	
bushes_quantity = get_int()
berries = get_list(bushes_quantity)
print(berries)

index = 0
sum_berries = 0
result = {}
key = ''

while index < bushes_quantity:
	if index == bushes_quantity - 1:
		sum_berries = berries[index] + berries[index - 1] + berries[0]
		key = f'{index - 1}:{index}:0'
	else:
		sum_berries = berries[index] + berries[index - 1] + berries[index + 1]
		key = f'{index - 1}:{index}:{index + 1}'
	result[key] = sum_berries
	index += 1
max_harvest = max(result.values())
position = [i for i in result if result[i] == max_harvest]
print(f'Max harvest locations: {position}, berries amount: {max_harvest}')
# position = max(result, key=result.get)
# max_harvest = result[position]
# print(f'Max harvest locations: {position}, berries amount: {max_harvest}')

