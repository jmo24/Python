'''
('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this
 input would return the tuple ('I', 'a', 'tuple')
'''


def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    #length = len(aTup)
    #print length
    #oddTuple = ()
    i = 0
    newTuple = ()
    while i <len(aTup):
    	if i % 2 == 0:
    		#print i
    		newTuple = newTuple + (aTup[i],)
    	i = i + 1
    return newTuple



aTup = ('I', 'am', 'a', 'test', 'tuple')
print oddTuples(aTup)