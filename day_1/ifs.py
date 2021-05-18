# day_1/ifs.py

"""
If statements can control the flow of your application.
"""

yes = True
no = False

if yes:
    print('This will print because yes is True')

if no:
    print('This wont print because no is False')


ben = 10

if ben == 10:
    print('Ben is equal to ten.')

if ben != 10:
    print('this wont print because ben is equal to 10')

if 11 > ben:
    print('11 is greater than ben')

if ben < 10:
    print('this wont print because ben is equal to 10')

if ben >= 10:
    print('this will print because ben is equal to 10')



print('-----------------------------------------------------------------------')
"""
Else statments can come after an if statement if you want something to happen
even if your first statement doesn't work
"""


if ben > 10:
    print('this wont print')
else:
    print(f'ben is not greater than 10')

"""
Elifs are similar but to else's but the have conditions too, and they only
execute the first statement to be true.
"""

if ben < 2:
    print('Baby')
elif ben < 10:
    print('Child')
elif ben < 13:
    print('Tween') # Only tween will print because its the first if or elif statement to be true
elif ben < 20:
    print('Teen')
else:
    print('Old')

print('-----------------------------------------------------------------------')

if ben < 2:
    print('Baby')
if ben < 10:
    print('Child')
if ben < 13:
    print('Tween') # Now this will print tween 
if ben < 20:
    print('Teen') # Now this will print teen
if ben < 100:
    print('Old') # Now this will print old
