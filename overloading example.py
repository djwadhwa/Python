def foo(*args, **kwds):
    if len(args)==1:
        return 1
    elif (len(args) == 2 ):
        return args[0] + args[1]
        
myargs = [3,4]

print (foo(*myargs))