s_number = 'osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen'
virus = 'anton'
result = ''
indexer = 0
flag = True

for letter in virus:
	if not flag:
		break
	for i in range(indexer, len(s_number)):
		value = s_number[i]
		if letter == value:
			result += s_number[i]
			indexer = i + 1
			break
		if i == len(s_number) - 1:
			flag = False
if result == virus:
	print('This serial number infected')
else:
	print('this serial number clear')
