def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a < b:
    	result = a
    else:
    	result = b
    
    #result = a
    if a%result == 0 and b%result == 0:
    	return result
    else:
    	print "echo"
    	result = result - 1
    	print result
    	gcdIter(result,b)

print gcdIter(9,12)