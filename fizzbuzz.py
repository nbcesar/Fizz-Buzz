#Fizz Buzz v1

print "Fizz buzz counting up to 100"

for n in range(1,101):
    if n % 5 == 0 and n % 3 == 0:
        print "fizz buzz"
    elif n % 5 == 0:
        print "buzz"
    elif n % 3 == 0:
        print "fizz"
    else:
        print n
