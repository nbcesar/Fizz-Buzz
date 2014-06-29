#Fizz Buzz v2

print "Fizz buzz counting up to any number"

max_num = raw_input('How high should I go: ')

for n in range(1,int(max_num) + 1):
    if n % 5 == 0 and n % 3 == 0:
        print "fizz buzz"
    elif n % 5 == 0:
        print "buzz"
    elif n % 3 == 0:
        print "fizz"
    else:
        print n
