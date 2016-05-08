import sys

def hello():
    name=""                 #Just an innocent variable.

    if len(sys.argv) == 1:      #If you didn't give a name.
        print ("Hello World!")

    else:                           #If you did it.
        for i in sys.argv[1:]:
            name += " "+i
        print ("Hello"+name+"!")


hello()                         #Running function.
