billAmount=0
tipRate=0
tip=0
total=0
gstAmount=0

billAmount = int(raw_input('Enter the bill amount: '))
tipRate = int(raw_input('Enter the tip rate: '))


tip = billAmount * tipRate/100
total =  billAmount + tip
gstAmount = int(total * 0.05)

print('The tip is', tip)
print('The total is', total)
print('total gst amt is', gstAmount)
