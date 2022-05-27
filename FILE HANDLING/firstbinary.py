import pickle
class customer:
    def __init__(self):
        self.id=0
        self.name=None
        self.rec=None

    def writedata(self):
        f = open("hi.txt", 'ab')
        rec=[]
        while True:
          self.id=int(input("enter the id"))
          self.name=input("enter the name:")
          li=[self.id,self.name]
          rec.append(li)
          ch=input("do you want to add more:")
          if ch=='n':
              break
        pickle.dump(rec,f)
        f.seek(0)
        f.close()

    def readdata(self):
        f=open("file1.txt",'rb')
        st=pickle.load(f)
        print(st)
        for i in st:
           print('id:',i[0])
           print('name:',i[1])
        f.close()



obj=customer()
obj.writedata()
#obj.readdata()
