def smart_divide(func):
   def inner(*args, **kwargs):
      print("I am going to divide",args[0],"and",args[1])
      if args[1] == 0:
         print("Whoops! cannot divide")
         return

      return func(*args, **kwargs)
   return inner

@smart_divide
def divide(a,b):
    return a/b
    
    
    #*args is pointer that is in tuples
    #**kwargs is pointer that is dictonary
    
