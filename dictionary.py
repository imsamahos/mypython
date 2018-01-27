ab = {
'anchita':'redmond',
'ankit':'frankfurt',
'anamika':'belleve',
'deepika':'mumbai',
'priyanka':'mumbai'
}

print 'length of dictionary is', len(ab)
#deleting a key value pair
del ab['anchita']
print 'length of dictionary is, (after delete operation)', len(ab)
#adding a key value pair
ab['divya'] = 'bangalore'
print 'length of dictionary is, (after insert operation)', len(ab)

if 'divya' in ab:
    print 'Divya lives in ', ab['divya']
