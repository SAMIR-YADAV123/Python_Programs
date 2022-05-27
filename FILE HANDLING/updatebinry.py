import pickle

def updatef():
      f=open("hi.txt",'rb+')
      s=pickle.load(f)
      t=0
      for i in s:
          if i[0]==3:
              i[1]=input("enter new name:")
              t+=1
              break

      if t==0:
          print("data not found!!")
      else:
          f.seek(0)
          pickle.dump(s,f)
      f.close()

def readdata():
      f = open("hi.txt", 'rb')
      st = pickle.load(f)
      print(st)
      for i in st:
          print('id:', i[0])
          print('name:', i[1])
      f.close()


updatef()
readdata()