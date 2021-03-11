# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 23:23:14 2021

@author: akshay
"""

import os


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    split=s.split(":")
    
    if (s[-2:] == "AM"):
        if (split[0]=="12"):
            split[0]= "00"
    elif(s[-2:] == "PM"):
        if (split[0]=="12"):
            split[0]= "12"
        else:
            split[0]=str(int(split[0])+12)
    time=':'.join(split)
    time=str(time[:-2])
    return time
            

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
