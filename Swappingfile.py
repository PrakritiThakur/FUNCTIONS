def swapFileData():
     file1 = input("File 1 to swap")
     file2 = input("File 2 to swap with")
     with open(file1,'r')as a :
        dataA = a.read()
     with open(file2,'r')as b :
         dataB =b.read()         
     with open (file1,'w') as a :
        a.write(dataB)        
     with open(file2,'w') as b :
         b.write(dataA)       

swapFileData()
