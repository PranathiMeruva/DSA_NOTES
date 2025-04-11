#FUNCTIONS IN PYTHON
z = 43
def our_print (s):      #do no use existing keywords to give function names, throws error
    print(z)
    print(s + "helloo")

our_print("Hieee 2")
#None vs null --> None is a constant, null returns boolean

# is keyword
a = [1,2,3,4]
print(a is [1,2,3,4])   #returns boolean, checks like == 

w = 5
q = 2
w = q
q = 4
print(w)

#FUNCTIONS - TRICKS
def add(a,b = 2):     #default argument should follow nondefault, so nondefault comes first, can't assign value to 'a' first 
    return a+b
print(add(3))