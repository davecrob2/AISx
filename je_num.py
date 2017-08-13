# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 13:24:36 2017

@author: davecrob2
"""

from datetime import datetime
import os

def code_gen(): 

    if not os.path.isfile("C:\\Users\\davecrob2\\Documents\\GitHub\\AIS\\jes.txt"):
        je_list=[]
    else:
        with open("C:\\Users\\davecrob2\\Documents\\GitHub\\AIS\\jes.txt",'r') as jes:
            je_list=jes.read()
            je_list=je_list.split("\n")
            je_list=list(filter(None,je_list))
        
    #Convert date into string
    today = str(datetime.now())
    
    #Convert date into integer without dashes
    today_format = today[:4]+today[5:7]+today[8:10]
    counter=1000
    str_counter = str(counter)
    je_num = today_format+str_counter
    
    
    if not je_list:
        je_list.append(je_num)
    else:
        last=je_list[-1]
        if last[:8]==je_num[:8]:
            x=int(last[8:])
            counter=x+1
            je_list.append(today_format+str(counter))
            #return(today_format+str(counter))
        else:
            je_list.append(je_num)
            #return(je_num)
    
    with open("C:\\Users\\davecrob2\\Documents\\GitHub\\AIS\\jes.txt",'w') as jes:
        for je in je_list:
            jes.write(je + "\n")
    return(je_list[-1])