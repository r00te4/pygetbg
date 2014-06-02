import re
import urllib
print "Usage pygetbg.py /path/to/remote/imgages/dir"
f2 = open("./style.css", "r")
str2=f2.read()
print str2
print "*"*10
pattern = re.compile(r'.jpg')
imglist = re.findall(r'url\(..\/images\/(.*).gif',str2)
#imgdir="http://www.tsinghua.edu.cn/publish/th/images/"
imgdir=sys.argv[1]
print imgdir
print imglist
urllist=[]
for img in imglist:
	url=imgdir+img+".jpg"
	urllib.urlretrieve(url,'d:\\temp\\getcssbg\\gifs\\'+img+".gif")
	#urllist.append(url)
print "hahahaha"*10
print urllist

