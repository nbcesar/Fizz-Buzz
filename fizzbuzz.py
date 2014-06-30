#Fizz Buzz v2
import sys

print "Fizz buzz counting up to any number"

def divisible(base, div):
    if base % div == 0:
        return True
    else:
        return False

def fizzbuzz(upper_limit=100):
    
            
    for n in range(1,upper_limit + 1):
        if divisible(n,5) and divisible(n,3):
            print "fizz buzz"
        elif divisible(n,5):
            print "buzz"
        elif divisible(n,3):
            print "fizz"
        else:
            print n


if __name__ == '__main__':
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
    fizzbuzz(number)

