
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
    	base = 1
    	return base
    if exp == 1:
        return base
    return base*recurPower(base,exp-1)


print recurPower(2,0)
