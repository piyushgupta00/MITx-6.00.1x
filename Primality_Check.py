# Different functions to print prime numbers in different ways....

def checkPrimeNumber(number):
  '''input has to be an positive interger, checks whether a number is prime
  or not, retruns Boolean'''
  primeflag=0
  for i in range(2,(number//2)+1):
    
    #can also be done as range(2,(number)**0.5+1) , check web resources for more efficient methods
    #like expressing the number as 6k+1 or 6k-1 then doing the division test or implementing the fermat's little theorem algorithm
      if number%i==0:
          primeflag=1
          break
  if primeflag==1:
      return False
  else:
      return True


def printPrimeSeq(t):
      '''prints a list of prime numbers in the given 2-t range'''
      primeseq=[]
      for i in range(2,t+1):
          if checkPrimeNumber(i):
              print("Prime Found: ",i)
              primeseq.append(i)
          else:
              continue
      print(primeseq)
      return print("The last prime in the sequence is", primeseq[-1])


def nthPrimenumber(n):
    '''Prints a list of first n prime numbers
    then returns the nth prime number in the prime number sequence'''
    primeseq=[]
    i=2
    while len(primeseq)!=n:
        if checkPrimeNumber(i):
          #print("Prime Found: ",i)
          primeseq.append(i)
          i=i+1
          continue
        else:
          i+=1
          continue
    #print(primeseq)
    return primeseq[-1]

def genPrime():
    '''generator function to print one prime number at a time'''
    currentprimenumber=0
    startprime=1
    while True:
        
        currentprimenumber=nthPrimenumber(startprime)
        yield currentprimenumber
        startprime=startprime+1



def genPrimesFn1():
    '''Function to return 100 prime numbers'''
    primes = []   # primes generated so far
    last = 1      # last number tried
    while len(primes) < 100:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
    return primes

def genPrimesFn2():
    '''Function to print every 10th prime 
    number, until you've printed 20 of them.'''
    primes = []   # primes generated so far
    last = 1      # last number tried
    counter = 1
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            counter += 1
            if counter % 10 == 0:
                # Print every 10th prime
                print(last)
            if counter % (20*10) == 0:
                # Quit when we've printed the 10th prime 20 times (ie we've
                # printed the 200th prime)
                return



def genPrimesFn3():
    '''Function to keep printing the prime number until the user stops the program.
    This way uses user input; you can also just run an infinite loop (while True)
    that the user can quit out of by hitting control-c'''
    primes = []   # primes generated so far
    last = 1      # last number tried
    uinp = 'y'    # Assume we want to at least print the first prime...
    while uinp != 'n':
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            print(last)
            uinp = input("Print the next prime? [y/n] ")
            while uinp != 'y' and uinp != 'n':
                print("Sorry, I did not understand your input. Please enter 'y' for yes, or 'n' for no.")
                uinp = input("Print the next prime? [y/n] ")
            
        
