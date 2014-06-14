def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    #result = 10
    if aStr == '':
    	#result = 0
    	#print 'if'
    	return 0
    else:
    	#print result
    	#print aStr
    	#print 'else'
    	#result += 1
    	return 1 + lenRecur(aStr[:-1])
    	#result += 1
    	

print lenRecur('hello')
#print lenRecur('0')
#print lenRecur('')