# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 15:28:06 2017

@author: davecrob2
"""
import csv
from je_num import code_gen
import json

JE = {}

def gl_add():
    password=input("Enter a Password")
    
    #Poor man's security
    if password == "Password":
        
        #Requests Account Name and Number to be added
        Account_Name=input("Enter an Account Name")
        Account_Number=input("Enter an Account Number")
    
    
    #Writes Account Name and Account Number inputs into a .json dictionary
        with open('gl.json','r') as fp:
            json_data=json.load(fp)
            json_data[Account_Name]=int(Account_Number)
        with open('gl.json','w') as fp:
            fp.write(json.dumps(json_data))

def JE_writer():
    code=code_gen()
    Account_Number=input("Enter an Account Number")
    Amount =input("Enter an Amount")
    JE[code]=[Account_Number,Amount]
    with open("C:\\Users\\davecrob2\\Documents\\GitHub\\AIS\\jeextract.csv",'w') as je_csv:
        writer =csv.writer(je_csv)
        for key, value in JE.items():
            writer.writerow([key,value])
    return JE

