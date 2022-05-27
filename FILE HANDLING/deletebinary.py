import pickle
def deletfile():
    fi=open('file1.txt','rb+')
    ch=int(input("enter the id which you want to delete:"))
    st=pickle.load(fi)
    rec=[]
    fo=0
    for i in st:
        if i[0]==ch:
           fo+=1
        else:
          rec.append(i)

    if fo==0:
        print("data not found:")
    else:
       fi.seek(0)
       pickle.dump(rec,fi)

def show():
    f=open("file1.txt",'rb')
    st=pickle.load(f)


    for i in st:
        print('ID:',i[0])
        print('name:',i[1])

deletfile()
show()



