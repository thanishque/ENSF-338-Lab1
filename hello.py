import sys

def do_stuff():
    if len(sys.argv) != 2:
        print("No command line args! try: filepathname <number>")
        return
    number = int(sys.argv[1])
    print (number)
    if number < 2:
        print("yes")
    else:
        for i in range(2, number):
            if number % i == 0:
                print("No")
                return
        print("Yes")


do_stuff()
#The program is determining if a number is prime or not. 
#it takes command line args but there is no check whether command line arg is valid added that.
#The error was that any number less than 2 is a prime number but before it printed no so updated that to yes.
