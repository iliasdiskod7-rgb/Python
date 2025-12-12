def digit_sum(x):
    s=0
    while x!=0:
        s=s+x%10
        x=x//10
    return s
def sum_sequence(n, term):
        """A8roisma arxikwn orwn akolou8ias                                                       
        n -- deikths teleutaiou orou (deikths prwtou = 1)               
        term -- synarthsh: term(i) einai o i-ostos oros                 
     
        Epistrefei tin timi term(1) + term(2) + ... + term(n).          
        """
        i, sum = 2, term(1)
        while i <= n:
             sum += term(i)
             i += 1
        return sum
def alternating_sum_100():
    term=lambda i:-i if i%2==0 else i
    n=100
    return sum_sequence(n,term)
def alternating_sequence_sum_100(term):
    term1=lambda i:-term(i) if i%2==0 else term(i)
    n=100
    return sum_sequence(n,term1)
def alternating_sum_squares_100():
    return  alternating_sequence_sum_100(lambda i:i**2)
def reserve_args(f):
     def g(x,y):
          return f(y,x)
     return g
def sum_sequence_rec(n,term):
     if n==0:
          return 0
     else:
          return term(n) + sum_sequence_rec(n-1,term)
       
def print_digits(x):
    if x<10:
         print(x)
    else:
         print_digits(x//10)
         print(x%10) 
     
    