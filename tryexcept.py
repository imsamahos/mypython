try:
  num = int(input("Enter a number: "))

  if num%3==0:
   print("Buzz")
  elif num%5==0:
   print("Fizz")
  else:
   print("Kuchh Bhi")
    
except:
  print("Not a valid number")