import os
import glob
import random
import shutil

def train_test_split(original_path,copy_path,test_path,train_path):
    
    #Deleting all current fies in the train test folders
    for filename in glob.glob(test_path+'*\\*.jpg', recursive=True):
        os.remove(filename)
    
    
    for filename in glob.glob(train_path+'*\\*.jpg', recursive=True):
        os.remove(filename)
    
    for filename in glob.glob(copy_path+'*\\*.jpg', recursive=True):
        os.remove(filename)
        

    
    #Deleting all current fies in the train test folders
    for filename in glob.glob(test_path+'*\\*.csv', recursive=True):
        os.remove(filename)
    
    
    for filename in glob.glob(train_path+'*\\*.csv', recursive=True):
        os.remove(filename)
        
    for filename in glob.glob(copy_path+'*\\*.csv', recursive=True): 
        os.remove(filename)
    
                              
    #Copying files from original folder to copy path
    for files in glob.glob(original_path+'*\\*.jpg', recursive=True): 
        source_file=files
        destination_file=files.replace('book-covers','book-covers-copy')
        shutil.copyfile(source_file,destination_file)    
    
    #Move random files for testing                          
    for folder in glob.glob(copy_path+'*', recursive=True): 
        files = os.listdir(folder)
        random_files = random.sample(files, k=100)
        for test_file in random_files:
            source_file=folder+'\\'+test_file
            destination_file=folder.replace('book-covers-copy','book-covers-test')
            shutil.move(source_file,destination_file)      
    
    #Move remaining files for training
    for folder in glob.glob(copy_path+'*', recursive=True):   
        files = os.listdir(folder)    
        for train_file in files:
            source_file=folder+'\\'+train_file
            destination_file=folder.replace('book-covers-copy','book-covers-train')
            shutil.move(source_file,destination_file)