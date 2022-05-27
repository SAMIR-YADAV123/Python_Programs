st=input("enter the string:")
uc=0
lc=0
d=0
s=0
ln=len(st)
for i in range(0,ln):
     ch=st[i]
     if ch>='A' and ch<='Z':
           uc+=1
     elif ch>='a' and ch<='z':
           lc+=1
     elif (ch.isdigit()):
            d+=1
     else:
           s+=1
print("total number of uper case:",uc)
print("total number of lower case:",lc)
print("total number of digit:",d)
print("total number of special char:",s)
