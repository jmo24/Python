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





from sys import argv
import subprocess
import argparse

#script,case = argv

parser = argparse.ArgumentParser(description='Run program using: \n python jtac.py 2014-0602-0555 [-b]')
parser.add_argument('case', help='Case number')
parser.add_argument('-b', '--butter', help='Give this option if you want to sync from large to butter', action='store_true')
args = parser.parse_args()


case = args.case
print args.butter


jtactools = '172.17.31.81'

def check_large_directory(case):
	large_ret = subprocess.call( "ssh %s 'ls -la /volume/CSdata/jmohamed/cases/%s'" %(jtactools,case), shell=True)
	#print large_ret, "Larger directory"
	return large_ret

def check_ftp_directory(case):
	ftp_ret = subprocess.call( "ssh %s 'ls -la /volume/ftp/pub/incoming/%s'" %(jtactools,case), shell=True)
	#print ftp_ret
	return ftp_ret


def copy_ftp_large(case):
	print ""
	mkdir_ret = subprocess.call("ssh %s 'mkdir /volume/CSdata/jmohamed/cases/%s'" %(jtactools,case), shell=True)
	#copy_ret = subprocess.call("ssh 172.17.31.81 'cp -R /volume/ftp/pub/incoming/%s/ /volume/CSdata/jmohamed/cases/%s/'" %(case,case), shell = True)
	copy_ret = subprocess.call("ssh %s 'rsync -azvi --progress /volume/ftp/pub/incoming/%s/ /volume/CSdata/jmohamed/cases/%s/'" %(jtactools,case,case), shell = True)
	#print mkdir_ret
	#print copy_ret
	if mkdir_ret == 0:
		return copy_ret
	else:
		return "Error! In making directory"

def sync_ftp_large(case):
	print ""
	#copy_ret = subprocess.call("ssh 172.17.31.81 'cp -R /volume/ftp/pub/incoming/%s/ /volume/CSdata/jmohamed/cases/%s/'" %(case,case), shell = True)
	sync_ret = subprocess.call("ssh %s 'rsync -azvi --progress /volume/ftp/pub/incoming/%s/ /volume/CSdata/jmohamed/cases/%s/'" %(jtactools,case,case), shell = True)
	if sync_ret == 0:
		return sync_ret
	else:
		return "Error! In Syncing directory"


ftp_ret = check_ftp_directory(case)
large_ret = check_large_directory(case)
#copy_ret = copy_ftp_large(case)



if ftp_ret == 0 and large_ret!= 0: # if folder exists in sftp but not in the larger location.
	#print ftp_ret
	#print large_ret
	copy_ret = copy_ftp_large(case)
	if copy_ret == 0:
		print "\n\n Success! Files copied from sftp to larger location"
	else:
		print "\n\n"
		print "Error! Files were not copied"
elif ftp_ret == 0 and large_ret == 0: # if folder exists in both sftp and the larger location.
	print "Folder exists, Syncing now"
	sync_ret = sync_ftp_large(case)
	#print sync_ret
	if sync_ret == 0:
		print "Success! Files copied from sftp to larger location"
	else:
		print "Error! Files could not be synced"
else:
	print 'Error! Folder does not exist in ftp'


def sync_function(location1, location2,case):
	if location1_ret == 0 and location2_ret!= 0: # if folder exists in location1 but not in the location2.
	#print ftp_ret
	#print large_ret
	location2_ret = copy_location(case)
		if location2_ret == 0:
			print "\n\n Success! Files copied from %s to %s location" %(location1,location2)
		else:
			print "\n\n"
			print "Error! Files were not copied"
	elif ftp_ret == 0 and large_ret == 0: # if folder exists in both sftp and the larger location.
		print "Folder exists, Syncing now"
		sync_ret = sync_ftp_large(case)
		#print sync_ret
		if sync_ret == 0:
			print "Success! Files copied from sftp to larger location"
		else:
			print "Error! Files could not be synced"
	else:
		print 'Error! Folder does not exist in ftp'











