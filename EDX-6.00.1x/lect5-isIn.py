def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr == '':
    	return False
    if len(aStr) == 1:
    	return aStr == char
    middle = len(aStr)/2
    if char == aStr[middle]:
    	return True
    elif char < aStr[middle]:
    	return isIn(char,aStr[0:middle])
    else:
    	#print aStr[middle:]
    	#print 'echo'
    	return isIn(char,aStr[middle:])


print isIn('a', '')
print isIn('n', 'hlmrttwwz')
print isIn('f', 'cfktuy')
print isIn('x', 'ehhijnnoqqqtuuvvyzz')
print isIn('x', 'acddggillmsxy')
print isIn('x', 'abjlmmmnpruwx')
