l=w=c=0
wt=0
ec=0
#f=open("file1.txt",'r')
with open("file1.txt",'r') as f:
 for line in f:
    l+=1
    c+=len(line)
    words=line.split()
    for i in words:
       n=len(i)
       if i[n-1]=='e' or i[n-1]=='E':
           ec+=1
       if i[0]=='T' or i[0]=='t':
            wt+=1
    w+=len(words)
print("no. of line:",l)
print("no. of words:",w)
print("no. of character:",c)
print("no. of word satarted with t:",wt)
print("no. of word endied with e:",ec)
f.close()
