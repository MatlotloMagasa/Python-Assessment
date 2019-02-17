# -*- coding: utf-8 -*-
"""

@author: 212693013
"""
import pandas as pd
import numpy as np

#The data frame ranges from 1 to 32, this is representative of the number of DSI on system. The rows 0 to 15 are the
#16 sensores of each DSI

df = pd.DataFrame(np.random.uniform(0.00, 1.00, size=(16,32)), columns=range(1,33))
print(df)


#To iterate data
for row in df.itertuples():
    import datetime
    print(df,'Timestamp: {:%Y-%m-%d  %H:%M:%S}'.format(datetime.datetime.now()))
    
    
#Saving the data as CSV for each iteration  

df.to_csv('mySensors.csv', sep='\t')
with open('mySensors.csv') as inputFile:
   for row in  df.itertuples():
     print(row, 'Timestamp: {:%Y-%m-%d  %H:%M:%S}'.format(datetime.datetime.now())) 
    
#To store te data for the sensors in Excel:
writer = pd.ExcelWriter('mySensors.xlsx')
df.to_excel(writer, 'Matlotlo')
writer.save()

#This funtion prompts the user to monitor one of the DSI results. The user should enter the number of the DSI. Typing any 
#text will result ina value error. Create an exception for this error:

try:
    monitor=int(input("Which DSI, from 1 to 32, would you like to monitor?"))
except ValueError:
   print('Your input should not be a text')
   
except ValueError:
   print('Your input should not be a text')
   
monitor=int(input("Which DSI, from 1 to 32, would you like to monitor?"))
if monitor < 1:
   print("Pipeline regions are numbered from DSI 1 to DSI 32. Please try again")
if monitor > 32:
   print("There is no DSI regions past 32. Please enter correct DSI value from 1 to 32")
else:
   print('System loading. Please wait...') 


    

  
 
 

  
   

