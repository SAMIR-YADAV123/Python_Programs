ec=ac=0
s=0
f=open("file1.txt",'r')
st=f.read()
n=len(st)
for i in st:
    if i=='e' or i == 'E':
       ec+=1
    elif i=='a' or i=='A':
        ac+=1
    elif i==' ':
        s+=1
print("total number of a:",ac)
print("total number of e:",ec)
print("total number of spaces:",s)

#count the numver is is
a=0
str=st.split()
for i in str:
    if i=='is':
        a+=1
print("total number of is:",a)