import pickle
class copy:
  def __init__(self):
      self.id=0
      self.name=None


  def copyfile(self):
      fin=open("hi.txt",'rb')
      fout=open("file1.txt",'wb')
      st=pickle.load(fin)
      rec=[]
      for i in st:
          if i[self.id]==1 or i[self.id]==2:
            rec.append(i)
      pickle.dump(rec,fout)

      fout.seek(0)
      fin.close()
      fout.close()

  def readdata(self):
      f = open("file1.txt", 'rb')
      st = pickle.load(f)
      for i in st:
          print('id:', i[0])
          print('name:', i[1])
      f.close()

obj=copy()
#obj.copyfile()
obj.readdata()


