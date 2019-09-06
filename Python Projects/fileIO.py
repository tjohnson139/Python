import os
import time
import datetime

fPath = 'C:\\Users\\Tyler\\Desktop\\Coding\\Python\\Python Projects\\A\\'
pathList = os.listdir(fPath)

for name in os.listdir(fPath):
    path = os.path.join(fPath, name)
    if path.endswith('.txt'):
        print(path + ' was modified ' + time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(path))))
