shoplist = ['apple','mango','carrot','banana']
myName = 'anchita'

# Indexing or 'Subscription' operation #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Item -3 is', shoplist[-3])
print('Item -4 is', shoplist[-4])
#print('Item -5 is', shoplist[-5])
#Above caused IndexError: list index out of range

#Slicing operation on list
print('Item 1 to 3 is', shoplist[1:3]) #should output mango and carrot
print('Item 2 to end is', shoplist[2:]) #should output carrot and banana
print('Item 1 to -1 is', shoplist[1:-1]) #should output mango carrot
print('Item start to end is', shoplist[:]) #should output whole list

#indexing on string myName = 'anchita'
print('characters 1 to 3 is', myName[1:3]) #should output nc
print('characters 2 to end is', myName[2:]) #should output chita
print('characters 1 to -1 is', myName[1:-1]) #should output nchit
print('characters start to end is', myName[:]) #should output anchita

#adding a step on the list data structure
print shoplist[::1] 
#should output complete list
print shoplist[::2] 
# should output two steps from the start
print shoplist[::3] 
#should output three steps from the start
print shoplist[::-1] 
#should out list in reverse order

