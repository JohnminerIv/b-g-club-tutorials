# day_1/types.py

"""
There are many different types of data that are availible to you in python. Can
anyone raise their hand and name one?
"""

yes = 19 < 21
print(yes) # True
print(yes == True) # True
print(yes == False) # False

print('-----------------------------------------------------------------------')

ten = 10
print(ten) # 10
print(ten + 2) # 12
print(2 - ten) # -8

print('-----------------------------------------------------------------------')

john = 'John Miner'
print(john) # John Miner
print(john + ' IV') # John Miner IV
print(f'My name is {john}') # My name is John Miner
print(john[0]) # J
print('M' in john) # True

print('-----------------------------------------------------------------------')

building_materials = ['straw', 'sticks', 'bricks']
print(building_materials) # ['straw', 'sticks', 'bricks']
building_materials.append('mud')
print(building_materials) # ['straw', 'sticks', 'bricks', 'mud']
print(building_materials[0]) # 'straw'
print(building_materials[0][0]) # s

print('-----------------------------------------------------------------------')

ages = {'John': 20, 'Rick': 52}
print(ages) # {'John': 20, 'Rick': 52}
print(ages['John']) # 20
ages['Morty'] = 15
print(ages) # {'John': 20, 'Rick': 52, 'Morty': 15}

print('-----------------------------------------------------------------------')

letters = {'a', 'b', 'c', 'b'}
print(letters) # {'b', 'c', 'a'}
letters.add('t')
print(letters) # {'b', 'c', 'a', 't'}
print('a' in letters) # True
print('z' in letters) # False

"""
Sometimes you can turn types into other types
"""
print('-----------------------------------------------------------------------')

print(int(yes))
print(str(ten))
print(list(john))
print(set(john))
print(set(building_materials))
