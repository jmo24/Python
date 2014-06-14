balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

minimumPayment = balance * ( monthlyPaymentRate / 100 )
unpaidBalance = balance - minimumPayment
Interest = (annualInterestRate/1200.0) * unpaidBalance
newBalance = unpaidBalance + Interest


totalPaid = 0
for i in range(1,13):
	if i == 1:
		minimumPayment = balance * ( monthlyPaymentRate)
		unpaidBalance = balance - minimumPayment
		Interest = (annualInterestRate/12.0) * unpaidBalance
		newBalance = unpaidBalance + Interest
		print "Month: " + str(i)
		print "Minimum monthly payment: " + str(round(minimumPayment,2))
		print "Remaining balance: " + str(round(newBalance,2))
		#print Interest
		#print newBalance
		#print "\n"
		totalPaid = totalPaid + minimumPayment
	else:
		#print newBalance
		minimumPayment = newBalance * ( monthlyPaymentRate )
		unpaidBalance = newBalance - minimumPayment
		Interest = (annualInterestRate/12.0) * unpaidBalance
		newBalance = unpaidBalance + Interest
		print "Month: " + str(i)
		print "Minimum monthly payment: " + str(round(minimumPayment,2))
		print "Remaining balance: " + str(round(newBalance,2))
		#print minimumPayment
		#print unpaidBalance
		#print Interest
		#print newBalance	
		#print "\n"	
		totalPaid = totalPaid + minimumPayment

print "Total Paid: " + str(round(totalPaid,2))
print "Remaining Balance: " + str(round(newBalance,2))



