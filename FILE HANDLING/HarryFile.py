# use open function to open a file
# f=open("sample.txt",'r')
# # data=f.read()
# data=f.read(15)
# print(data)
# data=f.read()  #AFTER 15 CHARACTER IT WILL READ FROM FILE
# print(data)
# f.close()

#READ DATA LINE BY LINE
# f=open("sample.txt",'r')

# data=f.readline()
# print(data)
# data=f.read()  #AFTER 15 CHARACTER IT WILL READ FROM FILE
# print(data)
# f.close()

#WRITTING IN THE FILE

# f=open("sample1.txt",'w')
# f.write("Google is good compnay,i would like to join\n")
# f.close()

#OPENING OF FILE USING WITH 

# with open("sample.txt",'r') as f:
#      print(f.read())

# write the tables

# for i in range(2,21):
#      with open(f"table{i}.txt",'w') as f:
#           for j in range(1,11):
#                f.write(f"{i} x {j} = {i*j}\n")
               
   
#    DELETE THE SPECIFIC CONTENT

# f=open("sample.txt",'r')

# temp=f.read();
# f=open("sample.txt",'w')
# temp=temp.replace("donkey","gooood")

# f.write(temp)
# f.close()

# find word in which line
count=0
with open("sample.txt",'r') as f:
   while(True):  
     cont=f.readline()
     if 'Microsoft' in cont:
          #  print("google is there")
           count+=1
           break
     else:
        count+=1
        
   print(f"Microsoft is present in {count} line.")     