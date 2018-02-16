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
  if num == 10:
    raise IOError("testing ioerror") # to mock an exception IOError
  if num == 20:
    raise ValueError("testing valueerror") # to mock an exception ValueError
  fizzbuzz(num)
  
except ValueError as valueError:
  #log here about the exception
  print("Input is not valid. Exception: {0}".format(valueError))
  print("Not a valid number")
  
except IOError as ioError:
  #log here about the exception
  print("Input is not valid. Exception: {0}".format(ioError))
  print("Not a valid number")
  
  # parent class Exception ? 