import pymongo
myclient =pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol=mydb["customer"] #print(mydb)

#x=mycol.find_one()
#print(x)
#for i in mycol.find():
  #  print(i)
#for x in mycol.find({'_id':2}):
 #   print(x)
#find the data where the name started with s or uper then s
#myqur={'name':{"$gt":"^y"}}
#for i in mycol.find(myqur):
#   print(i)
#descending order
#mydoc=mycol.find().sort("name",-1)
#for i in mydoc:
 # print(i)

#delete one opration
#mycol.delete_one({'name':'sona'})
#for i in mycol.find():
#   print(i)

#delete many document

#mydoc={'name':{'$regex':'^r'}}
#mycol.delete_many(mydoc)
#for i in mycol.find():
#  print(i)

#update collection
#myquery={"name":"sonu"}
#newv={'$set':{'name':'sony yadav'}}
#mycol.update_one(myqur,newv)
#for i in mycol.find():
# print(i)
#myqur={'name':'sonu'}

#update many collection

#myqur={"name":{"$regex":"^s"}}
#newx={"$set":{"name":"yadavs"}}
#x=mycol.update_many(myqur,newx)
#print(x,'\n')
for i in mycol.find().limit(3):
  print(i)