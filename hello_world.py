import sys
sys.stdout.write("Hello world!\n")
sys.stdout.write("Progress:\n")
for progress in range(1,100001):
	z=progress/1000
	x=int(z/2)
	st=u'\u2588'*x+'_'*(50-x)
	sys.stdout.write('\x1b[6;30;42m%s\x1b[0m\r'%(st))
sys.stdout.write("\n")
	
	

