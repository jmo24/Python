'''
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', 
then your program should print

Longest substring in alphabetical order is: abc

For problems such as these, do not include raw_input statements or define the 
variable s in any way. 
Our automated testing will provide a value of s for you - so the code you 
submit in the following box should assume s is already defined. If you are confused by
this instruction, please review L4 Problems 10 and 11 before you begin this
problem set.

Note: This problem is fairly challenging. We encourage you to work smart. 
If you've spent more than a few hours on this problem, we suggest 
that you move on to a different part of the course. If you have time, 
come back to this problem after you've had a break and cleared your head.
'''

import string
allletters = string.ascii_lowercase
#print allletters

letter_map = []
for i in allletters:
    letter_map.append(i)

#print letter_map[k]

#s = 'azcbobobegghbcdggbcgghakl'
#s = 'abcabcdabcdea'
#s = 'azcbobobegghakl'
#s='bdebcdbed'
#s='dpfjupxvzffvxnh'
#s='drxkwusluwsjzuilapxmkwmz'
#s='qvjzqayqnthb'
#s='gjeacvhdvy'
#s='whglocnckzsfexrqwxhbu'
s='rnkhhdhpgqibomtwqra'
new_list = []

for i in s:
    new_list.append(i)
    
print new_list
    
letter_map_length = len(letter_map)
#print letter_map_length


def locate_letter(x):
    k=0
    while k < letter_map_length:
        if x == letter_map[k]:
            x = k
            return x
        k = k + 1

new_list_number = []
for j in new_list:
    #print locate_letter(j)
    new_list_number.append(locate_letter(j))
    
#print new_list_number
#print new_list

new_list_number_length = len(new_list_number)

#print new_list_number_length

#print locate_letter('j') 

initial = 0
#last = 1

#s = 'azcbobobegghakl'
'''
sublist = []
while initial < new_list_number_length:
    last = 1
    final_string = new_list[initial]
    #print "loop1 " + final_string
    while last < new_list_number_length:
        #print initial,last
        #final_string = final_string + new_list[last]
        #print "loop2 " + final_string
        if new_list_number[last] >= new_list_number[initial]:
            final_string = final_string + new_list[last]
            #print "if " + final_string
            last = last + 1
        else:
            break
        last = last + 1
    #print sublist
    initial = initial + 1
    #print new_list_number[initial]
'''

'''
sublist = []
while initial < new_list_number_length:
    last = initial + 1
    print last
    final_string = new_list[initial]
    if new_list_number[initial] <= new_list_number[last]:
        final_string = final_string + new_list[last]
        print "if: " + final_string
        while last < new_list_number_length:
            if new_list_number[last] >= 
            final_string = final_string + new_list[last]
            print final_string
            last = last + 1
            #
    else:
        break
    initial = initial + 1
   '''     



#print final_string
'''
for i in new_list_number:
    j = i + 1
    final1 = [i]
    for j in new_list_number:
        print i, j, final1
    #print i

'''
print new_list_number
print new_list
answer = ''
temp = ''
answer_length = 0
temp_length = 0
#s = 'dpfjupxvzffvxnh'
sum =0
temp_sum =0 

i = 0
for x in new_list:
    #print x
    #print i
    if i == 0:
        temp = new_list[i]
    else:
        print "new_list " + str(new_list[i]) +" " + str(new_list_number[i]) + " " + str(new_list[i-1]) + " " + str(new_list_number[i-1]) + " " + temp
        #print new_list_number[i-1]
        if new_list_number[i] >= new_list_number[i-1]:
            temp = temp + new_list[i]
            temp_sum = temp_sum + new_list_number[i]
        else:
            print "1 "  + temp + " " + answer
            if len(answer) == len(temp):
                temp = new_list[i]
            if len(answer) < len(temp):
                answer_length = len(temp)
                answer = temp
                #print "test " + answer + " " + temp
                temp = new_list[i]
                #print "test1 "  + answer + " " + temp
                #print i
                sum = temp_sum
                temp_sum = 0
            else:
                temp = new_list[i]
    i = i + 1
    
if len(temp) > answer_length:
    answer = temp




    
    

            
print answer
            