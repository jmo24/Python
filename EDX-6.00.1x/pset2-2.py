balance = 4773
annualInterestRate = 0.2
installment = 0
newBalance = balance


installment = 0
#twelvemonth = 0
while installment < balance/2:
	#twelvemonth = 0
	newBalance = balance
	for i in range(1,13):
		#print twelvemonth
		#print newBalance
		#print i
		unpaidBalance = newBalance - installment
		Interest = unpaidBalance * (annualInterestRate/12.0)
		newBalance = unpaidBalance + Interest
		#twelvemonth = twelvemonth + installment + Interest
	#print installment, " " , twelvemonth
		#print newBalance
	if newBalance <= 0:
		print installment
		break
	else:
		installment = installment + 10
'''

def callcheck(balance,annualInterestRate,newBalance,installment):
	newBalance = balance
	for i in range(1,13):
		unpaidBalance = newBalance - installment
		Interest = unpaidBalance * (annualInterestRate/12.0)
		newBalance = unpaidBalance + Interest
		if newBalance <=0 and i < 12:
			break
		else:
			print newBalance

while installment < balance/2:
	newBalance = balance
	#print newBalance
	newBalance = callcheck(balance,annualInterestRate,newBalance,installment)
	#print newBalance
	if newBalance <= 0:
		print installment
		break
	else:
		installment = installment + 10

		'''