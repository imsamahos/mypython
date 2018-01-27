# create a tuple with simple brackets
zoo = ('python','elephant','penguin')
print'Total animals in the zoo are',len(zoo)

new_zoo = ('monkey','camel',zoo)
print 'Number of cages in the new zoo are', len(new_zoo)
print 'The animals in the new zoo are',new_zoo
print'The animals brought from the old zoo are',new_zoo[2]
print 'The last animal brought from the old zoo is',new_zoo[2][2]

