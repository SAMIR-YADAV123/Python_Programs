def  a(s,t):
     n=len(s)
     for i in range(n):
          if s[i]==t:
              return t

ch=input("enter the string:")
d=input("enter chractder which is searched:")
p=a(ch,d)
if p==None:
     print("character not found:")
else:
    print("character found:")