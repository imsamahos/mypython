def fizzbuzz(inputNumber): 
  if inputNumber%3==0:
   print("Buzz")
  elif inputNumber%5==0:
   print("Fizz")
  else:
   print("Kuchh Bhi")
  #log here that things happened successfully

try:
  num = int(input("Enter a number: "))
  fizzbuzz(num)
  
except(ValueError):
  #log here about the exception
  print("Not a valid number")