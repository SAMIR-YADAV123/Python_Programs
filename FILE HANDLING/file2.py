import os,sys
fname=input("enter the file name:")
if os.path.isfile(fname):
    f=open(fname,'r')
else:
    print(fname,"does not exist:")
    sys.exit()
s=f.read()
print(s)
f.close()