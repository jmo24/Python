#!/usr/bin/env python


# version 1.0
# 06/07/2014
### How-to-run:  python2.7 jtac.py 2014-0602-0555
# Basically checking if the file has been uploaded to ftp, and then copying the contents of the file to larger file location. 
# This can be done only when there are no local files present.
# If a folder already exists, then it will exit giving an error
# 'ret' is basically return
# Refer: Python for Unix and Linux System Admin - Subprocess.


# version 1.1
# 06/07/2014
# changed from using cp -R to rsync
# Refer: http://www.thegeekstuff.com/2010/09/rsync-command-examples/

# version 1.2
# 06/07/2014
# added support for 'argparse'
# http://www.pythonforbeginners.com/argparse/argparse-tutorial

# version 1.3
# 06/07/2014
# Removed hard coded jtactools server IP. Changed it to variable jtactools


# version 1.5
# 06/17/2014
# Moved to reusable functions. All old functions removed.

# version 2.0
# 06/17/2014
# Support for butter added. Ugly hack, due to lack of permissions in playing around in the butter folder.


# version 2.1
# 06/17/2014
# Support for butter added. Ugly hack, due to lack of permissions in playing around in the butter folder.


from sys import argv
import subprocess
import argparse

#script,case = argv

parser = argparse.ArgumentParser(description='Run program using: \n python jtac.py 2014-0602-0555 [-b]')
parser.add_argument('case', help='Case number')
parser.add_argument('-b', '--butter', help='Give this option if you want to sync from large to butter', action='store_true')
parser.add_argument('-a', '--attachment', help='Give this option if you want to sync from Case Manager to both large and butter', action='store_true')
parser.add_argument('-e', '--ebpg', help='Use this option, to avoid storing under EPBG in butter. Legacy support', action='store_true')
args = parser.parse_args()


case = args.case
print "\n"
print "#########################################################################"
print 'Case number is %s' %case
print 'Butter option is %s' %args.butter
print '\n'

jtactools = '172.17.31.81'
large_directory = '/volume/CSdata/jmohamed/cases/'
butter_directory = '/volume/casedata/EPBG/'
ftp_directory = '/volume/ftp/pub/incoming/'

if args.ebpg == True:
	butter_directory = '/volume/casedata/'
else:
	butter_directory = '/volume/casedata/EPBG/'

print 'Using jtac-tools server %s' %jtactools
print 'FTP location is %s%s' %(ftp_directory,case)
print 'Large location is %s%s' %(large_directory,case)
print 'Butter location %s%s' %(butter_directory,case)
print "\n\n"

def check_directory(location, case):
	location_ret = subprocess.call( "ssh %s 'ls -la %s%s'" %(jtactools,location,case), shell=True)
	#print ftp_ret
	return location_ret

def copy_to_location(location1, location2, case): #use this function when doing initial copy
	print ""
	mkdir_ret = subprocess.call("ssh %s 'mkdir %s%s'" %(jtactools,location2,case), shell=True)
	#mkdir_ret = subprocess.call("ssh %s 'mkdir %s%s'" %(jtactools,location2,case), shell=True)
	copy_ret = subprocess.call("ssh %s 'rsync -azvi --progress %s%s/ %s%s/'" %(jtactools,location1,case,location2,case), shell = True)
	#print mkdir_ret
	#print copy_ret
	if mkdir_ret == 0:
		return copy_ret
	else:
		return "Error! In making directory at %s" %(location2)


def sync_files(location1, location2, case): #use this function to sync between locations. Only the new files are copied.
	print "\n"
	print "#########################################################################"
	#copy_ret = subprocess.call("ssh 172.17.31.81 'cp -R /volume/ftp/pub/incoming/%s/ /volume/CSdata/jmohamed/cases/%s/'" %(case,case), shell = True)
	sync_ret = subprocess.call("ssh %s 'rsync -azvi --progress %s%s/ %s%s/'" %(jtactools,location1,case,location2,case), shell = True)
	if sync_ret == 0:
		return sync_ret
	else:
		return "Error! In Syncing directory between %s and %s" %(location1, location2) 


#ftp_ret = check_ftp_directory(case)
#large_ret = check_large_directory(case)
#copy_ret = copy_ftp_large(case)

def scp_files(location1, location2, case): #use this function to sync to butter. Hack because of lack of permission on the jtactools server.
	print ""
	scp_ret = subprocess.call("ssh %s 'scp -r %s%s/ %s%s/'" %(jtactools,location1,case,location2,case), shell = True)
	if scp_ret == 0:
		return scp_ret
	else:
		return "Error! In SCP files between between %s and %s" %(location1, location2) 



def sync(location1, location2, case): #main function
	location1_ret = check_directory(location1,case)
	location2_ret = check_directory(location2,case)
	if location1_ret == 0 and location2_ret!= 0: # if folder exists in location1 but not in the location2.
		#print location1_ret
		#print location2_ret
		location2_ret = copy_to_location(location1, location2, case)
		if location2_ret == 0:
			print "\n\n Success! Files copied from %s%s to %s%s " %(location1,case,location2,case)
		else:
			print "\n"
			print "Error! Files were not copied from %s%s to %s%s " %(location1,case,location2,case)
	elif location1_ret == 0 and location2_ret == 0: # if folder exists in both location1 and the location2.
		print "Folder exists at %s, Syncing now" %(location2)
		sync_ret = sync_files(location1, location2, case)
		#print sync_ret
		if sync_ret == 0:
			print "\n"
			print "Success! Files copied from %s%s to %s%s " %(location1,case,location2,case)
		else:
			print "\n"
			print "Error! Files could not be synced between %s%s to %s%s " %(location1,case,location2,case)
	else:
		print "\n"
		print 'Error! Folder does not exist in %s%s' %(location1,case)



sync(ftp_directory, large_directory,case)


if args.butter == True:
	scp_ret =scp_files(large_directory,butter_directory,case)
	print "\n#########################################################################"
	print "Starting butter copy"
	#print scp_ret, 'scp_ret'
	if scp_ret == 0:
		print "\nSuccess! Files copied from %s to %s%s " %(large_directory,butter_directory,case)
		print "Butter Link is \\butter\casedata\EPBG\%s\n" %(case)
	else:
		print "Issue in copying to butter location %s%s" %(butter_directory,case)




