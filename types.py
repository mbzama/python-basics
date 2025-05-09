print('Integer and Float Types Demo')
a=2
b=4.5

print('Sum: ', a+b)
print('Diff: ', a-b)
print('Div: ', a/b)
print('Round Div: ', round(a/b, 2))
print('Mul: ', a*b)
print('Mod: ', a%b)
print('Floor Div: ', a//b)
print('Power: ', a**b)
print('Type of a: ', type(a))
print('Type of b: ', type(b))
print('Type of a+b: ', type(a+b))
print('------------------')

print('String Type Demo')
a="ice cream"

print('a: ', a)
print('a[0]: ', a[0])
print('a[1:3]:', a[0:3])
print('a[1:]:', a[4:])
print('len(a):', len(a))

noofstates=25
statesTxt = 'No of States: ' + str(noofstates)
print(statesTxt)

print('List Type Demo')
a=[1,2,3,4,5]
print('a: ', a)

item1='egg'
item2='milk'
item3='bread'
item4='butter'
groceries = ["veggies"]
print('Items: ', groceries)
groceries.append(item1)
groceries.append(item2)    
groceries.append(item3)
groceries.append(item4)
print('Items: ', groceries)
print('Items[0]: ', groceries[1:3])
groceries[1]='fruit' # replace egg with fruit
print('Items: ', groceries)
groceries.insert(0, 'chocolate')
print('Items: ', groceries)

bathroom = ['soap', 'shampoo', 'toothpaste']
print('Bathroom Items: ', bathroom)

allItems = groceries + bathroom
print('All Items: ', allItems)
print('No of Items: ', len(allItems))

result = 'milk' in allItems
print('Is milk in all items: ', result)
result = 'apple' in allItems
print('Is apple in all items: ', result)