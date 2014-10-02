

def printnumbers(num1, num2):
    numbers = []

    for i in range (0, num1):
        print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers[::num2]:
        print num

printnumbers(10, 5)