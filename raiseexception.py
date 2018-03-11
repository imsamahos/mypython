def methodLevel0(inputNumber):
  try:
    print("this method at the lowest level does some magic but caused some error. We call it as value error and throw it to the callee")
    raise ValueError("ValueError from methodLevel0")
  except Exception as exception:
    raise exception


def methodLevel1(someInput):
  
  try:
    print("this method at the  level 1 does some magic.")
    methodLevel0(someInput)
  except Exception as exception:
    raise exception


try:
  print("main program")
  input = input("Any input:")
  methodLevel1(input)
  
except Exception as exception:
  #log here about the exception
  #library  - async way to push logs into another system
  # logging.warning('And this, too')
  ##### async way to do logging - dispatch this for me without waiting
  #and then show user a friedly message or any appropriate msg so that user can take further action
  #print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(exception).__name__, exception.args))
   print("We display error directly to our consumers:{0}".format(exception))