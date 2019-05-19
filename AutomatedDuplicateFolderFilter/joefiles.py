def executeFile(numberExecute, filePath):
    import os
    strippedFiles = [] #this is an empty list
    #path =  os.getcwd()
    filenames = os.listdir(filePath)
    for file in filenames:
        strippedFiles.append(file[numberExecute:]) #this is adding the number to the empty list
        
    newList = [] #this is a new empty list 
    moreThanOne = '' #this is adding dup to the front of the file 
    for item in strippedFiles: 
        if strippedFiles.count(item)>1 and moreThanOne!=item:
            moreThanOne = item
            counter = 1
            
            for fileNAME in strippedFiles: #This for loop is checking to see if the files have the same name after removing letters 
                if fileNAME == moreThanOne:
                    newList.append('dup'+str(counter)+fileNAME)
                    counter+=1
        elif moreThanOne != item:
            newList.append(item)
            
    k = 0 #renmaing the files in the directory 
    for filename in filenames:
        oldpath = os.path.join(filePath, filename)
        newpath = os.path.join(filePath, newList[k])
        os.rename(oldpath,newpath)
        k+=1

