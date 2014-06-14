#insert comment here
#u=insert second test comment here
def f(x):
	import math
	return 10*math.e**(math.log(0.5)/5.27 * x)


def radiationExposure(start, stop, step):
    if stop <= start:
        return 0
    else:
        #print start, f(start)
        return step*f(start) + radiationExposure((start+step), stop, step)



print radiationExposure(0, 5, 1)
