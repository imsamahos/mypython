shoplist = ['apple','mango','banana','carrot','pineapples']
print('I have', len(shoplist), 'items to purchase')

print('These items are', shoplist)
print ('these items are')
for item in shoplist:
    print(item)
print('\n I also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)
for item in shoplist:
    print(item)

print('I will sort my list now')
shoplist.sort()
print ('The sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print ('I bought the ', olditem)
print('My shopping list is now', shoplist)
