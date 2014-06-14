def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
    	return a 
    if a == 0:
    	return b
    return gcdRecur(b,a%b)

print gcdRecur(2,12)
print gcdRecur(17,12)
print gcdRecur(17,12)
