
'''def Dog:
def Pub:
    age;
    name;
    color;




def Lab:
    age;
    name;
    color;


    p1= Pub ("Spot",2, "black")
    p2 = Pub ("Mickey", 4, "white")
    l1 = Lab ("Smokey", 6, "grey")
    l2 = Lab ("Dian", 6, "white")

'''

class Pub:
    
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

class Lab:
    
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name



myPubList = list() 
myLabList = list()

p = Pub('Spot')
print("Pub Name:{0}".format(p.getName()))
myPubList.append(p)

p = Pub('Spooky')
print("Pub Name:{0}".format(p.getName()))
myPubList.append(p)

l = Lab('Lobby')
print("Lab Name:{0}".format(l.getName()))
myLabList.append(l)

l = Lab('Dobby')
print("Lab Name:{0}".format(l.getName()))
myLabList.append(l)


print('My vet list')
print('Pub list')

for pub in myPubList:
    print(pub.getName())

print('Lab list')

for lab in myLabList:
    print(lab.getName())


