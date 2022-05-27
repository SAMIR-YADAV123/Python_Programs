import pymongo
myclient =pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol=mydb["customer"] #print(mydb)
#del mycol
#data=[{'_id':2,'name':'pintu','age':26}]
    #  {'_id':5,'name':'ritik','age': 22}]
      #  {'_id':3,'name':'sonu','age':25}]
#mycol.insert_many(data)
#myl=[{"name":'samir',"rno":'20'}]
#mycol.insert_one(myl)
#x=mycol.find_one()
#print(x)
#dblist = myclient.list_database_names()
#print(dblist)#.list_database_names())
#if 'mydatabase' in dblist:
 # print("The database exists.")