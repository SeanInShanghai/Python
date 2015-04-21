import urllib
import time
import random
print "Auto Click the WebPage for Click-Num..."
for i in range(6):
	fs = urllib.urlopen(r'http://ubc.ecnu.edu.cn')
	print 'The ', i, 'time click done...'
	time.sleep(int(random.uniform(1, 5)))
print 'Auto Click WebPage Done...' 
