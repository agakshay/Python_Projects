# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 23:59:49 2021

@author: aksha
"""


# Complete the minimumPasses function below.
    
print ("Enter m, w, p, n in order :")
m = int(input())

w = int(input())

p = int(input())

n = int(input())


no_candies = m*w
count=count1=count2=count3=new_p=0

while(no_candies <= n):
    if no_candies<(n/2):
        if (p>no_candies):
            x=int(p/no_candies)
            new_p=p//(x*m*w)  
            rem=p-(x*m*w)
            if (rem>0):
               x=(p+rem)/(m*w) 
            count1=count1+x            
            
        elif(p<no_candies):
            x=int(no_candies/p)
            new_p=(x*m*w)//p
            rem = no_candies-(x*p)
            count2=count2+x
        else:
            x=int(p/no_candies)
            new_p=1
            rem = 0
            count3=count3+x
           
        
        val = m+w+new_p
        m= int(val//2)       
        w = int(val-m)       
        num_candies= m*w
        no_candies = num_candies+rem
        count = count1+count2+count3
        # print("After count "+str(count))
        # print("m "+str(m))
        # print("w "+str(w))
        # print("rem candies "+str(rem))
        # print("next no candies "+str(no_candies))

    else:
        # print("else")
        count=count+1
        # print("count "+str(count))
        no_candies=no_candies*2
        # print("no candies "+str(no_candies))
    
print("third "+str(int(count)))