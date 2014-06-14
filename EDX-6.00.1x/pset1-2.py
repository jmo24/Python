'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2

For problems such as these, do not include raw_input statements 
or define the variable s in any way. Our automated testing will provide 
a value of s for you - so the code you submit in the following box should
assume s is already defined. If you are confused by this instruction, 
please review L4 Problems 10 and 11 before you begin this problem set.
'''

s = 'azcbobobegghakl'
test = []
for b in s:
    test.append(b)
'''
new_list = []
a = 0
b = str(test[a]) + str(test[a+1])+ str(test[a+2])
new_list.append(b)
print "new-list"+ new_list[0]
'''

length = len(test)

new_list = []
a = 0
while a < length-2:
    b = str(test[a]) + str(test[a+1])+ str(test[a+2])
    new_list.append(b)
    a = a + 1
    
count = 0
for i in new_list:
    if i == 'bob':
        count = count + 1
        
print count
    
