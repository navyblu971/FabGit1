import urllib

link = "https://www.facebook.com/emilie.porchet?fref=ts"
f = urllib.urlopen(link)
myfile = f.read()
print myfile
