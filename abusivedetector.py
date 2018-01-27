#abusivedetector

text = raw_input("Enter some text (abusive text)")

abusivelist = ['shit','fuck','motherfucker']

value=any(i in text for i in abusivelist)
print(value)
#any(i in text for i in abusivelist)

'''
if text in abusivelist:
    print("That's an abusive term", text)
else:
    print ("Not an abusive text")
'''
