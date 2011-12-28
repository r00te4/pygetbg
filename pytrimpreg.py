import re
import sys
print "Welcome to use this tol  ^_^"
str=raw_input('Enter the tags \n')
#print str
#exit(0)
#str=u'<form action="login.jsp" method="post" name="form1" id="form1"  onSubmit="return check();">';
str=str.replace('\"','\\"')
str='\"#'+str+'#\"'
print str