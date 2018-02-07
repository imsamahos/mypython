
var=raw_input('Enter numbers splitted by a comma: ')
testSet = set() 
#Initialize an empty set

splitVar = var.split(",")

for i in splitVar:
    testSet.add(i)

print testSet
