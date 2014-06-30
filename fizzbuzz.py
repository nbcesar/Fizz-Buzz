#Fizz Buzz v2
import sys

print "Fizz buzz counting up to any number"

while True:
    try:
        if len(sys.argv) > 1:
            max_num = sys.argv[1]
        else:
            max_num = raw_input('How high should I go: ')
        number = int(max_num)
        break
    except ValueError:
        print "Must be a number"

for n in range(1,int(max_num) + 1):
    if n % 5 == 0 and n % 3 == 0:
        print "fizz buzz"
    elif n % 5 == 0:
        print "buzz"
    elif n % 3 == 0:
        print "fizz"
    else:
        print n


'''def subtractor(a, b): 
   """I subtract b from a and return the result"""  
   print "I'm a function. My name is {}".format(subtractor.__name__)
   print "I'm about to subtract {} and {}\n\n".format(a,b)
   return a - b  # i output a value by using the return statement


if __name__ == '__main__':
    subtractor(3, 2)
'''
