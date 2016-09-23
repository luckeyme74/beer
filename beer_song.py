def num_beers(n):
    print (str(n) + " bottles of beer on the wall")
    print (str(n) + " bottles of beer")
    print ("Take one down pass it around")
    print (str(n-1)+" bottles of beer on the wall!")
    if n > 1:
        num_beers(n - 1)
num_beers(99)
