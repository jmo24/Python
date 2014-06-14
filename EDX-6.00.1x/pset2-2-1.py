
balance = 3329
annualInterestRate = 0.2
installment = 0



def callcheck(balance,annualInterestRate,newBalance,installment):
	#newBalance = balance
	for i in range(1,13):
		unpaidBalance = newBalance - installment
		Interest = unpaidBalance * (annualInterestRate/12.0)
		newBalance = unpaidBalance + Interest
		#print i
	return newBalance
	'''	if newBalance <=0 and i < 12:
			break
		else:
			print i, newBalance
'''

installment = 0
while installment < balance:
	newBalance = balance
	#print newBalance
	newBalance = callcheck(balance,annualInterestRate,newBalance,installment)
	print newBalance
	if newBalance <= 0:
		#print installment
		break
	else:
		installment = installment + 10

print installment