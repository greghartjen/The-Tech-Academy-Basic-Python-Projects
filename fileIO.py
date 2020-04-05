
import os
import time

dirName = 'C:\\python_drill\\'

for file in os.listdir(dirName):
    if file.endswith('.txt'):
        print(os.path.join(dirName, file))
    
        print(time.ctime(os.path.getmtime(dirName)))

       
