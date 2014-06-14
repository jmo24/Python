
balance = 999999
annualInterestRate = 0.18
installment = 0



def newBalanceEndOfTwelveMonths(balance,annualInterestRate,newBalance,installment):
	#installment = round(installment,2)
	for i in range(1,13):
		unpaidBalance = newBalance - installment
		Interest = unpaidBalance * (annualInterestRate/12.0)
		newBalance = unpaidBalance + Interest
	return newBalance


lower = balance/12
upper = (balance * (1 + (annualInterestRate/12.0))**12)/12.0

#print lower
#print upper

installment = 0
newBalance = balance

#lower1 = newBalanceEndOfTwelveMonths(balance,annualInterestRate,newBalance,lower)
#upper1 = newBalanceEndOfTwelveMonths(balance,annualInterestRate,newBalance,upper)
avg = (lower + upper) /2
x = 1
totalpayment = newBalanceEndOfTwelveMonths(balance,annualInterestRate,newBalance,avg)
#print avg
#print totalpayment
#print totalpayment

while x > 0:
	#print totalpayment
	#print x
	avg = (lower + upper)/2
	totalpayment = newBalanceEndOfTwelveMonths(balance,annualInterestRate,newBalance,avg)
	#print avg
	#print totalpayment
	if totalpayment < 0:
		#print "True"
		upper = avg
		#totalpayment = newBalanceEndOfTwelveMonths(balance,annualInterestRate,newBalance,avg)
		#print x
	elif totalpayment > 0.05:
		#print "true1"
		lower = avg
	else :
		#print "False"
		print round(avg,2)
		break
	#x = x + 1



#print newBalanceEndOfTwelveMonths(balance,annualInterestRate,newBalance,28128.7738994)